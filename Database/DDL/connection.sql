drop table connection;

create table connection(
	person_id int NOT NULL AUTO_INCREMENT,
	name varchar(255),
	comp_id varchar(255),
	title varchar(255),
	country varchar(50),
	province varchar(50),
	city varchar(50),
	link varchar(255),
	PRIMARY KEY (person_id)
) DEFAULT CHARSET=utf8;

--demo data--
begin;

delete from connection;

insert into connection (name, comp_id, title, country, province, city, link) values
	('Hye Lim Moon', 'SAP', 'SAP Agile Developer Intern', 'CA', 'BC', 'Vancouver', 'https://www.linkedin.com/in/hyelim/'),
	('Kevin Poskitt', 'SAP', 'Product Manager', 'CA', 'BC', 'Vancouver', 'https://www.linkedin.com/in/kevin-poskitt-7976447/'),
	('Frank Sun ', 'Amazon', 'Software Development Manager', 'CA', 'BC', 'Vancouver', 'https://www.linkedin.com/in/frank-sun-a6b7411/'),
	('Jack Zhang', 'Amazon', 'Software Development Manager', 'CA', 'BC', 'Vancouver', 'https://www.linkedin.com/in/jackzhang/');
commit;