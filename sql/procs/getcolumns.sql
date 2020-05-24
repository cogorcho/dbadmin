
DELIMITER //

DROP PROCEDURE IF EXISTS GETCOLUMNS;

CREATE PROCEDURE GETCOLUMNS(IN schemaname VARCHAR(64), IN tabname VARCHAR(64))
BEGIN
    select 
        column_name, 
        upper(data_type) as data_type, 
        ifnull(character_maximum_length,0) as vclen,
        is_nullable,
        character_octet_length as octet_length,
        character_set_name,
        collation_name 
    from information_schema.columns 
    where table_name = tabname 
      and table_schema = schemaname
    order by ordinal_position;
END;

//
DELIMITER ;