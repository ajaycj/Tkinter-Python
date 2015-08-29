from Tkinter import *
import tkMessageBox
import MySQLdb

# Code to add widgets will go here...


master = Tk()
def callback():
    db = MySQLdb.connect("localhost", "root", "ajay.cj", "TEST")

    cursor = db.cursor()

    cursor.execute("SELECT * from NAME")

    data = cursor.fetchone()
    
    data = str(data)
    
    #data = data.split("('")

    for d in data:
        if(type(d) == "<type 'str'>"):
            print d
    
    db.close()
    tkMessageBox.showinfo("output", data)
    #return data	
#	tkMessageBox.showinfo("say hello", "Hello world")

b = Button(master, text = "data", command = callback)
b.pack()
mainloop()
