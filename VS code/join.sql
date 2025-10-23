use sample;

create table employee2(
emp_id int primary key,
emp_name varchar(20)not null,
dept_id int 
);

create table dept1(
dept_id int primary key,
dept_name varchar(20)
);

insert into employee2 values (1,'suresh',1011),(2,'sanjai',1012),(3,'raj',1013);

insert into dept1 values(1011,'civil'),(1012,'mech'),(1013,'it');


select emp_id,emp_name,dept_name
from employee2
inner join dept1
on employee2.dept_id=dept1.dept_id;