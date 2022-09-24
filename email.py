button= input("Enter your email id").strip()
username= button[:button.index('@')]
domain= button[button.index('@')+1:]
print("Your emai is "+button+ "\n the user name is " +username+ " and domain name is "+domain)
    