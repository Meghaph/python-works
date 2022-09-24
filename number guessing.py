from http.client import CONTINUE
import random
from re import I
print("hello there!!")
print("are you ready to play number guessing game!? ")
play=input("YES?? or NO??")
if play.lower()== "yes":
    print("That's great!!! let's play game:)")


i=0
while i<5:
   guesses=1
   i += 1
   print("chance number:"+str(i))
   j=5-i
   print("Your remaining chance is:",j)
   print("\n")

   
   guess_num=input("input your guessing number:")
   print("the number you guessed is:",guess_num)
   print("\n")

   rand_num= random.randrange(-1,11)
   if rand_num==guess_num:
    print("You got it correctly!!")
    guesses=guesses+1
    print("you got it at",guesses,)
    quit()
   else:
    print("You are wrong!!try again")
    print("The number was "+str(rand_num))
    print("-------------------------------")
    
    
elif play=="NO":
    print("OK!!")
else:
    print("wrong input please give the corrrect choice")



   
    

    
    