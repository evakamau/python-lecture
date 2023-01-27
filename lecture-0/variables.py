# containers that stoer information

NAME = ""
NUMBERS = ""


def another_hello_world(string: str):
    argument_passed = string
    NUMBERS = 20
    print(argument_passed, NUMBERS)


if __name__ == "__main__":
    another_hello_world("print me")
