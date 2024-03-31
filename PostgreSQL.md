
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

## 注意事项

- 示例操作假设您已经具备一定的 SQL 知识。
- 实际应用中通常会优先使用 `jsonb` 类型，因为它提供了更多功能并且性能更优。
- 根据实际情况，您可能需要调整查询和更新 JSON 数据的方法。
