from mysql import connector

mydb = connector.connect(
    host="localhost",
    user="chris",
    passwd="65536"
)

print(mydb)
