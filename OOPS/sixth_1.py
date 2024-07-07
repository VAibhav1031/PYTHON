"""
This module provides a simple banking system with user authentication and transaction capabilities.
"""

import mysql.connector
import bcrypt

my_host = "localhost"
my_database = "VtBank"
my_user = "root"
my_password = "UP@,./456"


def connect_to_database():
    """
    Connects to the MySQL database with the given credentials.
    
    Returns:
        connection: MySQL connection object.
        cursor: MySQL cursor object.
    """
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
    """
    Creates the Auth table in the database if it does not exist.
    
    Args:
        cursor: MySQL cursor object.
    """
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Auth (
                User_Name VARCHAR(255), 
                Passwrd VARCHAR(255),
                Balance INT,
                Acc_No VARCHAR(255)
            )
        """)
        print("Table created successfully or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")


class Bank:
    """
    A class used to represent a Bank.

    Attributes:
        accountNo (str): The account number of the bank account.
        balance (int): The balance of the bank account.
        connection: MySQL connection object.
        cursor: MySQL cursor object.
    """

    def __init__(self, accountNo: str, connection, cursor) -> None:
        """
        Constructs all the necessary attributes for the bank object.

        Args:
            accountNo (str): The account number.
            connection: MySQL connection object.
            cursor: MySQL cursor object.
        """
        self.accountNo = accountNo
        self.balance = 2000
        self.connection = connection
        self.cursor = cursor

    class Transact:
        """
        A nested class used to represent a transaction.

        Attributes:
            amount (float): The amount of the transaction.
            transition_type (str): The type of the transaction, either 'Withdraw' or 'Deposit'.
        """

        def __init__(self, amount, transition_type):
            """
            Constructs all the necessary attributes for the transaction object.

            Args:
                amount (float): The amount of the transaction.
                transition_type (str): The type of the transaction, either 'Withdraw' or 'Deposit'.
            """
            self.amount = amount
            self.type = transition_type.lower()

        def process(self, account):
            """
            Processes the transaction on the given account.

            Args:
                account (Bank): The bank account object to apply the transaction to.
            """
            if self.type == "withdraw":
                if account.balance >= self.amount:
                    account.balance -= self.amount
                else:
                    print("Insufficient Funds in the Accounts :)) !! ")

            elif self.type == "deposit":
                account.balance += self.amount

            else:
                print("Invalid Transaction Type:")
                return

            try:
                account.cursor.execute("UPDATE Auth SET Balance = %s WHERE Acc_No = %s", (account.balance, account.accountNo))
                account.connection.commit()
                print(f"Transaction successful.")
            except mysql.connector.Error as err:
                print(f"Error updating balance: {err}")

    def make_Transaction(self, amount, Transaction_type):
        """
        Initiates a transaction of a given type and amount.

        Args:
            amount (float): The amount to be transacted.
            Transaction_type (str): The type of the transaction, either 'Withdraw' or 'Deposit'.
        """
        k = self.Transact(amount, Transaction_type)
        k.process(self)
        print(f"Balance : $ {self.balance}")

    def Authentication(self, connection, cursor):
        """
        Authenticates the user, either as a new user or an existing user.

        Args:
            connection: MySQL connection object.
            cursor: MySQL cursor object.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
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
                try:
                    cursor.execute("INSERT INTO Auth (User_Name, Passwrd, Balance, Acc_No) VALUES (%s, %s, %s, %s)", 
                                   (usr, hashed_passwrd, self.balance, self.accountNo))
                    connection.commit()
                    print("Successfully done!")
                    return True
                except mysql.connector.Error as err:
                    print(f"Error: {err}")

        elif ch == "2":
            usr = input("Username: ")
            passwrd = input("Password: ")

            def verify_password(password, hashed_password):
                return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

            try:
                cursor.execute("SELECT Passwrd FROM Auth WHERE User_Name = %s", (usr,))
                result = cursor.fetchone()

                if result:
                    hashed_password = result[0].encode('utf-8')
                    if verify_password(passwrd, hashed_password):
                        print("User authenticated!")
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


# Main Program
connection, cursor = connect_to_database()
if connection and cursor:
    create_table(cursor)
    bank = Bank("25OP23ASD", connection, cursor)
    if bank.Authentication(connection, cursor):
        while True:
            transaction_type = input("Enter the Transaction Type [Withdraw, Deposit, quit]: ")
            if transaction_type == "quit":
                break
            elif transaction_type in ["Withdraw", "Deposit"]:
                try:
                    amount = float(input("Enter the Amount: "))
                    bank.make_Transaction(amount, transaction_type)
                except ValueError:
                    print("Invalid amount!")
            else:
                print("Invalid transaction type, Choose between Deposit or Withdraw")
else:
    print("Failed to connect to the database")

if connection:
    connection.close()





print(connect_to_database.__doc__)
print(Bank.__doc__)
print(Bank.Transact.__doc__)
print(Bank.Transact.process.__doc__)
