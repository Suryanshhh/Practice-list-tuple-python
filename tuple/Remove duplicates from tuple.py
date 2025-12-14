t = (1, 2, 2, 3, 1)
# Output: (1, 2, 3)

a=[]

for i in t:
    if i not in a:
        a.append(i)
print(tuple(a))