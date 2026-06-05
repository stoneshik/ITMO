-- Функция для генерации случайных байтовых значение типа bytea (нужно для имитации видеоконтента)
CREATE OR REPLACE FUNCTION random_bytea(bytea_length integer)
    RETURNS bytea AS $body$
SELECT
    decode(
        string_agg(
            lpad(
                to_hex(
                    width_bucket(random(), 0, 1, 256) - 1
                ),
                2,
                '0'
            ),
            ''
        ),
        'hex'
    )
FROM generate_series(1, $1);
$body$
    LANGUAGE 'sql'
    VOLATILE
    SET search_path = 'pg_catalog'
    ;


-- Добавление тестовых данных
INSERT INTO objects(obj_id, obj_name, obj_description, obj_color)
VALUES
    (0,
     'Плато',
     'Границы очерчены чрезвычайно резко. Оно совсем гладкое, ни щербинки не видно. Может быть, это даже жидкость - поверхность как будто плоская.',
     'Белый'),
    (1,
     'Река Нева',
     'Вытекает из Шлиссельбургской губы Ладожского озера, протекает по Приневской низине, впадает в Финский залив (Балтийское море). Её длина от истока до устья при впадении Большой Невы в Невскую губу у Невских ворот Санкт-Петербургского торгового порта — 74 км. Расстояние от истока до устья Невы по прямой — 45 км.',
     'Синий'),
    (2,
     'Апельсин',
     'Представляет собой круглый цитрусовый фрукт с оранжевой кожурой, иногда с красными прожилками. Мякоть у него кисловатая, светло-оранжевого или (у апельсинов-корольков) тёмно-красного цвета, разделённая на дольки. Бывают апельсины с косточками и без них.',
     'Оранжевый')
    ;

INSERT INTO users(user_id, user_name, user_surname)
VALUES
    (0, 'John', 'Smith'),
    (1, 'Иван', 'Иванов'),
    (2, 'Евгений', 'Кузнецов'),
    (3, 'Светлана', 'Зайцева')
    ;

INSERT INTO videograms(vid_id, user_id, vid_name, vid_date_of_creation, vid_content)
VALUES
    (0, 0, 'Первое видео плато', default, random_bytea(1000)),
    (1, 0, 'Второе видео плато', default, random_bytea(912)),
    (2, 0, 'Третье видео плато', default, random_bytea(450)),
    (3, 3, 'Видео Невы', default, random_bytea(400)),
    (4, 3, 'Видео апельсина', default, random_bytea(812))
    ;

INSERT INTO objects_in_videograms(obj_id, vid_id)
VALUES
    (0, 0),
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4)
    ;

INSERT INTO messages(
    msg_id,
    msg_sender_user_id,
    msg_recipient_user_id,
    msg_date_send,
    msg_text_header,
    msg_text_content
)
VALUES
    (0, 0, 1, default, 'Видеограммы белого плато', 'Привет! Я снял плато с которым не могу никак разобраться'),
    (1, 2, 3, default, 'Видеограмма Невы', 'Привет! Ты засняла прекрасный вид Невы на фоне вечернего неба'),
    (2, 3, 2, default, 'Видеограмма апельсина', 'Привет! Смотри какой апельсин я засняла')
    ;

INSERT INTO videograms_in_messages(vid_id, msg_id)
VALUES
    (0, 0),
    (1, 0),
    (3, 1),
    (4, 2)
    ;
