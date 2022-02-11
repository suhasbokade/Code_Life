from functools import reduce

input_list1 = [3, 4, 5, 6]
print(f"addition of {input_list1}=", reduce(lambda x, y: x + y, input_list1))

input_list2 = [1, 8, 4, 9]
print(f"addition of {input_list2}=", reduce(lambda x, y: x+y, input_list2))

input_list3 = [13, 14, 15, 10]
print(f"addition of {input_list3}=", reduce(lambda x, y: x +y, input_list3))