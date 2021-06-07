# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS;"
user_table_drop = "DROP TABLE IF EXISTS USERS;"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXIST ARTISTS;"
time_table_drop = "DROP TABLE IF EXIST TIME;"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE SONGPLAYS IF NOT EXISTS(
    songplay_id int,
    start_time BIGINT,
    user_id int, 
    level varchar, 
    song_id int, 
    artist_id int, 
    session_id int, 
    location varchar, 
    user_agent varchar
)
""")

user_table_create = ("""CREATE TABLE USERS IF NOT EXISTS(
    user_id int,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar 
)
""")

song_table_create = ("""
""")

artist_table_create = ("""CREATE TABLE SONGS IF NOT EXISTS(
    song_id int,
    title varchar,
    artist_id int,
    year int,
    duration FLOAT
)
""")

time_table_create = ("""CREATE TABLE TIME IF NOT EXISTS(
    start_time int,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday varchar
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