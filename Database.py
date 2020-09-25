import mysql.connector
from mysql.connector import connect, errorcode, Error
def ConnectMySql():
 try:
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="sandhyavisa",
            database="chatbot"
        )

    return mydb
 except Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Check user id and password")
            return False
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
            return False
        else:
            print(err)
            return False


