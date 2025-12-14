l1=[]
a=int(input("Elements number"))
for i in range(a):
    l1.append(int(input("Enter a number: ")))

print("The list that user have entered is:", l1)
duplicate_values=[]

for i in range(a):
    if l1.count(i)>1 and i not in duplicate_values:
        duplicate_values.append(i)
print("The duplicate values in the list are:", duplicate_values)