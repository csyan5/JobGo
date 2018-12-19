drop table salary;

create table salary(
	comp_id varchar(255),
	salary_id int NOT NULL AUTO_INCREMENT,
	job_title varchar(255),
	avg_salary float,
	low_salary float,
	high_salary float,
	currency varchar(50),
	job_type varchar(255),
	country varchar(50),
	province varchar(50),
	city varchar(50),
	PRIMARY KEY (comp_id, salary_id)
) ENGINE=myisam, DEFAULT CHARSET=utf8;

begin;

delete from salary;

insert into salary (comp_id, job_title, country, province, city, avg_salary, low_salary, high_salary, currency, job_type) values
	('SAP', 'Software Developer', 'CA', 'BC', 'Vancouver', '79000', '60000', '95000', 'CAD', 'Software Development'),
	('SAP', 'Software Engineer', 'CA', 'BC', 'Vancouver', '80000', '68000', '90000', 'CAD', 'Software Development'),
	('SAP', 'Software Engineer', 'CA', 'BC', 'Vancouver', '85000', '70000', '98000', 'CAD', 'Software Development'),
	('Amazon', 'Software Development Engineer', 'CA', 'BC', 'Vancouver', '103500', '80000', '140000', 'CAD', 'Software Development'),
	('Amazon', 'Software Development Engineer II', 'CA', 'BC', 'Vancouver', '114000', '92000', '132000', 'CAD', 'Software Development'),
	('Amazon', 'Software Development Engineer III', 'CA', 'BC', 'Vancouver', '100000', '85000', '140000', 'CAD', 'Software Development'),
	('Amazon', 'Software Development Engineer IV', 'CA', 'BC', 'Vancouver', '130000', '92000', '132000', 'CAD', 'Software Development'),
	('Amazon', 'Software Development Engineer V', 'CA', 'BC', 'Vancouver', '90000', '80000', '140000', 'CAD', 'Software Development'),
	('Amazon', 'Software Development Engineer VI', 'CA', 'BC', 'Vancouver', '150000', '92000', '200000', 'CAD', 'Software Development');
commit;