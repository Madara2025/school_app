import mysql.connector
from dotenv import load_dotenv
import os # os is python module for iteraction

query = "ALTER TABLE user ADD email VARCHAR(20);"
load_dotenv()
try:
    connection = mysql.connector.connect(host=os.getenv('host'),
                                         database=os.getenv('mysql_database'),
                                           user=os.getenv('mysql_user'),
                                             password=os.getenv('mysql_password')
                                        )
    cursor = connection.cursor()
    cursor.execute(query)

    print("succsess")
except:
    print("Somthing went wrong")

finally:
    if connection.is_connected():
        connection.close()