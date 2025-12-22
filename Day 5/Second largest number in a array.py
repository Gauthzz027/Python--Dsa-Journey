# Print the second largest number in a array

arr=list(map(int,input().split()))

first=second=float('-inf')

b=len(arr)

for i in range(b):
    if arr[i]>first:
        second=first
        first=arr[i]
    elif (first > arr[i]> second ):
        second=arr[i]



print(f"{first} is the largest number in array")
print(f"{second} is the second largest number in array")


