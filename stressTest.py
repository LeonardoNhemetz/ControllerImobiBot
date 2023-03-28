import mysql.connector
import time

# Conectar ao banco de dados
mydb = mysql.connector.connect(
  host="172.19.0.1",
  user="root",
  password="root",
  database="cad_imobiliarias"
)

# Creating a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Defining the SQL query to be executed
sql = "SELECT * FROM cadastros"

# Running the SQL query for 1000 times
for i in range(1000):
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(result)
    time.sleep(0.1) # adding a delay of 0.1 seconds to simulate stress

# Closing the database connection
mydb.close()