list1 = [6,1]
list2 = [2,4]
result = [list1[i] for i in range(len(list1)) for j in range(list2[i])]
print(result)
