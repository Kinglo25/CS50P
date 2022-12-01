def main():
    if len(sys.argv) > 2:
        print("Too many args")
        sys.exit(1)
    elif len(sys.argv) < 2:
        print("Too few args")
        sys.exit(1)
    try:
        file = open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(1)
    else:
        print(count_los(file))
    file.close()

                      #sdasdas
#dsadasdasdasdasdasd
                      #sdasdas
