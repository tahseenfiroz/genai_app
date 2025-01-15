import os
import psycopg2

api_key = os.environ["API_KEY"]
#
pgv_connection = psycopg2.connect(
    dbname=os.environ["DB_NAME"],
    user=os.environ["USER"],
    password=os.environ["PASSWORD"],
    host=os.environ["HOST"],
    port=os.environ["PORT"]
)

