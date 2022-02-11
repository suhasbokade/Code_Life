

input_list1 = [3, 4, 5, 6]
input_list2 = [1, 8, 4, 9]
input_list3 = [13, 14, 15, 10]
sum_of_value = list(map(lambda x, y, z: (x+y+z), input_list1, input_list2, input_list3))
print(sum_of_value)