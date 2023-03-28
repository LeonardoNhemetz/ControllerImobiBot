# import the required libraries
import pymysql
import time

# define the MySQL connection settings
mydb = pymysql.connect(
  host="category-app-mysql",
  user="root",
  password="root",
  database="cad_imobiliarias",
  port=81,  # port number for the MySQL server
  autocommit=True
)

# define the query to be executed
query = "SELECT * FROM yourtable"

# define the number of times to execute the query
num_iterations = 100

# execute the query for the given number of times
start_time = time.time() # start timer
for i in range(num_iterations):
    with mydb.cursor() as cursor:
        cursor.execute(query)
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
end_time = time.time() # end timer

# calculate and print the time taken to execute the queries
print("Time taken to execute the query " + str(num_iterations) + " times: " + str(end_time - start_time) + " seconds")
