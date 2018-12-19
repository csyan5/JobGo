drop table job;

create table job(
	comp_id varchar(255),
	job_id int NOT NULL AUTO_INCREMENT,
	title varchar(255),
	country varchar(255),
	province varchar(255),
	city varchar(255),
	avg_salary varchar(100),
	low_salary varchar(100),
	high_salary varchar(100),
	fulltime varchar(2) default '0',  -- 0-fulltime, 1-parttime
	type varchar(255),
	industry varchar(255),
	description text,
	apply_link varchar(255), 
	PRIMARY KEY (comp_id, job_id)
) ENGINE=myisam, DEFAULT CHARSET=utf8;

--demo data--
begin;

delete from job;

insert into job (comp_id, title, country, province, city, avg_salary, low_salary, high_salary, type, industry) values
	('SAP', 'Software Developer', 'CA', 'BC', 'Vancouver', 'CA$79,000/yr', 'CA$60K', 'CA$95K', 'SDE', 'IT'),
	('SAP', 'Software Engineer', 'CA', 'BC', 'Vancouver', 'CA$80,000/yr', 'CA$68K', 'CA$90K', 'SDE', 'IT'),
	('Amazon', 'Software Development Engineer', 'CA', 'BC', 'Vancouver', 'CA$103,500/yr', 'CA$80K', 'CA$140K', 'SDE', 'IT'),
	('Amazon', 'Software Development Engineer II', 'CA', 'BC', 'Vancouver', 'CA$114,000/yr', 'CA$92K', 'CA$132K', 'SDE', 'IT');

commit;