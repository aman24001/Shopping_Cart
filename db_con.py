import mysql.connector as db
def dbConn():
    conn = db.connect(
        host="localhost",
        user="root",
        password="",
        database="shopping_mall"
    )
    return conn 
