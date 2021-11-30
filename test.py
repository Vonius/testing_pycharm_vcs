from functions import call_my_name


def main(a, b):
    print(f"The sum of {a} and {b} is {a+b}")
    return a + b


if __name__ == "__main__":
    main(4, 6)
    call_my_name()