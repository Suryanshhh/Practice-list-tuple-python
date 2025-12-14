lst = [1, 2, 2, 3, 1, 4]
# Output: [1, 2, 3, 4]

l=[]
for i in range(len(lst)):
    if lst[i] not in l:
        l.append(lst[i])
print(l)