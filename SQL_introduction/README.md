<a href="#"><img src="https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# SQL - Introduction

## **[0. List databases](0-list_databases.sql)**

Write a script that lists all databases of your MySQL server.

<details>
<summary>Show answer</summary>

```sql
SHOW DATABASES;
```
</details>

---

## **[1. Create a database](1-create_database_if_missing.sql)**

Write a script that creates the database hbtn_0c_0 in your MySQL server.

  * If the database `hbtn_0c_0` already exists, your script should not fail
  * You are not allowed to use the `SELECT` or `SHOW` statements

<details>
<summary>Show answer</summary>

```sql
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```
</details>

---

## **[2. Delete a database](2-remove_database.sql)**

Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

  * If the database `hbtn_0c_0` doesn't exist, your script should not fail
  * You are not allowed to use the `SELECT` or `SHOW` statements

<details>
<summary>Show answer</summary>

```sql
DROP DATABASE IF EXISTS hbtn_0c_0;
```
</details>

---

## **[3. List tables](3-list_tables.sql)**

Write a script that lists all the tables of a database in your MySQL server.

  * The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

<details>
<summary>Show answer</summary>

```sql
SHOW TABLES;
```
</details>

---

## **[4. First table](4-first_table.sql)**

Write a script that creates a table called `first_table` in the current database in your MySQL server.

  * `first_table` description:
  * `id` INT
  * `name` VARCHAR(256)
  * The database name will be passed as an argument of the `mysql` command
  * If the table `first_table` already exists, your script should not fail
  * You are not allowed to use the `SELECT` or `SHOW` statements

<details>
<summary>Show answer</summary>

```sql
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```
</details>

---

## **[5. Full description](5-full_table.sql)**

Write a script that prints the following description of the table `first_table` from the database hbtn_0c_0 in your MySQL server.

  * The database name will be passed as an argument of the `mysql` command
  * You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

<details>
<summary>Show answer</summary>

```sql
SHOW CREATE TABLE first_table;
```
</details>

---

## **[6. List all in table](6-list_values.sql)**

Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

  * All fields should be printed
  * The database name will be passed as an argument of the `mysql` command

<details>
<summary>Show answer</summary>

```sql
SELECT * FROM first_table;
```
</details>

---

## **[7. First add](7-insert_value.sql)**

Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

  * New row:
  * `id` = `89`
  * `name` = `Best School`
  * The database name will be passed as an argument of the `mysql` command

<details>
<summary>Show answer</summary>

```sql
INSERT INTO first_table (id, name)
VALUES (89, 'Best School');
```
</details>

---

## **[8. Count 89](8-count_89.sql)**

Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

  * The database name will be passed as an argument of the `mysql` command

<details>
<summary>Show answer</summary>

```sql
SELECT COUNT(*) FROM first_table WHERE id = 89;
```
</details>

---

## **[9. Full creation](9-full_creation.sql)**

Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

  * `second_table` description:
  * `id` INT
  * `name` VARCHAR(256)
  * `score` INT
  * The database name will be passed as an argument to the `mysql` command
  * If the table `second_table` already exists, your script should not fail
  * You are not allowed to use the `SELECT` and `SHOW` statements
  * Your script should create these records:
  * `id` = 1, `name` = "John", `score` = 10
  * `id` = 2, `name` = "Alex", `score` = 3
  * `id` = 3, `name` = "Bob", `score` = 14
  * `id` = 4, name = "George", `score` = 8

<details>
<summary>Show answer</summary>

```sql
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
```
</details>

---

## **[10. List by best](10-top_score.sql)**

Write a script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.

  * Results should display both the score and the name (in this order)
  * Records should be ordered by score (top first)
  * The database name will be passed as an argument of the mysql command

<details>
<summary>Show answer</summary>

```sql
SELECT score, name FROM second_table ORDER BY score DESC;
```
</details>

---

## **[11. Select the best](11-best_score.sql)**

Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

  * Results should display both the score and the name (in this order)
  * Records should be ordered by score (top first)
  * The database name will be passed as an argument of the `mysql` command

<details>
<summary>Show answer</summary>

```sql
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
```
</details>

---

## **[12. Cheating is bad](12-no_cheating.sql)**

Write a script that updates the score of Bob to 10 in the table `second_table`.

  * You are not allowed to use Bob's id value, only the `name` field
  * The database name will be passed as an argument of the `mysql` command

<details>
<summary>Show answer</summary>

```sql
UPDATE second_table
SET score = 10
WHERE name = 'Bob';
```
</details>

---

## **[13. Score too low](13-change_class.sql)**

Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

  * The database name will be passed as an argument of the `mysql` command

<details>
<summary>Show answer</summary>

```sql
DELETE FROM second_table WHERE score <= 5;
```
</details>

---

## **[14. Average](14-average.sql)**

Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

  * The result column name should be `average`
  * The database name will be passed as an argument of the `mysql` command

<details>
<summary>Show answer</summary>

```sql
SELECT AVG(score) AS average FROM second_table;
```
</details>

---

## **[15. Number by score](15-groups.sql)**

Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

  * The result should display:
  * the `score`
  * the number of records for this `score` with the label `number`
  * The list should be sorted by the number of records (descending)
  * The database name will be passed as an argument to the `mysql` command

<details>
<summary>Show answer</summary>

```sql
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
```
</details>

---

## **[16. Say my name](16-no_link.sql)**

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

  * Don't list rows where the `name` column does not contain a value
  * Results should display the score and the name (in this order)
  * Records should be listed by descending score
  * The database name will be passed as an argument to the `mysql` command

In this example, new data have been added to the table `second_table`.

<details>
<summary>Show answer</summary>

```sql
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
```
</details>

---

## **[17. Go to UTF8](100-move_to_utf8.sql)**
**`advanced`**

Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

You need to convert all of the following to `UTF8`:

  * Database `hbtn_0c_0`
  * Table `first_table`
  * Field `name` in `first_table`

<details>
<summary>Show answer</summary>

```sql
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE first_table MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
</details>

---

## **[18. Temperatures #0](101-avg_temperatures.sql)**
**`advanced`**

Import in `hbtn_0c_0` database this table dump: [download](temperatures.sql)

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

<details>
<summary>Show answer</summary>

```sql
SELECT city, AVG(value) AS avg_temp FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
```
</details>

---

## **[19. Temperatures #1](102-top_city.sql)**
**`advanced`**

Import in `hbtn_0c_0` database this table dump: [download](temperatures.sql) (same as `Temperatures #0`)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

<details>
<summary>Show answer</summary>

```sql
SELECT city, AVG(value) AS avg_temp FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
```
</details>

---

## **[20. Temperatures #2](103-max_state.sql)**
**`advanced`**

Import in `hbtn_0c_0` database this table dump: [download](temperatures.sql) (same as `Temperatures #0`)

Write a script that displays the max temperature of each state (ordered by State name).

<details>
<summary>Show answer</summary>

```sql
SELECT state, MAX(value) as max_temp FROM temperatures
GROUP BY state
ORDER BY state ASC;
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 02/03/26 to 06/03/26 for Holberton School Bordeaux
