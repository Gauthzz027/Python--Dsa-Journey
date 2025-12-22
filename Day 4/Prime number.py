#check prime number or not
import math
def prime():
    n=int(input("Enter a number:"))
    
    if n<1:
        print("Not a prime number")
        return
    a=int(math.sqrt(n)+1)
    for i in range(2,a):
        if n%i==0:
            print(f"{n} is not a prime number")
            return

    print(f"{n} is a prime number")
prime()