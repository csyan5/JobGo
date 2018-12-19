drop table company_review;

create table company_review(
	comp_id varchar(255),
	review_id int NOT NULL AUTO_INCREMENT,
	reviewer_title varchar(255),
	score varchar(100),
	pros text,
	cons text,
	PRIMARY KEY (comp_id, review_id)
) ENGINE=myisam, DEFAULT CHARSET=utf8;
--alter table company_review engine=innodb;

--demo data--
begin;

delete from company_review;

insert into company_review (comp_id, reviewer_title, score, pros, cons) values
	('SAP', 'Current Employee - Software Developer', '3|5|4|5|2', 'WORK LIFE BALANCE AND FLEXIBILITY', 'Work life balance could be better'),
	('SAP', 'Current Employee - Software Developer', '3|5|4|5|2', 'Great flexibility to work from home', 'There are literally no cons I can think of to working at SAP'),
	('SAP', 'Current Employee - Software Developer', '3|5|4|5|2', 'SAP is a wonderful organization to work for because it works with Fortune 500 clients whereby we are always ahead technology and best practices. Companies like Nike, Porsche, Mercedes. Apple are a few of our clients and other partners.Aside from the benefits, discounted purchase options and remarkable engagement groups, the talent is amazing and you will work with many competent people.We have yoga and meditation classes, mindfulness workshops. Many invited guests from technology industries to provides you with information.Leadership women work shops, global coaching, mentoring programs and flexible work environment.It is truly a top notch company that will give back to their employees.No company is perfect but this is prefect for me', 'You are responsible for your career progression, so make it work.'),
	('Amazon', 'Current Employee - Software Developer', '3|5|4|5|2', 'Working towards a better work-life balance', 'Work/life balance seems comparable to other places I\'ve worked - not worse'),
	('Amazon', 'Current Employee - Software Developer', '3|5|4|5|2', 'Get to learn a lot in a short duration', 'I have no work life balance issues'),
	('Amazon', 'Current Employee - Software Developer', '3|5|4|5|2', 'Wonderful work culture for fresher', 'I don\'t see any cons');
commit;
