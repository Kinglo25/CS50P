import sys, requests, json

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit(1)
try:
    amount = float(sys.argv[1])
except ValueError:
    print("NaN")
    sys.exit(1)
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r = r.json()
    amount *= r["bpi"]["USD"]["rate_float"]
    print(f"${amount:,.4f}")
except requests.RequestException:
    sys.exit(1)