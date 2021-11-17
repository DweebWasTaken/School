print("Below is our drinks menu:")
print("1.Coke   2.Coffee   3.Juice")
drink = int(input("Enter your choice of drink:"))

if drink==1:
   print("Coke is $1.00")
elif drink==2:
   print("Coffee is $0.50")
elif drink==3:
   print("Juice is $2.00")
else:
   print("Sorry, you have entered an invalid choice")
