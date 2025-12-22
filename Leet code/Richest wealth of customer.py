account=[[1,2,3],[2,3,4]]
max_row=0
for row in account:
    current=0
    for amount in row:
        current= current+amount
    if current>max_row:
        max_row=current
print(max_row)