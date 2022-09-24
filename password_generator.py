#password generator program
from operator import truediv
import random

char="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()~`"
while 1:
    char_length=int(input("Enter the length of the character"))
    char_no=int(input("Enter the number of password that you want to generat"))
    for x in range(0,char_no):
        password=''
        for x in range(0,char_length):
         password_gen=random.choice(char)
         password=password+password_gen
        print("The password is:"+password)
