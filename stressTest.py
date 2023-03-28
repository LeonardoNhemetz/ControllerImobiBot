# import the required libraries
import mysql.connector
import time

# define the MySQL connection settings
mydb = mysql.connector.connect(
  host="192.168.1.199",
  user="root",
  password="root",
  database="cad_imobiliarias"
)

# define the query to be executed
query = "SELECT * FROM cadastros"

# define the number of times to execute the query
num_iterations = 100

# execute the query for the given number of times
start_time = time.time() # start timer
for i in range(num_iterations):
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)
end_time = time.time() # end timer

# calculate and print the time taken to execute the querie
print("Time taken to execute the query " + str(num_iterations) + " times: " + str(end_time - start_time) + " seconds")
