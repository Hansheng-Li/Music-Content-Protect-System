
# PostgreSQL 创建表和插入数据指南


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
