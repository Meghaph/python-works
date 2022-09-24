from tkinter import *
root=Tk()
root.geometry('300x300')
root.title("MAD LIB GENERATOR")
Label(root, text= 'Mad Libs Generator \n Have Fun!' , font = 'arial 20 bold').pack()

def madlib():
    name= input("Enter your name")
    rollno=input("enter your roll number")
    sec=input("Enter your section")

    print("HEllO"+name+ " !!" "\n nice name actually!!\n Here is the details about you,\n So your name is" +name+" ,your register number is"+rollno+" ,and your sectio is"+sec)


B=Button(root, text= 'SHOW DETAILS', font ='arial 15', command= madlib, bg = 'ghost white').place(x=60, y=120)

root.mainloop()

