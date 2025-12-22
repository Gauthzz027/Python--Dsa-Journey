# Count digits of a number

def count_digits():
    x=0
    n=int(input("Enter a number:"))
    if n==0:
        print (1)
    while n !=0:
        n=n//10
        x= x+1
    print(x)
count_digits()