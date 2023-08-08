import pandas as pd
import pipline
import psycopg2
import sqlalchemy as sa
from dotenv import load_dotenv
from os import getenv
load_dotenv()
df = pipline.csv_reader.interpret(r'C:\Users\User\Documents\Bonfire\Homework\sql_d1\titanic (1).csv')

__user = getenv("USER")
__password = getenv("PASSWORD")
__server = getenv("SERVER")

db_params = {
    "user": __user,
    "password": __password,
    "host": __server,
    "port": "5432",
    "database": "xcqkhuuk"
}

engine = sa.create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

df.to_sql('titanic', engine, index=False, if_exists='replace')
engine.dispose()
