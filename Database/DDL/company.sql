drop table company;

create table company(
	comp_id varchar(255),
	website varchar(255),
	size varchar(100),
	type varchar(255),
	revenue varchar(100),
	hq_country varchar(50),
	hq_province varchar(50),
	hq_city varchar(50),
	industry varchar(255),
	founded date,
	benefit_rating float,
	main_benefit text,
	description text,
	itv_experience varchar(255),
	itv_obtain_way varchar(255),
	itv_difficulty varchar(20),
	logo varchar(255),
	PRIMARY KEY (comp_id)
) DEFAULT CHARSET=utf8;


--demo data--
begin;

delete from company;

insert into company (comp_id, website, size, type, revenue, hq_country, hq_province, hq_city, industry) values
	('SAP', 'http://http//www.sap.com/careers', '10000+ employees', 'Company - Public (SAP)', '$10+ billion (CAD) per year', 'Germany', 'Baden-Württemberg', 'Walldorf', 'Computer Hardware & Software'),
	('Amazon', 'http://www.amazon.jobs/', '10000+ employees', 'Company - Public (AMZN)', '$10+ billion (CAD) per year', 'US', 'WA', 'Seattle', 'Internet');

commit;