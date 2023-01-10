def makesumofdigits(number):
    sumofdigits = 0
    while number // 10 > 0:
        sumofdigits += number % 10
        number = number // 10
        if len(str(number)) == 1:
            sumofdigits += int(str(number)[0])
            break
    print("Calculated sum of digits: ")
    print(sumofdigits)


# userInput = input()
try:
    print("Enter integer number via keyboard: ")
    makesumofdigits(int(input()))
except:
    print("Input is not OK (text, symbols and floating numbers are not allowed for input).")
