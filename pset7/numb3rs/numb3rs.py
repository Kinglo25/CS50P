import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search("^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        for i in range(1, 5):
            if int(matches.group(i)) > 255:
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    main()