DO LANGUAGE plpgsql
$$
DECLARE
    tle_scheme constant information_schema.tables.table_schema%TYPE = 's335159';
    tle_name information_schema.tables.table_name%TYPE;
    col_name information_schema.columns.column_name%TYPE;
    new_col_name information_schema.columns.column_name%TYPE;
    count_column_renaming int := 0;
    old_count_column_renaming int := 0;
    count_table_renaming int := 0;
BEGIN
    FOR tle_name IN SELECT table_name FROM information_schema.tables WHERE table_schema = tle_scheme
    LOOP
        old_count_column_renaming := count_column_renaming;
        FOR col_name IN
            SELECT column_name FROM information_schema.columns
                WHERE table_schema = tle_scheme AND table_name = tle_name AND column_name SIMILAR TO '%[''"]%'
        LOOP
            new_col_name := replace(col_name, '''', '');
            new_col_name := replace(new_col_name, '"', '');
            EXECUTE 'ALTER TABLE '
                        || quote_ident(tle_name)
                        || ' RENAME COLUMN '
                        || quote_ident(col_name)
                        || ' TO '
                        || quote_ident(new_col_name);
            count_column_renaming := count_column_renaming + 1;
        END LOOP;
        IF count_column_renaming > old_count_column_renaming THEN
            count_table_renaming := count_table_renaming + 1;
        END IF;
    END LOOP;
    RAISE INFO 'Схема: %', tle_scheme;
    RAISE INFO 'Столбцов переименовано: %', count_column_renaming;
    RAISE INFO 'Таблиц изменено: %', count_table_renaming;
END
$$