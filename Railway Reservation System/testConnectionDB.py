import mysql.connector

connect_args={
    "host": "127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"root",
    "database":"test",
}

db = mysql.connector.connect(**connect_args)
cursor = db.cursor

sql = "Show Tables"
cursor.execute(sql)
print(cursor.fetchone())

cursor.close()
db.close()
