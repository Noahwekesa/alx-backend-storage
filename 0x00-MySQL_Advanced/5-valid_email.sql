-- creates a trigger that resets the attr valid_email

CREATE TRIGGER new_email BEFORE
UPDATE ON users
FOR EACH ROW
BEGIN
IF OLD.email != NEW.email THEN
SET NEW.valid_email = 0;
END IF;
END;
