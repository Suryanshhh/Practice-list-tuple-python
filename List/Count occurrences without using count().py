lst = [1, 2, 2, 3, 2]
# Output: {1:1, 2:3, 3:1}
l=[]
for i in range(len(lst)):
    if lst[i] not in l:
        count=0
        for j in range(len(lst)):
            if lst[i]==lst[j] :
                count+=1
        l.append(lst[i])
        print(f"the count of {lst[i]} is {count}")

