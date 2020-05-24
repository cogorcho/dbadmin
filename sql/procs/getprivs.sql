DELIMITER //

DROP PROCEDURE IF EXISTS GETPRIVS;

CREATE PROCEDURE GETPRIVS(IN username VARCHAR(128))
BEGIN
    select 
        privilege_type, 
        is_grantable  
    from information_schema.user_privileges
    where grantee = username;
END;

//

DELIMITER ;