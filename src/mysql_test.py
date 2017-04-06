import mysql.connector

cnx = mysql.connector.connect(user="sql11166605", password="FctpTVkSmB",
                              host="sql11.freemysqlhosting.net",
                              database="sql11166605", port="3306")
cursor = cnx.cursor()

cursor.execute("insert into CATEGORY (name, min_age, max_age) values (\"asdf\", \"1\", \"1\")")
query = "SELECT CATEGORY_ID, NAME, MIN_AGE, MAX_AGE FROM CATEGORY"

cursor.execute(query)

for (id, name, min, max) in cursor:
    print("hello",id, name, min, max)

cnx.close()