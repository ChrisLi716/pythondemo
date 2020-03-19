from openpyxl import Workbook
from mysql import connector

wb = Workbook()

#https://www.cnblogs.com/programmer-tlh/p/10461353.html

sheet = wb.create_sheet("Mysheet", 0)

mydb = connector.connect(
    host="192.168.64.128",
    user="root",
    passwd="65536",
    database="mysql"
)

# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#     print(x)

header = ["id", "username", "buy_name", "buy_mobile"]

datas = []
datas.append(header)

mycursor = mydb.cursor()
mycursor.execute("select * from t_dg_buy_user")
all_data = mycursor.fetchall()
fileds = [field[0] for field in mycursor.description]

sheet.append(fileds)

# 从第一行开始写
for data in all_data:
    sheet.append(data)

wb.save("balances.xlsx")
