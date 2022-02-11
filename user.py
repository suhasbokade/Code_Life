import calculator as cal

input_1 = 20
input_2 = 10

total_sum = cal.add(input_1, input_2)
print(f"sum of {input_1} and {input_2} is = {total_sum}")
total_sub = cal.sub(input_1, input_2)
print(f"sub of {input_1} and {input_2} is = {total_sub}")
total_multi = cal.multiply(input_1, input_2)
print(f"multiply of {input_1} and {input_2} is = {total_multi}")
total_division = cal.division(input_1, input_2)
print(f"division of {input_1} and {input_2} is = {total_division}")
total_floor = cal.floor(input_1, input_2)
print(f"floor of {input_1} and {input_2} is = {total_floor}")
