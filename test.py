from functions import call_my_name, product, division


def another_test_function():
    print(f"lol, it's so boring testing vcs")


def main(a, b):
    print(f"The sum of {a} and {b} is {a + b}")
    return a + b


if __name__ == "__main__":
    main(4, 6)
    call_my_name()
    division(product(5, 6), 2)
    another_test_function()
