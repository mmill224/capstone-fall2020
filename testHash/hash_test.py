from passlib.hash import sha256_crypt

# Immidiately hashes password upon input
hashed_password = sha256_crypt.hash((input("Please enter a password: ")))
print(hashed_password)

password2 = input("Re-enter your password: ")
print(sha256_crypt.hash(password2))

hashed_password2 = sha256_crypt.hash(password2)
# if (hashed_password == hased_password2) ....
# ^^ THIS WILL FAIL ^^ 
# Hashed passwords are not the same even if the same string is used

# Can use verify function to test if equal
if (sha256_crypt.verify(password2, hashed_password)):
    print("Passwords match")
else:
    print("Passwords do not match")
