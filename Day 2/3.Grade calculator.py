# Grade calculator

a=int(input("Enter your mark:"))

if a>=90:
    print("You have secured A grade")
elif a>75 and a<89:
    print("You have secured B grade")
elif a>50 and a<74:
    print("You have secured C grade")
else:
    print("You have Failed")