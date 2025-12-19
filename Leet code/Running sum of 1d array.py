num=list(map(int,input().split()))
print(num)

counter=0
list=[]
for i in num:
    counter= counter+i
    list.append(counter)
print(list)