l1=[]
for i in range(6):
    l1.append(int(input("Enter a number: ")))

print("The list that user have entered is:", l1)

event_count=0
odd_count=0
for i in range(len(l1)):
    if l1[i]%2==0:
         event_count+=1
    else:
         odd_count+=1
print("The count of even numbers in the list is:", event_count)
print("The count of odd numbers in the list is:", odd_count)         