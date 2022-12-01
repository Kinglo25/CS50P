import random

def main():
    guess_number(get_level())

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise ValueError
        except ValueError:
            continue
        else:
            return level

def guess_number(level):
    x = random.randint(1, level)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError
        except ValueError:
            continue
        else:
            if guess == x:
                print("Just right!")
                break
            elif guess > x:
                print("Too large!")
                continue
            else:
                print("Too small!")
                continue

if __name__ == "__main__":
    main()