import csv, sys

def main():
    str = check_argv(sys.argv)
    if str:
        print(str)
        sys.exit(42)
    copy = lst_name(sys.argv[1])
    convert(sys.argv[2], copy)

def check_argv(argv):
    if len(argv) < 3:
        return "Too few command-line arguments"
    elif len(argv) > 3:
        return "Too many command-line arguments"
    if not argv[1].endswith(".csv"):
        return "Not a CSV file"
    return 0

def lst_name(arg):
    students = []
    try:
        with open(arg, 'r') as file:
            r = csv.DictReader(file)
            for row in r:
                students.append(row)
    except FileNotFoundError:
        print("File Not found")
        sys.exit(1)
    return students

def convert(arg, copy):
    try:
        with open(arg, 'w') as file:
            fieldnames = ["first", "last", "house"]
            w = csv.DictWriter(file, fieldnames=fieldnames)
            w.writeheader()
            for row in copy:
                last, first = row["name"].split(', ')
                w.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        print("File Not found")
        sys.exit(1)

if __name__ == "__main__":
    main()