# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS;"
user_table_drop = "DROP TABLE IF EXISTS USERS;"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXIST ARTISTS;"
time_table_drop = "DROP TABLE IF EXIST TIME;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE SONGPLAYS IF NOT EXISTS(
    songplay_id SERIAL PRIMARY KEY,
    start_time BIGINT,
    user_id int, 
    level varchar, 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location varchar, 
    user_agent varchar
);
""")

user_table_create = ("""CREATE TABLE USERS IF NOT EXISTS(
    user_id int PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar 
);
""")

song_table_create =  ("""CREATE TABLE SONGS IF NOT EXISTS(
    song_id varchar NOT NULL PRIMARY KEY,
    title varchar(255) NOT NULL,
    artist_id varchar(255) NOT NULL,
    year int,
    duration FLOAT
);
""")

artist_table_create = ("""CREATE TABLE ARTISTS IF NOT EXISTS(
    artist_id varchar(255) PRIMARY KEY,
    name varchar(255) NOT NULL,
    location varchar,
    latitude FLOAT,
    longitude FLOAT
)
""")

time_table_create = ("""CREATE TABLE TIME IF NOT EXISTS(
    start_time BIGINT PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
)

""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]