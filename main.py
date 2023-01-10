def makesumofdigits(number):
    sumofdigits = 0
    while number % 10 > 0:
        sumofdigits += number % 10
        number = number // 10
    print("Calculated sum of digits: ")
    print(sumofdigits)


try:
    print("Enter integer number via keyboard: ")
    makesumofdigits(int(input()))
except:
    print("Input is not OK (text, symbols and floating numbers are not allowed for input).")
