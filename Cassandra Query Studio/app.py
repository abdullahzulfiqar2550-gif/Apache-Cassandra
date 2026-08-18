import streamlit as st
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import pandas as pd
import time

# Create keyspace company with replication={'class': 'SimpleStrategy', 'replication_factor': 1};
# use company;
# create table employee(
#     emp_id int primary key,
#     emp_name text,
#     age int,
#     department text,
#     salary Decimal,
# )
# INSERT INTO employee (emp_id, emp_name, age, department, salary) VALUES (1, 'ABDULLAH', 30, ' AI Engineering', 75000.00);
# INSERT INTO employee (emp_id, emp_name, age, department, salary) VALUES (2, 'ALI', 28, 'DATA SCIENCE', 65000.00);
# select * from employee;
# upadate employee set salary=80000.00 where emp_id=1;
# delete from employee where emp_id=2;
# drop table employee;
# drop keyspace company;

@st.cache_resource
def get_session():
    for _ in range(10):
        try:
            cluster = Cluster(["cassandra"])
            session = cluster.connect()
            return session
        except Exception:
            time.sleep(3)
    st.error("Cannot connect to Cassandra.")
    st.stop()

session = get_session()

def get_keyspaces():
    rows = session.execute("SELECT keyspace_name FROM system_schema.keyspaces")
    return [r.keyspace_name for r in rows if not r.keyspace_name.startswith("system")]

def get_tables(keyspace):
    rows = session.execute("SELECT table_name FROM system_schema.tables WHERE keyspace_name=%s", [keyspace])
    return [r.table_name for r in rows]

def run_query(cql):
    cql = cql.strip()
    if not cql:
        return None, "Query is empty."
    try:
        result = session.execute(cql)
        return result, None
    except Exception as e:
        return None, str(e)

def is_read(cql):
    return cql.strip().upper().startswith("SELECT")


st.sidebar.title("Cassandra GUI Tool")
keyspaces = get_keyspaces()

if keyspaces:
    chosen_ks = st.sidebar.selectbox("Keyspace", keyspaces)
    tables = get_tables(chosen_ks)
    if tables:
        st.sidebar.markdown("**Tables**")
        for t in tables:
            st.sidebar.markdown(f"&nbsp;&nbsp;• `{t}`")
    else:
        st.sidebar.info("No tables yet.")
else:
    st.sidebar.info("No user keyspaces found.")


st.title("Cassandra Query Runner")
st.caption("Write any CQL — SELECT, INSERT, UPDATE, DELETE, CREATE, DROP")

cql_input = st.text_area("CQL Query", height=160, placeholder="SELECT * FROM mykeyspace.mytable;")

if st.button("Execute", use_container_width=True):
    result, error = run_query(cql_input)

    if error:
        st.error(f"**Error:** {error}")
    else:
        st.success("Query executed successfully.")

        if is_read(cql_input):
            rows = list(result)
            if rows:
                cols = result.column_names
                df = pd.DataFrame(rows, columns=cols)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("Query returned no rows.")