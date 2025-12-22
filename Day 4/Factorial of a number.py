# Print factorial of a number

def factorial():
    n=int(input("Enter a number:"))
    b=1
    if n<0:
        print("Enter positive number")
    b=1
    for i in range(1,n+1):
        b*=i 
    print(b)
factorial()

