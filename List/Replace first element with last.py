lst = [10, 20, 30, 40]
# Output: [40, 20, 30, 10]
#temp=lst[0]
#lst[0]=lst[-1]
#lst[-1]=temp
#print(lst)

#2nd method
#lst[0],lst[-1]=lst[-1],lst[0]
#print(lst)

#3rd method
#a=lst.pop(0)
#b=lst.pop(-1)
#lst.insert(0,b)
#lst.append(a)


#4th method
lst=[lst[-1]]+lst[1:-1]+[lst[0]]
print(lst)

