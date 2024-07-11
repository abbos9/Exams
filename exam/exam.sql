CREATE TABLE Employees(
    first_name varchar(20),
    last_name varchar(20),
    email varchar(30),
    phone_num DATE,
    hire_date DATE,
    job_id varchar(20),
    salary INT,
    commision_pct INT,
    manager_id INT,
    departament_id INT
);

INSERT INTO Employees(?,?,?,?,?,?,?,?,?,?) VALUES('SANJAR','IBN RAVSHANOV','sanjaribnravshamov@gmail.com',
'+998974585543','20-11-2004','sj2005',50000,2000,'is2000',20);

SELECT * FROM Employees;
SELECT * FROM Employees WHERE name='Дэвид';
SELECT * FROM Employees WHERE job_id='IT_PROG';
SELECT *  FROM Employees WHERE departament_id=50 AND salary >=4000 ;
SELECT * FROM Employees WHERE departament_id=20 AND departament_id=30;
SELECT * FROM Employees WHERE last_name LIKE '%a';
SELECT * FROM Employees WHERE departament_id=50 AND departament_id=80 AND commision_pct IS NOT NULL;
SELECT salary FROM Employees WHERE salary LIMIT 9000 OFFSET 7999;
SELECT * FROM Employees WHERE first_name LIKE '%qwerty%';
SELECT manager_id  FROM Employees;
