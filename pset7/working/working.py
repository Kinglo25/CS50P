import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    ans = ""
    min = ""
    hours = ""
    if not re.search(r"^(?:(\d+:?\d*? AM) to (\d+:?\d*? PM)|(\d+:?\d*? PM) to (\d+:?\d*? AM))$", s):
        raise ValueError
    if matches := re.search(r"^(?:(\d+:?\d*? AM) to (\d+:?\d*? PM)|(\d+:?\d*? PM) to (\d+:?\d*? AM))$", s):
        for i in range(1, 5):
            if string := matches.group(i):
                if matches_2 := re.search(r"^(\d+):?(\d*)?", string):
                    if matches_2.group(1):
                        hours = matches_2.group(1)
                        if int(hours) > 12:
                            raise ValueError
                    if matches_2.group(2):
                        min = matches_2.group(2)
                        if int(min) >= 60:
                            raise ValueError
                if string.endswith("AM"):
                    hours = int(hours)
                    if hours == 12:
                        ans += "00:"
                    else:
                        ans += str(hours).zfill(2) + ':'
                    if min:
                        ans += min
                    else:
                        ans += "00"
                else:
                    hours = int(hours) + 12
                    if hours == 24:
                        ans += "12:"
                    else:
                        ans += str(hours).zfill(2) + ':'
                    if min:
                        ans += min
                    else:
                        ans += "00"
                if not re.search("to", ans):
                    ans += " to "
    return ans


if __name__ == "__main__":
    main()