# Learn Cassandra by Building

A practical, hands-on repository for learning **Apache Cassandra** through CQL, data modeling, database operations, and distributed database concepts.

This repository focuses on building Cassandra knowledge by writing and executing real commands instead of only studying theory.

## 📚 Topics Covered

### 1. Cassandra Installation & Setup

* Apache Cassandra installation on macOS
* Apache Cassandra installation on Windows
* Java/JDK configuration
* Python and `cqlsh` setup
* Cassandra service management
* Connecting to Cassandra using `cqlsh`
* Checking Cassandra version

### 2. Keyspaces

* Creating keyspaces
* Using keyspaces
* Replication configuration
* `SimpleStrategy`
* `NetworkTopologyStrategy`
* Replication factor

### 3. Tables & CRUD Operations

* Creating tables
* Inserting data
* Reading data
* Updating data
* Deleting data
* `TRUNCATE`
* `DROP TABLE`
* `DROP KEYSPACE`

### 4. Primary Keys & Data Modeling

* Partition keys
* Clustering keys
* Composite partition keys
* Understanding how Cassandra distributes data
* Designing tables according to query patterns

### 5. Cassandra Data Types

* `TEXT`
* `INT`
* `FLOAT`
* `BOOLEAN`
* `UUID`
* `DATE`
* `TIMESTAMP`

### 6. Collections

Working with Cassandra collection types:

* **LIST**
* **SET**
* **MAP**
* Inserting collection values
* Updating collection values

### 7. Indexes

* Creating indexes
* Querying indexed columns
* Describing tables
* Dropping indexes
* Understanding when indexes are useful

### 8. TTL — Time To Live

* Applying TTL to records
* Automatic expiration of data
* Checking remaining TTL
* Understanding Cassandra's automatic data expiration

### 9. Replication

Understanding Cassandra's distributed architecture through:

* `SimpleStrategy`
* `NetworkTopologyStrategy`
* Replication factor
* Multi-datacenter replication
* Data distribution concepts

### 10. Consistency Levels

Practical exploration of:

* `CONSISTENCY ONE`
* `CONSISTENCY QUORUM`
* `CONSISTENCY ALL`

Understanding the relationship between **consistency, availability, and distributed data**.

### 11. Compaction & Tombstones

* Cassandra compaction
* Tombstones
* Why deleted data creates tombstones
* How compaction manages storage
* Impact of tombstones on Cassandra performance

---

## 🎯 Learning Approach

The repository follows a **build-first approach**:

```text
Installation
     ↓
Keyspaces
     ↓
Tables
     ↓
CRUD Operations
     ↓
Primary Keys
     ↓
Data Modeling
     ↓
Data Types
     ↓
Collections
     ↓
Indexes
     ↓
TTL
     ↓
Replication
     ↓
Consistency Levels
     ↓
Compaction & Tombstones
```

## 🧠 Key Cassandra Concepts

One of the main goals of this repository is to understand that Cassandra data modeling is **query-driven**.

Instead of designing tables exactly like a traditional relational database, Cassandra requires thinking about:

* How data will be queried
* Partition-key selection
* Clustering-key design
* Data distribution
* Replication
* Consistency
* High availability
* Distributed storage

## 🛠️ Technologies

* **Apache Cassandra**
* **CQL — Cassandra Query Language**
* **cqlsh**
* **Java / JDK**
* **Python**
* **Homebrew**
* **Chocolatey**
* **Windows**
* **macOS**

## 🚀 What I Am Building

This repository is part of my broader journey into **SQL, NoSQL, databases, and data engineering**.

The goal is not simply to memorize Cassandra commands, but to develop practical knowledge of **distributed database architecture, data modeling, scalability, replication, and consistency**.


## ⭐ Purpose

**Learn Cassandra by Building — from basic CQL operations to distributed database concepts.**

If you find this repository useful, consider giving it a ⭐ on GitHub.
