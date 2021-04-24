import bcrypt

password = b"ThisIsMyPassword"
hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed_pw)


enetred_password = input("Enter your password: ")
enetred_password = bytes(enetred_password, encoding="utf-8")
if bcrypt.checkpw(enetred_password, hashed_pw):
    print("Logged in!")
else:
    print("Invalid Password!")
