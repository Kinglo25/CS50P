from validator_collection import checkers

if checkers.is_email(input("Input: ").strip().lower()):
    print("Valid")
else:
    print("Invalid")