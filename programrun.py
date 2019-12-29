from unicon import unicon
from calculator import cal
from coinflip import cflip
from test import mumble_jumble
on = True
while on == True:
    program = input('Program: ')
    if program == ('unicon'):
        unicon()
    elif program == ('cal'):
        cal()
    elif program == ('cflip'):
        cflip()
    elif program == ('mumblejumble'):
        mumble_jumble()
    elif program == ('stop'):
        break
