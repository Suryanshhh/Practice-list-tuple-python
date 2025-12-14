t = (1, 2, 3, 4)
# Output: (4, 2, 3, 1)
b=list(t)
a=b[0]
b[0]=b[-1]
b[-1]=a
print(tuple(b))