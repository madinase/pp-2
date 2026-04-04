CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook(name, phone) VALUES(p_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE delete_contact_proc(p_id INT DEFAULT NULL, p_name VARCHAR DEFAULT NULL, p_phone VARCHAR DEFAULT NULL)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_id IS NOT NULL THEN
        DELETE FROM phonebook WHERE id = p_id;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM phonebook WHERE phone = p_phone;
    ELSIF p_name IS NOT NULL THEN
        DELETE FROM phonebook WHERE name = p_name;
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1 .. array_upper(p_names, 1) LOOP
        IF p_phones[i] ~ '^[0-9+]+$' AND length(p_phones[i]) >= 5 THEN
            INSERT INTO phonebook(name, phone) VALUES(p_names[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'Некорректный номер для пользователя %: %', p_names[i], p_phones[i];
        END IF;
    END LOOP;
END;
$$;