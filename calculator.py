import time
def cal():
    first_number = float(input('First number: '))
    sign = input('Sign: ')
    second_number = float(input('Second number: '))
    result = 0
    if sign == '+':
        result = first_number + second_number
    if sign == '-':
        result = first_number - second_number
    if sign == 'x':
        result = first_number * second_number
    if sign == '/':
        result = first_number / second_number
    print(result)
    time.sleep(5)





