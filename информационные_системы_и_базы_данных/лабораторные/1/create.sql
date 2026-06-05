CREATE TABLE IF NOT EXISTS objects (
    obj_id SERIAL PRIMARY KEY,
    obj_name VARCHAR(100) NOT NULL,
    obj_description TEXT NOT NULL,
    obj_color VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    user_surname VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS videograms (
    vid_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    vid_name VARCHAR(100) NOT NULL,
    vid_date_of_creation TIMESTAMP NOT NULL DEFAULT current_timestamp,
    vid_content BYTEA NOT NULL
);

CREATE TABLE IF NOT EXISTS objects_in_videograms (
    obj_in_vid_id SERIAL PRIMARY KEY,
    obj_id INT NOT NULL REFERENCES objects(obj_id) ON DELETE CASCADE,
    vid_id INT NOT NULL REFERENCES videograms(vid_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS messages (
    msg_id SERIAL PRIMARY KEY,
    msg_sender_user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    msg_recipient_user_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
    msg_date_send TIMESTAMP NOT NULL DEFAULT current_timestamp,
    msg_text_header VARCHAR(200) NOT NULL,
    msg_text_content TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS videograms_in_messages (
    vid_in_msg_id SERIAL PRIMARY KEY,
    vid_id INT NOT NULL REFERENCES videograms(vid_id) ON DELETE CASCADE,
    msg_id INT NOT NULL REFERENCES messages(msg_id) ON DELETE CASCADE
);
