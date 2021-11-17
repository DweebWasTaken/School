number = input("Enter your choice (1-2): ")
staff = input("Are you a staff (Y/N)? ")
if number=="1":
   if staff == "Y":
        price = 5*0.9
   else:
        price = 5*0.95
elif number=="2":
    if staff == "Y":
        price = 10*0.8
    else:
        price = 10
else:
   print("You did not enter a valid input")
   exit()   

print(f"Price is ${price}")
