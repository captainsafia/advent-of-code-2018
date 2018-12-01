# Iteration 1
with open("frequencies.txt") as frequencies:
    result = 0
    numbers = frequencies.read().splitlines()
    for number in numbers:
        if number.startswith("-"):
            number_as_int = int(number[1:])
            result -= number_as_int
        elif number.startswith("+"):
            number_as_int = int(number[1:])
            result += number_as_int
        else:
            raise Exception("{} is not in the valid format.".format(number))
    print(result)

# Iteration 2
with open("frequencies.txt") as frequencies:
    result = 0
    numbers = frequencies.read().splitlines()
    for number in numbers:
        result += int(number)
    print(result)

# Iteration 3
with open("frequencies.txt") as frequencies:
    result = sum([int(number) for number in frequencies.read().splitlines()])
    print(result)