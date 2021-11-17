print ("""1.Determine odd or even
2.Determine bigger number
3.Find sum of numbers
4.Display even numbers, inclusive
 """)

number = input("Enter your choice (1-4):")

if number=="1":
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
    if (x == 'q'):
      break
    print("No valid integer! Please try again ...")



elif number=="2":
  input_1 = int(input("Enter number 1:"))
  input_2 = int(input("Enter number 2:")) 
  if input_1==input_2:
    print("The two numbers are the same")
  elif input_1<input_2:
    print("Number 2 is bigger than Number 1")
  elif input_1>input_2:
    print("Number 1 is bigger than Number 2")
  else:
    print("The two numbers are not the same")



else:
   print("You did not enter a valid input")
   exit()   

print(f"Price is ${price}")


