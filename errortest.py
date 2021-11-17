try:
  x=int(input("Enter a number: "))
  print(1/x) #print inverse
except ValueError: #optional
  print("Pls enter a valid number!")
except ZeroDivisionError: #optional
  print("Pls enter a number bigger than 0!")
except:
  print("Any other exceptions will print this")
finally:
  print("This line will always be printed")
