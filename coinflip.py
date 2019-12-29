import random
import time
def cflip ():
    game_on =  True
    restart = False
    bet = 0
    while game_on:
        coin_flip= random.choice(["heads","tails"])
        flip_guess = input('heads or tails? ')
        bet_amount = int(input (f'''
        Your bet amount is currently {bet}, 
        how much more money do you wish to add? 
        If you dont want to add money, just enter 0
        '''))
        print ("Flipping...")
        time.sleep(2)
        if flip_guess == coin_flip:
            bet = bet + bet_amount
            print (f"You were right! The coin is flipped on {flip_guess}! Your bet has been increased to {bet}")
        else:
            bet = bet - bet_amount
            print (f"Oops, looks like the coin flipped on {coin_flip}, try again next time! Your bet has been decreased to {bet}")
        if bet < 0:
            print("Looks like your bet has become debt, pay up!")
            print("Game over")
            game_restart = input ('Restart game?')
            if game_restart == 'no':
                break
            elif game_restart == 'yes':
                restart = True
                bet = 0
        if not restart:
            game_continue = input("Continue game?")
            if game_continue == 'yes':
                game_on = True
            elif game_continue == 'no':
                game_on = False
            else:
                print ("Sorry, that is an invalid response.")

