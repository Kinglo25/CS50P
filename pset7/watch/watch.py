import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^<iframe(?:.*)(https?://(?:www\.)?youtube\.com/embed/\w*)(?:.*)></iframe>$", s):
        return match.group(1).replace("be.com/embed", ".be").replace("www.", "").replace("http:", "https:")


...


if __name__ == "__main__":
    main()