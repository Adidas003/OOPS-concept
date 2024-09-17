# import calendar

# year = int(input("Enter the year :"))
# month = int(input("Enter the month :"))

# cal = calendar.month(year, month)

# print(cal)


num = int(input("Enter the number"))

flag = False;

if num == 1:
    print(f"{num},is not a prime number")
    
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            
            break
if flag:
    print(f"{num}, is not a prime numbner")
else:
    print(f"{num}, is a prime number")



