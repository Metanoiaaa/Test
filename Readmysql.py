print("read my sql")

import mysql.connector as my

#host(adres)
#database
#username
#password

dbConnection = my.connect(
    host='localhost',
    user= 'root',
    password='',
    database='temp',
)

myCursor = dbConnection.cursor();
myCursor.execute('SELECT * FROM auto')

alleregels=myCursor.fetchall();

print(alleregels)

for rij in alleregels:
    print("Gevonden sport is: " + rij[1])
