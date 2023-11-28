while True:
    password1 = input("input passport：")     
    password2 = input("input passport again：")
    if password1 == password2 and 8 <= len(password1) <= 12:
        print("successful！")
        break
    else:
        print("fail do it again")