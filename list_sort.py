list = []
list_temp = []
flag = True
while flag:
    entrance = input("Please Inter Number or cancel typed exit ")
    if entrance == "exit":
        break
    else:
        numbers = int(entrance)
        list.append(numbers)
list_temp = list_temp + list
list_temp.sort()
print(f"list User: {list}")
print(f"List Sorted of user: {list_temp}")
if list == list_temp:
    print(f"Two List equal")
else:
    print("Two List Not equal")

