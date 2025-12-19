# Print sum of digits of number

n=input("Enter a number:")

l=list(n)

sum=0

for i in l:
    sum= int(i)+sum
print(sum)
