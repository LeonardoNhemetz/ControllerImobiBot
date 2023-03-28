# Importing the required libraries
import mysql.connector
import time

# Establishing the connection with the remote MySQL server
mydb = mysql.connector.connect(
  host="172.19.0.2",
  user="root",
  password="root",
  database="cad_imobiliarias"
)

# Creating a cursor object
mycursor = mydb.cursor()

# Executing a select statement on a specific table
start_time = time.time()
mycursor.execute("SELECT * FROM specific_table")
end_time = time.time()

# Fetching the results and printing the time taken to execute the query
result = mycursor.fetchall()
print("Time taken to execute the query:", end_time - start_time, "seconds")