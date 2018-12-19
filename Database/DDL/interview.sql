drop table interview;

create table interview(
	comp_id varchar(255),
	job_id int,
	interview_id int NOT NULL AUTO_INCREMENT,
	date date,
	question text,
	PRIMARY KEY (comp_id, job_id, interview_id)
) ENGINE=myisam, DEFAULT CHARSET=utf8;

--demo data--
begin;

delete from interview;

insert into interview (comp_id, job_id, date, question) values
	('SAP', 1, '2018-09-09', 'asked all basic data structure questions, also some class projects I\'ve done in school. Doubly linked-list, hashmap, SQL, primary key, foreign key etc.'),
	('SAP', 2, '2018-08-08', 'How will you build an API for Memory Cache? Choose whichever language you are comfortable with.'),
	('Amazon', 1, '2017-08-08', 'What is HashTable? How does it work in the backend perspective? What to do if the collision happened? Whats the time complexity of inserting? deleting? seaching? What\'s the time complexity for the worse case?'),
	('Amazon', 2, '2017-07-07', 'signed a nda ');

commit;