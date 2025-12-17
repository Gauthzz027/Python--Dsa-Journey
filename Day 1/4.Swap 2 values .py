#swap two numbers using a temporary variable

a=int(input("Enter first value:"))
b=int(input("Enter second value:"))

print("Before swapping")
print(f"First value is {a}")
print(f"Second value is {b}")

print("After swapping")
c=a
a=b
print(f"First value is {a}")
print(f"Second value is {c}")

