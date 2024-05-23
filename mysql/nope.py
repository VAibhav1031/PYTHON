import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


password = "example_password"
hashed_password = hash_password(password)
print("Hashed Password:", hashed_password.decode('utf-8'))
