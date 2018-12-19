DELIMITER $$

create FUNCTION getDictValue (bean_code varchar(50), dict_code varchar(50), lang_code varchar(8)) returns varchar(50)

begin

declare v_lang varchar(8);
declare v_out varchar(50);

	if lang_code is null then
		set v_lang = "en_us";
	else
		set v_lang = lang_code;
	end if;

	select dict_value into v_out 
	from sys_dict_data a 
	where a.bean_code = bean_code 
		and a.dict_code = dict_code 
		and a.lang_code = v_lang;

	return v_out;

end$$

DELIMITER ;