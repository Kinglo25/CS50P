import inflect

p = inflect.engine()

my_list = []
while True:
    try:
        my_list += [input("Name: ")]
    except EOFError:
        break
new_list = p.join(my_list)
print("Adieu, adieu, to " + new_list)