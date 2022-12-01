import sys, random
from pyfiglet import Figlet

def main():
    f = Figlet()
    fonts = f.getFonts()
    if len(sys.argv) == 1:
        rnd_font = fonts[random.randrange(0, len(fonts))]
        print(f.renderText(input("Input: ")))
        f.setFont(font=rnd_font)
    elif len(sys.argv) == 3:
        if (sys.argv[1] != '-f' and sys.argv[1] != '--font') or sys.argv[2] not in fonts:
            sys.exit(1)
        f.setFont(font=sys.argv[2])
        print(f.renderText(input("Input: ")))
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()