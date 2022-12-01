input = input("Input: ").strip()
output = input.replace('a', '').replace('e', '').replace('u', '').replace('i', '').replace('o', '').replace('A', '').replace('E', '').replace('U', '').replace('I', '').replace('O', '')
print(f"Output: {output}")