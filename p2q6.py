sum = 0

while True:
    input_1 = (input("Enter a number or q to Quit:"))

    #numbers adding probelms

    if (input_1 == 'q'):
        break
    else:
        
        if input_1.isnumeric():
            sum += int(input_1)

        print(f"Current total is {input_1}")
      
print(sum)