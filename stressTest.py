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

# Configurando o cursor do MySQL
mycursor = mydb.cursor()

# Definindo a consulta SQL a ser executada
query = "SELECT * FROM cadastros"

# Configurando o número de iterações
iterations = 1000

# Iniciando o cronômetro
start_time = time.time()

# Executando a consulta SQL em um loop
for i in range(iterations):
    mycursor.execute(query)
    result = mycursor.fetchall()

# Parando o cronômetro
stop_time = time.time()

# Calculando o número de consultas por segundo
queries_per_second = iterations / (stop_time - start_time)

# Imprimindo o número de consultas por segundo
print("Número de consultas por segundo:", queries_per_second)