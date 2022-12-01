import pizza

def test_check_argv():
    assert pizza.check_argv(["hello"]) == "Too few command-line arguments"
    assert pizza.check_argv(["hello", "how", "are u?"]) == "Too many command-line arguments"
    assert pizza.check_argv(["hello.py", "file.csv"]) == 0
    assert pizza.check_argv(["hello.py", "file.csvasd"]) == "Not a CSV file"
