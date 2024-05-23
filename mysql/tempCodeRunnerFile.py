            if hashed_password:
                hashed_password = hashed_password[0]  # Extract the hashed password from the tuple
                return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
            else:
                return False  # Return False if hashed password is not found