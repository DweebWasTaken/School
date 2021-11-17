input_1 = int(input("Enter starting number:"))
input_2 = int(input("Enter ending number:"))


if (input_1> input_2):
 for i in reversed(range(input_2, input_1+1,2)):
  print(i,end= ' ')
 else:
  print() 
 

else:
 for i in range(input_1, input_2,2):
  print(i,end= ' ')

 else:
  print() 
