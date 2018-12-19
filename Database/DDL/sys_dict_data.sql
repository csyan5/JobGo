drop table sys_dict_data;

create table sys_dict_data(
	bean_code varchar(50) ,
	dict_code varchar(50) ,
	lang_code varchar(8) default 'en_us',
	dict_value varchar(50) not null,
	bean_desc varchar(200),
	dict_desc varchar(200),
	PRIMARY KEY (bean_code, dict_code, lang_code)
) DEFAULT CHARSET=utf8;

begin;

delete from sys_dict_data;

insert into sys_dict_data (bean_code, dict_code, dict_value) values
	('YesOrNo', '0', 'No'),
	('YesOrNo', '1', 'Yes');

commit;