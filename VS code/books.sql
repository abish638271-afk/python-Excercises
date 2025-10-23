use sample;

create table books(
id int primary KEY,
title varchar(50),
author varchar(40),
publication_year int ,
genrec varchar(30),
price float,
stock int
);

insert into books values(1,'to kill a mockingbird','harber lee',1960,'fiction',12.99,10);
insert into books values(2,'1984','george orwell',1949,'science fiction',10.99,15);
insert into books values (3,'pride and prejudice','jane austen',1813,'romance',9.99,5);
insert into books values (4,'the hobbit','j.r.r tolkien',1937,'fantacy',14.99,20);
insert into books values(5,'The Catcher in the Rye','J.D.Salinger',1951,'fiction',11.99,8);

select* from books;
select sum(price * stock) as  total_inventory from books;   

select genrec,count(*)as count from books group by genrec;    

select title from books 
where publication_year <1950;     

select title,author,genrec,price from books
where genrec ='fiction'or (price<12.99);

select title,stock as days from books
where stock> 10 ;
