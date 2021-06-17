<h1>Introduction</h1>

Sparkify, a startup, wants to analyze the data they've gathered on songs and user activity on their new music streaming app. The analytics team is particularly interested in learning about the songs that users are listening to. They currently lack an easy way to query their data, which is stored in a directory of JSON logs on user activity on the app,
in addition to a directory containing JSON metadata on the songs in their app.

They would like to build a Postgres database with tables optimized for song play analysis queries. To conduct our analysis, several steps must be completed, including the creation of a database schema and an ETL pipeline. The database and ETL pipeline will be validated against the expected results by running SQL queries provided by Sparkify's analytics team.

As the Data Engineer assigned to this project, I will define fact and dimension tables for a star schema for a specific analytic focus, as well as write an ETL pipeline that uses Python and SQL to transfer data from files in two local directories into these tables in Postgres.


Database star schema

![Alt text](img/star-schema.jpg?raw=true "star schema")


<h1>Files in repository</h1>

1) test.ipynb displays the first few rows of each table to let you check your database.
2) create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3) etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4) etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5) sql_queries.py contains all your sql queries, and is imported into the last three files above.
6) Data folder contains your data which resides in JSON log files. 



*** To run the above files you can use MS Visual Studio and Jupyter Notebook ***

*** For this Project we will host our postgres server on a Docker container, below are instructions on how to run the complete project**


To run the project locally follow the steps below:

<h3>Step 1:</h3>

Run a postgres instance on Docker

a) Docker pull postgres:latest

b) Docker run --name randydb-postgres -e POSTGRES_PASSWORD=datapassword -d -p 5432:5432 postgres

c) Docker exec -it randydb-postgres bash

d) psql -U postgres

e) create Database student_randy

The database is now ready to be queried.


Step 2:

Create all the tables before inserting data (this will check if the tables already existed, delete, and re-create them)

a) Run create_tables.py

Step 3: 

Run the Extract, Transform and Load process

a) Run etl.py


Lastly open up test.ipynb in Jupyter Notebook to test our analytical queries! 
