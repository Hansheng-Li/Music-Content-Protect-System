# PostgreSQL guide to creating tables and inserting data
[Link](https://www.runoob.com/postgresql/postgresql-data-type.html)

## Create table

Create a new table `users`, including user IDs, names and email addresses:

```sql
Create table If Not Exists users (
     user_id SERIAL PRIMARY KEY,
     name VARCHAR(50),
     email VARCHAR(255) UNIQUE NOT NULL
);
```

## Insert data

Insert data into the `users` table:

```sql
TRUNCATE TABLE users
INSERT INTO users (name, email) VALUES ('Zhang San', 'zhangsan@example.com');
```
The TRUNCATE TABLE command is used to immediately delete all rows within a table, but not the table itself. This command is much faster than using the DELETE command to delete all rows because it does not scan every row in the table to delete, but directly deletes the data file and re-initializes the table space. TRUNCATE will also not fire any delete triggers for the table. It should be noted that this operation is irreversible. Once executed, all data in the table will be lost.

Insert multiple pieces of data at once:

```sql
INSERT INTO users (name, email) VALUES
('Li Si', 'lisi@example.com'),
('wangwu', 'wangwu@example.com');
```

## Query data

Use the `SELECT` statement to query data:

```sql
SELECT * FROM users;
```

## Update and delete data

- update data:

   ```sql
   UPDATE users SET email = 'newemail@example.com' WHERE user_id = 1;
   ```

- delete data:

   ```sql
   DELETE FROM users WHERE user_id = 1;
   ```

## Use foreign keys

Create the `orders` table and associate it to the `user_id` of the `users` table using a foreign key:

```sql
CREATE TABLE orders (
     order_id SERIAL PRIMARY KEY,
     order_date DATE NOT NULL,
     user_id INTEGER REFERENCES users(user_id),
     order_total DECIMAL(10, 2)
);
```

## Create index

One of the ways to improve query efficiency is to create an index:

```sql
CREATE INDEX idx_users_email ON users(email);
```

## Insert data in batches

Insert multiple records at once:

```sql
INSERT INTO users (name, email) VALUES
('Zhaoliu', 'zhaoliu@example.com'),
('Sun Qi', 'sunqi@example.com'),
('zhouba', 'zhouba@example.com');
```

## Use the COPY command

For large-scale data insertion, the `COPY` command is a faster option:

```sql
COPY users(name, email) FROM '/path/to/your/datafile.csv' DELIMITER ',' CSV;
```

## Handle duplicate data

The `ON CONFLICT` statement is used to handle the situation of inserting duplicate data:

```sql
INSERT INTO users (user_id, name, email) VALUES
(1, 'new name', 'newemail@example.com')
ON CONFLICT (user_id)
DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email;
```


# psycopg2 data insertion method summary

When using `psycopg2`, the PostgreSQL database adapter, for data insertion, there are many ways to pass parameters and insert data.

## Use `%s` as placeholder

The most common way is to use `%s` as a parameter placeholder.

```python
cur.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", ("Alice", "alice@example.com", 30))
```

## Use named parameters

By using naming to insert data, the code is clearer and easier to understand.

```python
sql = "INSERT INTO users (name, email, age) VALUES (%(name)s, %(email)s, %(age)s)"
data = {"name": "Alice", "email": "alice@example.com", "age": 30}
cur.execute(sql, data)
```

## Use the `executemany` method to insert in batches

When multiple pieces of data need to be inserted, you can use the `executemany` method.

```python
sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
data = [("Alice", "alice@example.com", 30),
         ("Bob", "bob@example.com", 25)]
cur.executemany(sql, data)
```

## Use the `psycopg2.sql` module to build dynamic SQL

For more flexibility in building SQL statements, the `psycopg2.sql` module can be used.

```python
from psycopg2 import sql

sql_query = sql.SQL("INSERT INTO users (name, email, age) VALUES ({}, {}, {})").format(
     sql.Literal("Alice"),
     sql.Literal("alice@example.com"),
     sql.Literal(30)
)
cur.execute(sql_query)
```

Each of these methods has its own advantages and can be chosen based on the actual situation and personal preference.


# PostgreSQL JSON Processing Guide

PostgreSQL's JSON support allows us to store, query, and process data in JSON format directly in the database. This is extremely useful for applications that need to deal with complex data structures. Here are some basic examples of how to manipulate JSON data in PostgreSQL.

## Preparation

First, we need to create a table containing JSON data. For example, we create a table named `user_profiles`, which contains two fields: `id` and `profile`.

```sql
CREATE TABLE user_profiles (
     id SERIAL PRIMARY KEY,
     profile JSON NOT NULL
);
```

## Insert JSON data

Example of inserting records containing JSON data into the `user_profiles` table.

```sql
INSERT INTO user_profiles (profile)
VALUES
   ('{"name": "张三", "age": 28, "interests": ["swimming", "reading"]}'),
   ('{"name": "李思", "age": 32, "interests": ["running", "music"], "address": {"city": "Beijing", "street": " Chang'an Street"}}');
```

## Query JSON data

### Query the entire JSON field

A query that retrieves the contents of the entire `profile` field.

```sql
SELECT profile FROM user_profiles;
```

### Query specific elements of JSON fields

Use the `->` operator to get a field value of a JSON object.

```sql
SELECT profile->'name' AS name FROM user_profiles;
```

### Query nested elements within a JSON field

Query nested JSON objects using the `->` and `->>` operators.

```sql
SELECT profile->'address'->>'city' AS city FROM user_profiles WHERE profile->'address' IS NOT NULL;
```

### Filter based on the contents of JSON fields

Example of filtering records based on JSON field content.

```sql
SELECT * FROM user_profiles
WHERE profile->'interests' ? 'Swimming';
```

### Update JSON fields

Update a JSON field, such as adding a new interest.

```sql
UPDATE user_profiles
SET profile = jsonb_set(profile, '{interests}', profile->'interests' || '"Travel"')
WHERE id = 1;
```
# Python connection PostgreSQL operation manual

This manual provides sample code for using Python to connect to PostgreSQL and perform common database operations.

## Preparation

Make sure the `psycopg2` library is installed. If it is not installed yet, run the following command:

```bash
pip install psycopg2
```

## Sample code

### 1. Connect to the database

```python
import psycopg2

conn = psycopg2.connect(
     dbname="testdb",
     user="your_username",
     password="your_password",
     host="localhost"
)
cur = conn.cursor()
```

### 2. Create table

```python
cur.execute("""
CREATE TABLE users (
     id SERIAL PRIMARY KEY,
     name VARCHAR(50),
     email VARCHAR(50),
     ageINT
)
""")
conn.commit()
```

### 3. Insert data

```python
cur.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", ("Alice", "alice@example.com", 30))
conn.commit()
```

### 4. Query data

```python
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
     print(row)
```

### 5. Update data

```python
cur.execute("UPDATE users SET age = %s WHERE name = %s", (31, "Alice"))
conn.commit()
```

### 6. Delete data

```python
cur.execute("DELETE FROM users WHERE name = %s", ("Alice",))
conn.commit()
```

### 7. Insert data in batches

```python
users = [("Bob", "bob@example.com", 25), ("Charlie", "charlie@example.com", 28)]
cur.executemany("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", users)
conn.commit()
```

### 8. Query data under specific conditions

```python
cur.execute("SELECT * FROM users WHERE age > %s", (26,))
rows = cur.fetchall()
for row in rows:
     print(row)
```

### 9. Count query

```python
cur.execute("SELECT COUNT(*) FROM users")
count = cur.fetchone()[0]
print(f"Total users: {count}")
```

### 10. Delete table

```python
cur.execute("DROP TABLE users")
conn.commit()
```

### Advanced operations

This section provides examples of advanced database operations, including transaction processing, batch operations, indexing, and performance optimization.

### 11. Transaction processing

```python
conn.autocommit = False
try:
     cur.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", ("Daisy", "daisy@example.com", 24))
     conn.commit()
except Exception as e:
     conn.rollback()
     print(e)
```

### 12. Batch operation optimization

```python
data = [("Eva", "eva@example.com", 22), ("Frank", "frank@example.com", 29)]
cur.executemany("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", data)
conn.commit()
```
 


