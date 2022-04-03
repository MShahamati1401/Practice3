import random

list = []
list_temp = []
count = 0
get_numbers = int(input("Please Inter Numbers random"))
while count < get_numbers:
    numbers = random.randint(1, 20)
    if numbers in list:
        continue
    else:
        list.append(numbers)
        count += 1
print(list)
