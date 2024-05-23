import mysql.connector

my_host = "localhost"
my_database = "vaibhav"
my_user = "root"
my_password = "UP@,./456"

try:
  connection = mysql.connector.connect(
      host=my_host,
      database=my_database,
      user=my_user,
      password=my_password
  )

  cursor = connection.cursor()
 
  cursor.execute("SELECT Name,Address FROM vaib WHERE Maritial_Status=\"Single\"") 

  result = cursor.fetchall()

  for row in result:
      print(row)

  
  cursor.execute("SHOW TABLES")
  result1=cursor.fetchall()

  for row in result1:
    print(row)

except mysql.connector.Error as err:
  print("Error connecting to MySQL:", err)

finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("Connection closed")
