import sys

def main():
    fraction_str = input("Fuel: ").strip()
    print(gauge(convert(fraction_str)))


def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage) + '%'


if __name__ == "__main__":
    main()