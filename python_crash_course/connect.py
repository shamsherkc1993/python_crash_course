import mysql.connector as mysql
import json
import os

mydb = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="ERP_SYSTEM"
)

dbcursor = mydb.cursor()

path = "/Users/shamsher/Desktop/Project/python_crash_course/SQLQUERIES/departments.sql"

with open(path, 'r') as file:
    sql_query = file.read()

dbcursor.execute(sql_query)

# fetch data
rows = dbcursor.fetchall()
columns = [col[0] for col in dbcursor.description]

# convert to JSON-ready format
data = [dict(zip(columns, row)) for row in rows]

# create DATAS folder
os.makedirs("/Users/shamsher/Desktop/Project/python_crash_course/DATAS", exist_ok=True)

# table name from sql file
table_name = os.path.splitext(os.path.basename(path))[0]

# save json
json_path = f"/Users/shamsher/Desktop/Project/python_crash_course/DATAS/{table_name}.json"
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(f"✅ JSON file created: {json_path}")