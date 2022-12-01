import csv, sys
from tabulate import tabulate

def main():
    str = check_argv(sys.argv)
    if str:
        print(str)
        sys.exit(42)
    print(tabulated_csv_file(sys.argv[1]))


def check_argv(argv):
    if len(argv) < 2:
        return "Too few command-line arguments"
    elif len(argv) > 2:
        return "Too many command-line arguments"
    if not argv[1].endswith(".csv"):
        return "Not a CSV file"
    return 0

def tabulated_csv_file(arg):
    try:
        with open(arg) as file:
            reader = csv.reader(file)
            headers = next(reader, None)
            return tabulate(reader, headers, tablefmt="grid")
    except FileNotFoundError:
        print("File Not found")
        sys.exit(1)

if __name__ == "__main__":
    main()