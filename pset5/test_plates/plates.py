def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not (s[0].isalpha()) or not (s[1].isalpha()):
        return False
    m = 0
    for char in s:
        if char == '0' and m == 0:
            return False
        if char.isdigit():
            m = 1
        if char.isalpha() and m == 1:
            return False
        if not char.isalnum():
            return False
    return True


if __name__ == "__main__":
    main()