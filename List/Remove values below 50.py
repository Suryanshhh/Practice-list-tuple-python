scores=[45,67,89,32,76]
#for i in scores:
#    if i<50:
#        scores.remove(i)

a=[i for i in scores if i>=50]
print("The list after removing values below 50 is:", a)            