import datetime, sys
import inflect
p = inflect.engine()

def main():
    print((lived_minutes(input('Date of birth: ').strip())))


def lived_minutes(birthday):
    try:
        datetime.datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        sys.exit("Invalid date")
    else:
        birthday = datetime.date.fromisoformat(birthday)
        today = datetime.date.today()
        minutes = (today - birthday).total_seconds() / 60
        minutes = int(minutes)
        return f"{p.number_to_words((minutes), andword='').capitalize()} minutes"



if __name__ == "__main__":
    main()