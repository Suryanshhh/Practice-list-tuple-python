l1=[]
for i in range(7):
    l1.append(int(input("Enter a number: ")))
    
print("The list that user have entered is:", l1)
print("The maximum number in the list is:", max(l1))
print("The minimum number in the list is:", min(l1))
print("The avg of the numbers in the list is:", (sum(l1))//len(l1))