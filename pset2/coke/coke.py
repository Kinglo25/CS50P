amount = 50
while (amount > 0):
    print(f"Amount Due: {amount}")
    try:
        coin = int(input("Insert coin: "))
    except:
        continue
    if (coin != 25 and coin != 10 and coin != 5):
        continue
    amount -= coin
print(f"Change owed: {abs(amount)}")