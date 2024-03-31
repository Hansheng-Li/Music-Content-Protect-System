
# PostgreSQL 创建表和插入数据指南
[Link](https://www.runoob.com/postgresql/postgresql-data-type.html)

## 创建表格

创建一个新表`users`，包括用户ID、姓名和邮箱地址：

```sql
Create table If Not Exists users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(255) UNIQUE NOT NULL
);
```

## 插入数据

向`users`表中插入数据：

```sql
TRUNCATE TABLE users
INSERT INTO users (name, email) VALUES ('张三', 'zhangsan@example.com');
```
TRUNCATE TABLE命令用于立即删除表内的所有行，但不删除表本身。这个命令比使用DELETE命令删除所有行要快得多，因为它不扫描表中的每一行来删除，而是直接删除数据文件并重新初始化表空间。TRUNCATE也不会触发表的任何删除触发器。需要注意的是，这个操作是不可逆的，一旦执行，之前表中的所有数据都会丢失。

一次插入多条数据：

```sql
INSERT INTO users (name, email) VALUES 
('李四', 'lisi@example.com'),
('王五', 'wangwu@example.com');
```

## 查询数据

使用`SELECT`语句来查询数据：

```sql
SELECT * FROM users;
```

## 更新和删除数据

- 更新数据：

  ```sql
  UPDATE users SET email = 'newemail@example.com' WHERE user_id = 1;
  ```

- 删除数据：

  ```sql
  DELETE FROM users WHERE user_id = 1;
  ```

## 使用外键

创建`orders`表，并使用外键关联到`users`表的`user_id`：

```sql
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    user_id INTEGER REFERENCES users(user_id),
    order_total DECIMAL(10, 2)
);
```

## 创建索引

提高查询效率的方法之一，创建索引：

```sql
CREATE INDEX idx_users_email ON users(email);
```

## 批量插入数据

一次性插入多条记录：

```sql
INSERT INTO users (name, email) VALUES 
('赵六', 'zhaoliu@example.com'),
('孙七', 'sunqi@example.com'),
('周八', 'zhouba@example.com');
```

## 使用COPY命令

对于大规模数据插入，`COPY`命令是更快的选择：

```sql
COPY users(name, email) FROM '/path/to/your/datafile.csv' DELIMITER ',' CSV;
```

## 处理重复数据

`ON CONFLICT`语句用于处理插入重复数据的情况：

```sql
INSERT INTO users (user_id, name, email) VALUES 
(1, '新名字', 'newemail@example.com')
ON CONFLICT (user_id) 
DO UPDATE SET name = EXCLUDED.name, email = EXCLUDED.email;
```


# psycopg2 数据插入方法总结

在使用 `psycopg2` 这个 PostgreSQL 数据库适配器进行数据插入时，有多种方法可以实现参数的传递和数据的插入。

## 使用 `%s` 作为占位符

最常见的方法是使用 `%s` 作为参数占位符。

```python
cur.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", ("Alice", "alice@example.com", 30))
```

## 使用命名参数

通过使用命名的方式来插入数据，让代码更加清晰易懂。

```python
sql = "INSERT INTO users (name, email, age) VALUES (%(name)s, %(email)s, %(age)s)"
data = {"name": "Alice", "email": "alice@example.com", "age": 30}
cur.execute(sql, data)
```

## 使用 `executemany` 方法批量插入

当有多条数据需要插入时，可以使用 `executemany` 方法。

```python
sql = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
data = [("Alice", "alice@example.com", 30),
        ("Bob", "bob@example.com", 25)]
cur.executemany(sql, data)
```

## 使用 `psycopg2.sql` 模块构建动态 SQL

为了更灵活地构建 SQL 语句，可以使用 `psycopg2.sql` 模块。

```python
from psycopg2 import sql

sql_query = sql.SQL("INSERT INTO users (name, email, age) VALUES ({}, {}, {})").format(
    sql.Literal("Alice"),
    sql.Literal("alice@example.com"),
    sql.Literal(30)
)
cur.execute(sql_query)
```

这些方法各有优势，可以根据实际情况和个人偏好来选择。


# PostgreSQL JSON 处理指南

PostgreSQL 的 JSON 支持使得我们可以在数据库中直接存储、查询和处理 JSON 格式的数据。这对于需要处理复杂数据结构的应用来说极其有用。以下是一些关于如何在 PostgreSQL 中操作 JSON 数据的基本示例。

## 准备工作

首先，我们需要创建一个包含 JSON 数据的表。例如，我们创建一个名为 `user_profiles` 的表，它包含 `id` 和 `profile` 两个字段。

```sql
CREATE TABLE user_profiles (
    id SERIAL PRIMARY KEY,
    profile JSON NOT NULL
);
```

## 插入 JSON 数据

向 `user_profiles` 表中插入包含 JSON 数据的记录的示例。

```sql
INSERT INTO user_profiles (profile)
VALUES
  ('{"name": "张三", "age": 28, "interests": ["游泳", "阅读"]}'),
  ('{"name": "李四", "age": 32, "interests": ["跑步", "音乐"], "address": {"city": "北京", "street": "长安街"}}');
```

## 查询 JSON 数据

### 查询整个 JSON 字段

检索整个 `profile` 字段内容的查询。

```sql
SELECT profile FROM user_profiles;
```

### 查询 JSON 字段的特定元素

使用 `->` 操作符获取 JSON 对象的某个字段值。

```sql
SELECT profile->'name' AS name FROM user_profiles;
```

### 查询 JSON 字段内嵌套的元素

使用 `->` 和 `->>` 操作符查询嵌套的 JSON 对象。

```sql
SELECT profile->'address'->>'city' AS city FROM user_profiles WHERE profile->'address' IS NOT NULL;
```

### 根据 JSON 字段的内容进行筛选

根据 JSON 字段内容筛选记录的示例。

```sql
SELECT * FROM user_profiles
WHERE profile->'interests' ? '游泳';
```

### 更新 JSON 字段

更新 JSON 字段，例如添加一个新的兴趣爱好。

```sql
UPDATE user_profiles
SET profile = jsonb_set(profile, '{interests}', profile->'interests' || '"旅行"')
WHERE id = 1;
```
# Python 连接 PostgreSQL 操作手册

本手册提供了使用 Python 连接 PostgreSQL 并进行常见数据库操作的示例代码。

## 准备工作

确保安装了 `psycopg2` 库。如果尚未安装，请运行以下命令：

```bash
pip install psycopg2
```

## 示例代码

### 1. 连接数据库

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

### 2. 创建表

```python
cur.execute("""
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    age INT
)
""")
conn.commit()
```

### 3. 插入数据

```python
cur.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", ("Alice", "alice@example.com", 30))
conn.commit()
```

### 4. 查询数据

```python
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)
```

### 5. 更新数据

```python
cur.execute("UPDATE users SET age = %s WHERE name = %s", (31, "Alice"))
conn.commit()
```

### 6. 删除数据

```python
cur.execute("DELETE FROM users WHERE name = %s", ("Alice",))
conn.commit()
```

### 7. 批量插入数据

```python
users = [("Bob", "bob@example.com", 25), ("Charlie", "charlie@example.com", 28)]
cur.executemany("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", users)
conn.commit()
```

### 8. 查询特定条件的数据

```python
cur.execute("SELECT * FROM users WHERE age > %s", (26,))
rows = cur.fetchall()
for row in rows:
    print(row)
```

### 9. 计数查询

```python
cur.execute("SELECT COUNT(*) FROM users")
count = cur.fetchone()[0]
print(f"Total users: {count}")
```

### 10. 删除表

```python
cur.execute("DROP TABLE users")
conn.commit()
```

### 高级操作

本部分提供了一些高级数据库操作的示例，包括事务处理、批量操作、索引和性能优化等。

### 11. 事务处理

```python
conn.autocommit = False
try:
    cur.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", ("Daisy", "daisy@example.com", 24))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
```

### 12. 批量操作优化

```python
data = [("Eva", "eva@example.com", 22), ("Frank", "frank@example.com", 29)]
cur.executemany("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", data)
conn.commit()
```

...

此文件只包含部分代码示例，完整示例请参考上述回答。


