Server [localhost]:
Database [postgres]:
Port [5432]:
Username [postgres]:
Password for user postgres:

psql (18.7)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

postgres=# \c college
You are now connected to database "college" as user "postgres".
college=# \dt
           List of tables
 Schema |  Name   | Type  |  Owner
--------+---------+-------+----------
 public | student | table | postgres
(1 row)


college=# \l
                                                            List of databases
   Name    |  Owner   | Encoding | Locale Provider |      Collate       |       Ctype        | Locale | ICU Rules |   Access privileges
-----------+----------+----------+-----------------+--------------------+--------------------+--------+-----------+-----------------------
 college   | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 postgres  | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 student   | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           |
 template0 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
 template1 | postgres | UTF8     | libc            | English_India.1252 | English_India.1252 |        |           | =c/postgres          +
           |          |          |                 |                    |                    |        |           | postgres=CTc/postgres
(5 rows)


college=# CREATE TABLE student (
college(#     id SERIAL PRIMARY KEY,
college(#     name VARCHAR(100),
college(#     age INT,
college(#     course VARCHAR(50),
college(#     marks INT
college(# );
ERROR:  relation "student" already exists
college=# \d student
                                    Table "public.student"
 Column |          Type          | Collation | Nullable |               Default
--------+------------------------+-----------+----------+-------------------------------------
 id     | integer                |           | not null | nextval('student_id_seq'::regclass)
 name   | character varying(100) |           |          |
 age    | integer                |           |          |
 course | character varying(50)  |           |          |
 marks  | integer                |           |          |
Indexes:
    "student_pkey" PRIMARY KEY, btree (id)


college=# insert into student(name,age,course,marks)
college-# values
college-# ('rahul',20,'bca',90),
college-# ('rohith',20,'ece',90),
college-# ('satyam',20,'cse',90),
college-# ('srija',19,'mech',90);
INSERT 0 4
college=# select * from student;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  1 | rahul  |  20 | bca    |    90
  2 | rohith |  20 | ece    |    90
  3 | satyam |  20 | cse    |    90
  4 | srija  |  19 | mech   |    90
(4 rows)


college=# select * from student where marks>80;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  1 | rahul  |  20 | bca    |    90
  2 | rohith |  20 | ece    |    90
  3 | satyam |  20 | cse    |    90
  4 | srija  |  19 | mech   |    90
(4 rows)


college=# select * from student orderby acs;
ERROR:  syntax error at or near "acs"
LINE 1: select * from student orderby acs;
                                      ^
college=# select * from student orderby asc;
ERROR:  syntax error at or near "asc"
LINE 1: select * from student orderby asc;
                                      ^
college=# select * from student orderby marks asc;
ERROR:  syntax error at or near "marks"
LINE 1: select * from student orderby marks asc;
                                      ^
college=# select * from student order by marks asc;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  1 | rahul  |  20 | bca    |    90
  2 | rohith |  20 | ece    |    90
  3 | satyam |  20 | cse    |    90
  4 | srija  |  19 | mech   |    90
(4 rows)


college=# select * from student order by marks dsc;
ERROR:  syntax error at or near "dsc"
LINE 1: select * from student order by marks dsc;
                                             ^
college=# select * from student order by marks des;
ERROR:  syntax error at or near "des"
LINE 1: select * from student order by marks des;
                                             ^
college=# select * from student order by marks desc;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  1 | rahul  |  20 | bca    |    90
  2 | rohith |  20 | ece    |    90
  3 | satyam |  20 | cse    |    90
  4 | srija  |  19 | mech   |    90
(4 rows)


college=# update table student set marks=99 where id=2;
ERROR:  syntax error at or near "table"
LINE 1: update table student set marks=99 where id=2;
               ^
college=# update student set marks=99 where id=2;
UPDATE 1
college=# select * from student
college-# select * from student;
ERROR:  syntax error at or near "select"
LINE 2: select * from student;
        ^
college=# select * from student;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  1 | rahul  |  20 | bca    |    90
  3 | satyam |  20 | cse    |    90
  4 | srija  |  19 | mech   |    90
  2 | rohith |  20 | ece    |    99
(4 rows)


college=# update student set marks=99 where id=2,1;
ERROR:  syntax error at or near ","
LINE 1: update student set marks=99 where id=2,1;
                                              ^
college=# update student set marks=99 where id=2 and id=1;
UPDATE 0
college=# select * from student;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  1 | rahul  |  20 | bca    |    90
  3 | satyam |  20 | cse    |    90
  4 | srija  |  19 | mech   |    90
  2 | rohith |  20 | ece    |    99
(4 rows)


college=# update student set marks=99 where id in(2,1);
UPDATE 2
college=# select * from student;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  3 | satyam |  20 | cse    |    90
  4 | srija  |  19 | mech   |    90
  1 | rahul  |  20 | bca    |    99
  2 | rohith |  20 | ece    |    99
(4 rows)


college=# update student set marks=89 where id=1;
UPDATE 1
college=# select * from student;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  3 | satyam |  20 | cse    |    90
  4 | srija  |  19 | mech   |    90
  2 | rohith |  20 | ece    |    99
  1 | rahul  |  20 | bca    |    89
(4 rows)


college=# update student
college-# set marks = case
college-# when id = 1 then 89
college-# when id =2 then then 99
college-# when id = 3 then 80
college-# end
college-# where in (1,2,3);
ERROR:  syntax error at or near "then"
LINE 4: when id =2 then then 99
                        ^
college=# UPDATE student
college-# SET marks = CASE
college-#     WHEN id = 1 THEN 89
college-#     WHEN id = 2 THEN 99
college-#     WHEN id = 3 THEN 80
college-# END
college-# WHERE id IN (1, 2, 3);
UPDATE 3
college=# select * from student;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  4 | srija  |  19 | mech   |    90
  1 | rahul  |  20 | bca    |    89
  2 | rohith |  20 | ece    |    99
  3 | satyam |  20 | cse    |    80
(4 rows)


college=# update student set marks= marks+5;
UPDATE 4
college=# select * from student;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  4 | srija  |  19 | mech   |    95
  1 | rahul  |  20 | bca    |    94
  2 | rohith |  20 | ece    |   104
  3 | satyam |  20 | cse    |    85
(4 rows)


college=# select * from students
college-# limit=2;
ERROR:  syntax error at or near "="
LINE 2: limit=2;
             ^
college=# select * from students
college-# limit 2;
ERROR:  relation "students" does not exist
LINE 1: select * from students
                      ^
college=# select * from student
college-# limit 2;
 id | name  | age | course | marks
----+-------+-----+--------+-------
  4 | srija |  19 | mech   |    95
  1 | rahul |  20 | bca    |    94
(2 rows)


college=# select * students order by marks desc where limit 2;
ERROR:  syntax error at or near "students"
LINE 1: select * students order by marks desc where limit 2;
                 ^
college=# SELECT * FROM student
college-# ORDER BY marks DESC
college-# LIMIT 2;
 id |  name  | age | course | marks
----+--------+-----+--------+-------
  2 | rohith |  20 | ece    |   104
  4 | srija  |  19 | mech   |    95
(2 rows)


college=# select count(*) from student where course=bca;
ERROR:  column "bca" does not exist
LINE 1: select count(*) from student where course=bca;
                                                  ^
college=# select count(*) from student where course='bca';
 count
-------
     1
(1 row)


college=# select course,count(*)
college-# from student
college-# group by course;
 course | count
--------+-------
 cse    |     1
 bca    |     1
 ece    |     1
 mech   |     1
(4 rows)


college=# select min(marks) from student;
 min
-----
  85
(1 row)


college=# select max(marks) from student;
 max
-----
 104
(1 row)


college=# select avg(marks) from student;
         avg
---------------------
 94.5000000000000000
(1 row)


college=# create table student_card(
college(# card_id serial primary key,
college(# card_number varchar(50),
college(# id int unique reference student(id)
college(# );
ERROR:  syntax error at or near "reference"
LINE 4: id int unique reference student(id)
                      ^
college=# CREATE TABLE student_card (
college(#     card_id SERIAL PRIMARY KEY,
college(#     card_number VARCHAR(50),
college(#     id INT UNIQUE REFERENCES student(id)
college(# );
CREATE TABLE
college=# \d student_card;
                                        Table "public.student_card"
   Column    |         Type          | Collation | Nullable |                    Default
-------------+-----------------------+-----------+----------+-----------------------------------------------
 card_id     | integer               |           | not null | nextval('student_card_card_id_seq'::regclass)
 card_number | character varying(50) |           |          |
 id          | integer               |           |          |
Indexes:
    "student_card_pkey" PRIMARY KEY, btree (card_id)
    "student_card_id_key" UNIQUE CONSTRAINT, btree (id)
Foreign-key constraints:
    "student_card_id_fkey" FOREIGN KEY (id) REFERENCES student(id)


college=# insert into student_card(card_number,student_id)
college-# values
college-# ('cs122',01),
college-# ('cs134',02),
college-# ('cs115',03),
college-# ('cs149',04));
ERROR:  syntax error at or near ")"
LINE 6: ('cs149',04));
                    ^
college=# INSERT INTO student_card (card_number, id)
college-# VALUES
college-# ('cs122', 1),
college-# ('cs134', 2),
college-# ('cs115', 3),
college-# ('cs149', 4);
INSERT 0 4
college=# select * from student_card;
 card_id | card_number | id
---------+-------------+----
       1 | cs122       |  1
       2 | cs134       |  2
       3 | cs115       |  3
       4 | cs149       |  4
(4 rows)


college=# drop table student_card;
DROP TABLE
college=# \d student_card;
Did not find any relation named "student_card".
college=# create table departments(
college(# department_id serial primary key,
college(# department_name varchar(100));
CREATE TABLE
college=# \d departments;
                                              Table "public.departments"
     Column      |          Type          | Collation | Nullable |                      Default
-----------------+------------------------+-----------+----------+----------------------------------------------------
 department_id   | integer                |           | not null | nextval('departments_department_id_seq'::regclass)
 department_name | character varying(100) |           |          |
Indexes:
    "departments_pkey" PRIMARY KEY, btree (department_id)


college=# insert into departments(department_name)
college-# values
college-# ('cse'),
college-# ('mech'),
college-# ('aiml'),
college-# ('is');
INSERT 0 4
college=# select * from departments;
 department_id | department_name
---------------+-----------------
             1 | cse
             2 | mech
             3 | aiml
             4 | is
(4 rows)


college=# create table new(
college(# employee_id serial primary key,
college(# employee_name varchar(100),
college(# salary int,
college(# department_id init reference departments(department_id)
college(# );
ERROR:  syntax error at or near "reference"
LINE 5: department_id init reference departments(department_id)
                           ^
college=# CREATE TABLE employees (
college(#     employee_id SERIAL PRIMARY KEY,
college(#     employee_name VARCHAR(100),
college(#     salary INT,
college(#     department_id INT REFERENCES departments(department_id)
college(# );
CREATE TABLE
college=# \d employee;
Did not find any relation named "employee".
college=# \d employees;
                                            Table "public.employees"
    Column     |          Type          | Collation | Nullable |                    Default
---------------+------------------------+-----------+----------+------------------------------------------------
 employee_id   | integer                |           | not null | nextval('employees_employee_id_seq'::regclass)
 employee_name | character varying(100) |           |          |
 salary        | integer                |           |          |
 department_id | integer                |           |          |
Indexes:
    "employees_pkey" PRIMARY KEY, btree (employee_id)
Foreign-key constraints:
    "employees_department_id_fkey" FOREIGN KEY (department_id) REFERENCES departments(department_id)


college=# insert into employees(employee_name,salary,department_id)
college-# values
college-# ('rohith',100000,2),
college-# ('rahul',20000,2),
college-# ('satyam',100000,1),
college-# ('srija',50000,3);
INSERT 0 4
college=# select * from employees;
 employee_id | employee_name | salary | department_id
-------------+---------------+--------+---------------
           1 | rohith        | 100000 |             2
           2 | rahul         |  20000 |             2
           3 | satyam        | 100000 |             1
           4 | srija         |  50000 |             3
(4 rows)


college=# update employees set salary=95000 where employee_id=2;
UPDATE 1
college=# select * from employees;
 employee_id | employee_name | salary | department_id
-------------+---------------+--------+---------------
           1 | rohith        | 100000 |             2
           3 | satyam        | 100000 |             1
           4 | srija         |  50000 |             3
           2 | rahul         |  95000 |             2
(4 rows)


college=# update employees set salary=500000 where employee_id=2;
UPDATE 1
college=# select * from employees;
 employee_id | employee_name | salary | department_id
-------------+---------------+--------+---------------
           1 | rohith        | 100000 |             2
           3 | satyam        | 100000 |             1
           4 | srija         |  50000 |             3
           2 | rahul         | 500000 |             2
(4 rows)


college=# update employees set salary=95000 where employee_id=4;
UPDATE 1
college=# select * from employees;
 employee_id | employee_name | salary | department_id
-------------+---------------+--------+---------------
           1 | rohith        | 100000 |             2
           3 | satyam        | 100000 |             1
           2 | rahul         | 500000 |             2
           4 | srija         |  95000 |             3
(4 rows)


college=# update employees set salary=500000 where employee_id=4;
UPDATE 1
college=# select * from employees;
 employee_id | employee_name | salary | department_id
-------------+---------------+--------+---------------
           1 | rohith        | 100000 |             2
           3 | satyam        | 100000 |             1
           2 | rahul         | 500000 |             2
           4 | srija         | 500000 |             3
(4 rows)


college=#