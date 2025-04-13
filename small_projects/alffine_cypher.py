# we are gonnna create the


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None


def encrypt(a, b, test_v):
    #
    # a*x + b  mod 26
    result = ""
    for ch in test_v:
        if ch.isalpha():
            x = ord(ch) - ord("a")
            new_i = (a * x + b) % 26
            result += chr(new_i + ord("a"))

        else:
            result += ch  # no change to punctuation and space
    return result


def decrypt(a, b, encr):
    # finding the inverse of a
    a_inv = mod_inverse(a, 26)

    decrypted = ""
    for ch in encr:
        if ch.isalpha():
            y = ord(ch) - ord("a")
            w = (a_inv * (y - b)) % 26
            decrypted += chr(w + ord("a"))

        else:
            decrypted += ch
    return decrypted


if __name__ == "__main__":
    # i know i know there are only 12 valid ones a  which are co-prime but i want to go by myself

    while True:
        try:
            a = int(input("Enter the a : "))
            b = int(input("Enter the b : "))

        except ValueError as e:
            print(f"OOOOOOPSS !!! Error Occured : {e}")
            continue

        if gcd(a, 26) == 1 and 0 <= b <= 25:
            print("Nice mannnnnnn :)")
            break

        print("⚠️ 'a' must be coprime of a ,  and  the b must be the value between 0-25")

    test = input("Enter the string ::")

    enc = encrypt(a, b, test)

    print(f"🔒 Encrypted Value is : {enc}")

    decr = decrypt(a, b, enc)
    print(f"🔓 Decrypted value is : {decr}")

    print("BYEEEEEE+++++++++++++")
