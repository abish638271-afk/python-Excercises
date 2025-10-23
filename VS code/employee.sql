use sample;

create table employee1(
emp_id int primary key,
emp_name varchar(20)not null,
emp_age int,
emp_dept varchar(20)
);

create table emp_salary(
emp_sal_id int,
emp_id int,
emp_salary int,
FOREIGN KEY (emp_id) REFERENCES employee1(emp_id)
);

insert into employee1 values (1,'suresh',39,'civil');
insert into employee1 values (2,'ramesh',30,'mech');
insert into employee1 values (3,'mani',37,'chem');
insert into employee1 values (4,'sanjai',39,'civil');

insert into emp_salary values (11,1,30000),(12,2,40000),(13,3,30000),(14,4,40000);

select * from emp_salary;



