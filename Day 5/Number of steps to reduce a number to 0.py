# Print number of steps to reduce a number to zero

n=int(input("Enter a number:"))
counter=0

while n!=0:
    if n%2==0:
        n=n/2
        counter=counter+1
    else:
        n=n-1
        counter=counter+1


print(f"{counter} steps")