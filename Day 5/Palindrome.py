n=int(input("Enter a number:"))
rev=0
dup=n
while n!=0:
    last=n%10
    rev= rev*10+last
    n=n//10


if rev==dup:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")
