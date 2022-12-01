import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    count = 0
    while (matches := re.search(r"( um($|\?|\.|\,|\:| |\!))|(^um($|\?|\.|\,|\:| |\!))", s, re.IGNORECASE)):
        s = s[matches.span()[1]:]
        count += 1
    return count

if __name__ == "__main__":
    main()