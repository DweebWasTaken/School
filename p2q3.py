years = int(input("Enter years:"))
salary = int(input("Enter salary:"))

if (years <10 ):
    if (salary < 1000):
         print("Increament is $100")
    elif (salary < 2000):
         print("Increament is $200")
    else:
     print("Increament is $300")
else:
    if (salary < 1000):
         print("Increament is $200")
    elif (salary < 2000):
         print("Increament is $300")
    else:
     print("Increament is $400")