ans = input("Expression: ").strip().split()

ans[0] = float(ans[0])
ans[2] = float(ans[2])
match ans[1]:
    case "+":
        print(ans[0] + ans[2])
    case "-":
        print(ans[0] - ans[2])
    case "/":
        print(ans[0] / ans[2])
    case "*":
        print(ans[0] * ans[2])