def collatz(number):
    if number % 2 == 0:
        result = number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
    print(result)
    return result


while True:
    try:
        print('Pick a number!')
        inputNumber = int(input())
        while inputNumber != 1:
            inputNumber = collatz(inputNumber)
        break
    except ValueError:
        print('You must enter an integer!')