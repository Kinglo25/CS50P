from random import randint


def main():
    score = 0
    level = get_level()
    for _ in range(10):
        chances = 3
        x = generate_integer(level)
        y = generate_integer(level)
        while chances:
            print(x,'+', y, '= ', end="")
            ans = int(input())
            if ans == x + y:
                score += 1
                break
            else:
                print("EEE")
                chances -= 1
                if chances == 0:
                    print(x,'+', y, '= ', x + y)
    print(score)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 1 and level != 2 and level != 3:
                raise ValueError
        except ValueError:
            continue
        else:
            return level


def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    if level == 2:
        return randint(10, 99)
    if level == 3:
        return randint(100, 999)


if __name__ == "__main__":
    main()