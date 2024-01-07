import sqlite3
con=sqlite3.connect("Database.db")

def insertdata(name,age,city):
    qry = "insert into User(name,age,city) values(?,?,?);"
    con.execute(qry,(name,age,city))
    con.commit()
    print("Insert sucessfully")
print("""
      1.insert
      2.update
      3.delete
      4.display
      """)
      
ch=1
while ch==1:
    c=int(input("Enter your choice"))
    if(c==1):
        print("INSERT")
        name = input("Enter your name")
        age = int(input("Enter your age"))
        city = input("Enter your city")
        insertdata(name,age,city)
    elif(c==2):
        print("UPDATE")
    elif(c==3):
        print("DELETE")
    elif(c==4):
        print("DISPLAY")
    else:
        print("invalid selection")
        ch=int(input("Enter 1 to continue"))
        print("Thankyou")