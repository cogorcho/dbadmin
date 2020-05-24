DELIMITER //

DROP PROCEDURE IF EXISTS GETUSERS;

CREATE PROCEDURE GETUSERS()
BEGIN
    select distinct grantee as USERNAME
    from information_schema.user_privileges
    order by 1;
END;

//

DELIMITER ;