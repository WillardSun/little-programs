import random
def mumble_jumble():
    message = input('Statement: ')
    for word in message:
        message = message - word
        upper_or_lower = random.choice(['upper','lower'])
        if upper_or_lower == 'upper':
            word
        elif upper_or_lower == 'lower':
            str.lower(word)
    print (message)

