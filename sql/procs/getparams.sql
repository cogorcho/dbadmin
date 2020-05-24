CREATE PROCEDURE GETPARAMS(procname VARCHAR(64), pschema VARCHAR(64))
BEGIN
    select 
        ordinal_position, 
        parameter_name, 
        parameter_mode,
        upper(data_type), 
        ifnull(character_maximum_length,0) as vclen
    from information_schema.parameters 
    where specific_name = procname COLLATE utf8_unicode_ci 
      and specific_schema = pschema COLLATE utf8_unicode_ci 
    order by ordinal_position;
END;
