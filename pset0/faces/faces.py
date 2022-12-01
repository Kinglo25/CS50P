def main():
    print(convert(input()))

def convert(str):
    str = str.replace(":)", '🙂').replace(":(", '🙁')
    return str

main()