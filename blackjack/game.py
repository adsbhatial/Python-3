'''
Game program
'''
from blackjack import blackjack
from blackjack import player

def start_game():
    '''
    Function which performs actual blackjacking
    '''
    print("Welcome to blackjack!")
    bankroll = blackjack.correct_value("Please enter your bankroll: ", 0)
    init_bankroll = bankroll
    game_player = player.Player(bankroll)
    game_dealer = player.Player(bankroll)

    while True:
        bet_amount = blackjack.correct_value("Pleae enter your bet: ", bankroll)
        game_dealer.reset_hand()
        game_player.reset_hand()
        game = blackjack.Blackjack(bet_amount, game_dealer, game_player)

        print("Your first card is :", game.hit(game_player)[1])
        print("Your second card is :", game.hit(game_player)[1])
        print("\nDealer's first card is :", game.hit(game_dealer)[1])
        game.hit(game_dealer)
        game_bust = game.start_turn(False, game_player)
        game_lost = False
        game_tied = False
        if game_bust:
            print("\nYou busted!")
            game_lost = True
            game_won = False
        else:
            game_won = game.start_turn(True, game_dealer)
            if game_won:
                print(f"Dealer busted at {game_dealer.points()}! You won")
            else:
                print("\nDealer's hand was: ", game_dealer.hand_cards.list_cards())
                if game_dealer.points() > game_player.points():
                    game_lost = True
                    print("\nSorry you lost")
                elif game_dealer.points() == game_player.points():
                    game_tied = True
                else:
                    print("\nYou won!")

        if not game_won and game_lost:
            if game_player.remove_money(bet_amount):
                print("You lost ", bet_amount)
                bankroll = bankroll - bet_amount
        elif game_tied:
            print("Its a tie")
        else:
            game_player.add_money(bet_amount)
            print("You won ", bet_amount)
            bankroll = bankroll + bet_amount

        print("You're balance is : ", bankroll)

        print("\nDo you want to play again?")
        if input("y for yes, n for no :")[0] == "y":
            if bankroll == 0:
                print("You don't the money kid! Get lost!")
                break
        else:
            if init_bankroll - bankroll > 0:
                print("The House always wins!")
            elif init_bankroll == bankroll:
                print("You can only win and the house can't lose. It's a tie kid.")
            else:
                print("You got us this time!")
            break

if __name__ == "__main__":
    start_game()
