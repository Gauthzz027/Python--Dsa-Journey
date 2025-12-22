# Print Fibonacci series

def fibo():
    n=int(input("Enter a number:"))
    a,b=0,1
    list=[]
    while len(list)<n:
        list.append(a)
        a,b= b,a+b
    print(list)

fibo()
