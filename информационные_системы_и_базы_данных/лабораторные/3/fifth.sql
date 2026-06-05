SELECT "ГРУППА", avg(date_part('year', age("ДАТА_РОЖДЕНИЯ"))) AS "ВОЗРАСТ" FROM
    "Н_ЛЮДИ" INNER JOIN "Н_УЧЕНИКИ"
    ON "Н_ЛЮДИ"."ИД" = "Н_УЧЕНИКИ"."ЧЛВК_ИД"
GROUP BY "ГРУППА"
    HAVING avg(date_part('year', age("ДАТА_РОЖДЕНИЯ")))
    < (SELECT max(date_part('year', age("ДАТА_РОЖДЕНИЯ"))) AS "ВОЗРАСТ"
       FROM "Н_ЛЮДИ" INNER JOIN "Н_УЧЕНИКИ" ON "Н_ЛЮДИ"."ИД" = "Н_УЧЕНИКИ"."ЧЛВК_ИД"
       WHERE "ГРУППА" = '1100');