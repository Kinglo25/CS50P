def main():
    str = input("Input: ").strip()
    print(shorten(str))

def shorten(word):
    char_str = "aAeEuUiIoO"
    for char in char_str:
        word = word.replace(char, '')
    return word


if __name__ == "__main__":
    main()