import sys

def main():
    check_argv()
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    else:
            print(count_los(file))
    file.close()

def count_los(file):
    nb_of_lines = 0
    for line in file:
        line = line.lstrip()
        if line.startswith('#') or not line:
            continue
        else:
            nb_of_lines += 1
    return nb_of_lines

def check_argv():
    if len(sys.argv) > 2:
        print("Too many args")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few args")
        sys.exit(1)
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

if __name__ == "__main__":
    main()