t = (10, 20, 30, 40)
# Find index of 30

a=list(t)
x=30
for i in range(len(a)):
    if a[i]==x:
        print(i)
        break