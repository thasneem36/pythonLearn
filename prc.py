def printname():
    if user == "mt" and password == 123:
        print("hello admin")
    else:
        print("worrng password")
        
user = input("enter the username")
password = int(input("password"))

printname()