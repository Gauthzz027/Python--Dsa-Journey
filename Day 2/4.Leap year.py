# Check leap year

a=int(input("Enter year to check:"))

if a%4==0:
    print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year")

