while True:
    try:
        x, y = input("Fraction: ").split('/')
        x = int(x)
        y = int(y)
    except ValueError:
        pass
    else:
        if (x > y):
            continue
        else:
            try:
                fuel = round(x/y * 100)
            except ZeroDivisionError:
                    continue
            else:
                if fuel >= 99:
                    print('F')
                elif fuel <= 1:
                    print('E')
                else:
                    print(f"{fuel}%")
            break

