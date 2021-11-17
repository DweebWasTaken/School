while True:
 try:
   x = int(input("Enter an integer: "))
   if  (x % 2) == 0:
    print("The number is even")
   elif (x % 1) == 0:
    print("The number is odd")
   else:
    print("Great, you have successfully entered an integer!")

 except ValueError:
   print("No valid integer! Please try again ...")


