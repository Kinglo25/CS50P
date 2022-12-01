import sys

from PIL import Image, ImageOps

def main():
    str = check_argv(sys.argv)
    if str:
        print(str)
        sys.exit(42)
    overlay_images(sys.argv)

def check_argv(argv):
    #Check # of cmd line agr
    if len(argv) < 3:
        return "Too few command-line arguments"
    elif len(argv) > 3:
        return "Too many command-line arguments"

    #Check if the arg ends with ".jpg", ".jpeg" or ".png" and if both end with ther same
    ends = (".jpg", ".jpeg", ".png")
    if not argv[1].lower().endswith(ends) or not argv[2].lower().endswith(ends):
        return "Invalid input"
    if argv[1].lower()[-3:] != argv[2].lower()[-3:]:
        return "Input and output have different extensions"

    #Check if arg[1] can be opened
    try:
        with open(argv[1]) as file:
            pass
    except IOError:
        return "File can't be open"
    #Returns 0 if everthing is ok!
    return 0

def overlay_images(argv):
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(sys.argv[1]) as photo:
                photo = ImageOps.fit(photo, shirt.size)
                photo.paste(shirt, shirt)
                photo.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    except OSError:
        sys.exit(f"Can not convert {input_image}")

if __name__ == "__main__":
    main()