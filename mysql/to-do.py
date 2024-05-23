import mysql.connector
import bcrypt

my_host = "localhost"
my_database = "useless"
my_user = "root"
my_password = "UP@,./456"

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host=my_host,
            database=my_database,
            user=my_user,
            password=my_password
        )
        return connection, connection.cursor()
    except mysql.connector.Error as err:
        print("Error connecting to MySQL:", err)
        return None, None

def create_todo_table(cursor):
    try:
        cursor.execute("CREATE TABLE IF NOT EXISTS todo (User_Name varchar(255), U_Age int, Password varchar(255))")
    except mysql.connector.Error as err:
        print("Error creating todo table:", err)

def save_todo_list(user_name):
    file_name = f"{user_name}.txt"
    try:
        with open(file_name, "w") as f:
            while True:
                todo_item = input("Enter what you want to do (press Enter to stop): ")
                if not todo_item:
                    break
                f.write(todo_item + "\n")
        print("To-do list saved successfully!")
    except Exception as e:
        print("Error saving to-do list:", e)

def view_todo_list(user_name):
    file_name = f"{user_name}.txt"
    try:
        with open(file_name, "r") as f: 
            print("Your to-do list:")
            print(f.read())
    except FileNotFoundError:
        print("File does not exist.")
    except Exception as e:
        print("Error viewing to-do list:", e)

def start(cursor):
    print("Enter what you want to-do:")
    print("1. Existing User ")
    print("2. New user")
    user = input("Enter the User Type: ")

    if user == '1':
        user_name = input("Enter the UserName: ")
        password = input("Enter the password: ")

        
        def verify_password(password, hashed_password):
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

        cursor.execute("SELECT Password FROM todo WHERE User_Name = %s ", (user_name,))
        result = cursor.fetchone()
   
        if result:
            hashed_password = result[0].encode('utf-8')  # Unpack the tuple and get the hashed password
            if verify_password(password, hashed_password):
                print("User authenticated!")
                print("*************************")
                print("\t1. Want to Create to-do")
                print("\t2. Want to see Already created to-do:")
                print()
                n = input("\tEnter: ")
                if n == '1':
                    save_todo_list(user_name)
                elif n == '2':
                    view_todo_list(user_name)
                else:
                    print("Incorrect input. Try Again or File doesn't exist.")
        else:
            print("User not found or password incorrect.")
        
    elif user == '2':
        user_name = input("Enter the username: ")
        age = int(input("Enter the age: "))
        password = input("Enter the password: ")
        re_type = input("Enter the password again: ")
        if password == re_type:
            # Hash the password before inserting it into the database
            hashed_password = hash_password(password)
            cursor.execute("INSERT INTO todo VALUES (%s, %s, %s)", (user_name, age, hashed_password))
            connection.commit()
            print("User created successfully!")
            print("*************************")
            print()
            print("1. Want to Create to-do")
            n = input("\tEnter: ")
            if n == '1':
                save_todo_list(user_name)
            else:
                print("Incorrect input. Try Again")
        else:
            print("Passwords do not match.")
    else:
        print("Invalid input. Please enter 1 or 2.")

if __name__ == "__main__":
    connection, cursor = connect_to_database()
    if connection and cursor:
        create_todo_table(cursor)
        try:
            start(cursor)
        except Exception as e:
            print("An error occurred during execution:", e)
        finally:
            cursor.close()
            connection.close()
            print("Connection closed")
        
        while True:
            choice = input("\nDo you want to continue? (yes/no): ").lower()
            if choice == 'yes':
                print("/n")
                try:
                    connection, cursor = connect_to_database()
                    if connection and cursor:
                        start(cursor)
                    else:
                        print("Program terminated due to database connection error.")
                except Exception as e:
                    print("An error occurred during execution:", e)
            elif choice=='no':
                break
            elif choice != 'yes':
                print("Invalid choice. Please enter 'yes' or 'no'.")
    else:
        print("Program terminated due to database connection error.")
