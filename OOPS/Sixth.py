import mysql.connector
import bcrypt

my_host = "localhost"
my_database = "VtBank"
my_user = "root"
my_password = "UP@,./456"


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


def create_table(cursor):
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Auth (
                User_Name VARCHAR(255), 
                Passwrd VARCHAR(255),
                Balance INT DEFAULT 2000,
                Acc_No VARCHAR(255) PRIMARY KEY
            )
        """)
        print("Table created successfully or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")


class Bank:
    def __init__(self, accountNo: str, connection, cursor) -> None:
        self.accountNo = accountNo
        self.balance = 2000
        self.connection = connection
        self.cursor = cursor

    class Transact:
        def __init__(self, amount, transaction_type):
            self.amount = amount
            self.type = transaction_type.lower()

        def process(self, account):
            if self.type == "withdraw":
                if account.balance >= self.amount:
                    account.balance -= self.amount
                else:
                    print("Insufficient Funds in the Account! ")
                    return
            elif self.type == "deposit":
                account.balance += self.amount
            else:
                print("Invalid Transaction Type")
                return

            try:
                account.cursor.execute("UPDATE Auth SET Balance = %s WHERE Acc_No = %s", (account.balance, account.accountNo))
                account.connection.commit()
                print(f"Transaction successful.")
            except mysql.connector.Error as err:
                print(f"Error updating balance: {err}")

    def make_transaction(self, amount, transaction_type):
        transaction = self.Transact(amount, transaction_type)
        transaction.process(self)
        print(f"Balance: $ {self.balance}")

    def authentication(self):
        print("Authentication")
        print("1. New user")
        print("2. Existing User")

        ch = input("Enter the choice: ")

        def hash_password(password):
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            return hashed_password

        if ch == "1":
            usr = input("Enter the Username: ")
            print("Password must be at least 8 characters")
            passwrd = input("Enter Password: ")
            re_type = input("Retype the Password: ")
            if passwrd == re_type:
                hashed_passwrd = hash_password(re_type)
                acc_no = input("Enter Account Number: ")
                try:
                    self.cursor.execute("INSERT INTO Auth (User_Name, Passwrd, Acc_No) VALUES (%s, %s, %s)", (usr, hashed_passwrd, acc_no))
                    self.connection.commit()
                    print("Successfully registered!")
                    self.accountNo = acc_no
                    self.balance = 2000
                    return True
                except mysql.connector.Error as err:
                    print(f"Error: {err}")

        elif ch == "2":
            usr = input("Username: ")
            passwrd = input("Password: ")

            def verify_password(password, hashed_password):
                return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

            try:
                self.cursor.execute("SELECT Passwrd, Acc_No, Balance FROM Auth WHERE User_Name = %s", (usr,))
                result = self.cursor.fetchone()

                if result:
                    hashed_password, acc_no, balance = result
                    hashed_password = hashed_password.encode('utf-8')
                    if verify_password(passwrd, hashed_password):
                        print("User authenticated!")
                        self.accountNo = acc_no
                        self.balance = balance
                        return True
                    else:
                        print("Authentication failed.")
                else:
                    print("User not found.")
            except mysql.connector.Error as err:
                print(f"Error: {err}")

        else:
            print("Invalid choice")

        return False


connection, cursor = connect_to_database()
if connection and cursor:
    create_table(cursor)
    bank = Bank("", connection, cursor)
    if bank.authentication():
        while True:
            transaction_type = input("Enter the Transaction Type [Withdraw, Deposit, quit]: ")
            if transaction_type.lower() == "quit":
                break
            elif transaction_type.lower() in ["withdraw", "deposit"]:
                try:
                    amount = float(input("Enter the Amount: "))
                    if amount <= 0:
                        raise ValueError("Amount must be positive")
                    bank.make_transaction(amount, transaction_type)
                except ValueError as ve:
                    print(f"Invalid amount: {ve}")
            else:
                print("Invalid transaction type, Choose between Deposit or Withdraw")
    connection.close()
else:
    print("Failed to connect to the database")


# 12b045020