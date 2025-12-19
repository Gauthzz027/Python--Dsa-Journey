# Reversing a number using loops (MATHEMATICAL DIGIT-BY-DIGIT)

num=input("Enter any number:")
rev=0

while num != 0:
    last= num%10
    rev = rev*10+last
    num = num//10

print(rev)

#rev1=str(num[::-1])
#print(rev1)