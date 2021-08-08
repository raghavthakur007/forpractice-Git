num = int(input("Enter your three digit number"))
rem= num%10
num = int(num/10)

rem = rem*(num%10)
num = int(num/10)
rem =rem*(num%10)
num= num/10
print("The number is :",rem)
