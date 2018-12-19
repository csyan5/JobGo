drop table connection_background;

create table connection_background(
	person_id int,
	bg_id int NOT NULL AUTO_INCREMENT,
	bg_type varchar(2) default '0', -- 0-education, 1-Work Experience
	bg_name varchar(255),
	start_date date,
	end_date date,
	description text,
	PRIMARY KEY (person_id, bg_id)
) ENGINE=myisam, DEFAULT CHARSET=utf8;

--demo data--  set sql_mode='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION'
begin;

delete from connection_background;

insert into connection_background (person_id, bg_name, start_date, end_date, description) values
	(1, 'Simon Fraser University', STR_TO_DATE('2017', '%Y'), STR_TO_DATE('2018', '%Y'), 'Master of Science - MSc, Big Data'),
	(1, 'Simon Fraser University', STR_TO_DATE('2013', '%Y'), STR_TO_DATE('2017', '%Y'), 'Bachelor of Science, Software System'),
	(2, 'The University of British Columbia', STR_TO_DATE('2009', '%Y'), STR_TO_DATE('2011', '%Y'), 'Diploma, Accounting'),
	(2, 'University of Toronto - New College', STR_TO_DATE('2002', '%Y'), STR_TO_DATE('2007', '%Y'), 'IBM Internship Varsity Water Polo (OUA Gold Medal 2002) New College Alumni'),
	(3, 'Zhejiang University', '', '', 'Master of Science (M.S.) Electrical and Electronics Engineering'),
	(4, 'Tsinghua University', STR_TO_DATE('1991', '%Y'), STR_TO_DATE('1993', '%Y'), 'Master, Engineering'),
	(4, 'Tsinghua University', STR_TO_DATE('1986', '%Y'), STR_TO_DATE('1991', '%Y'), 'Bachelor, Engineering');
commit;