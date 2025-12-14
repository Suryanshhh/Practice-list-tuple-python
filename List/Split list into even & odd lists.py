lst = [1, 2, 3, 4, 5, 6]
# Output: even=[2,4,6], odd=[1,3,5]

even=[]

for i in lst:
    if i%2==0:
        even.append(i)
        lst.remove(i)
print("even=",even)
print("odd=",lst)