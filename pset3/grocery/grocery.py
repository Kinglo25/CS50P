grocery_list = {}
while True:
    try:
        item = input("").upper()
    except EOFError:
        break
    else:
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
grocery_list = sorted(grocery_list.items())
for item in grocery_list:
    print(item[1], item[0], sep=' ')
