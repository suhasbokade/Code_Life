list1 = [2, 3, 4, 55, 56, 78, 75, 69, 66, 101, 100]
even_count = 0
odd_count = 0
n = 0
while (n<len(list1)):
    if list1[n] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    n += 1

print("Even number in the list", even_count)
print("Odd number in the list", odd_count)