password1 = input("Please set a password：")
password2 = input("Do it again：")

if password1 == password2 and 8 <= len(password1) <= 12:
    print("Successful！")
else:
    print("Fail")