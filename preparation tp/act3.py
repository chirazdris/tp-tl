my_list = [1, 3, 5, 7, 9, 8, 6, 4, 2]
for i in range(len(my_list)//2):
    my_list[i], my_list[-(i+1)] = my_list[-(i+1)], my_list[i]
print(my_list)
