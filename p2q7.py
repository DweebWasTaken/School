while True:
 try:
   x = int(input("Enter an integer: "))
   print("Great, you have successfully entered an integer!")

 except ValueError:
   print("No valid integer! Please try again ...")
