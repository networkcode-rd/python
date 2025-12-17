import random

suits = ("Hearts","Diamonds","Spades","Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

playing = True

# Card Class

class card:

    def __init__(self,suit,rank):
        self.suit_a = suit
        self.rank_a = rank

    def __str__(self):
        return self.rank_a + " of " + self.suit_a

# Deck Class
class deck:

    def __init__(self):
        self.deck = []
        for suit_x in suits:
            for rank_y in ranks:
                self.deck.append(card(suit_x, rank_y))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n" + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


# Hand class
class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank_a]

        if card.rank_a == "Ace":
            self.aces += 1

    def adjust_value_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        

# test_deck = deck()
# test_deck.shuffle()

# test_player = Hand()
# pulled_card = test_deck.deal()
# print(pulled_card)

# test_player.add_card(pulled_card)
# print(test_player.value)

# Chips Class

class Chips:

    def __init__(self,total=100):
        self.total = total

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


# Taking Bet:-

def take_bet(Chips):

    while True:

        try:
            Chips.bet = int(input("How many chips would you like to bet? Insert a number: "))
        except ValueError:
            print("Sorry please provide an integer")

        else:
            if Chips.bet > Chips.total:
                print(f"Sorry you do not have enough chips. You have {Chips.total}")
            else:
                break


# Take hit

def hit(deck,Hand):
    
    single_card = deck.deal()
    Hand.add_card(single_card)
    Hand.adjust_value_ace()

# Prompt player to Hit or Stand:

def hit_or_stand(deck,Hand):

    global playing

    while True:

        x = input("Hit or Stand? Enter 'h' or 's': ")

        if x[0].lower() == 'h':
            hit(deck,Hand)
        elif x[0].lower() == 's':
            print("Player chose to Stand, Dealer's turn.")
            playing = False

        else:
            print("Wrong input. Please provide value for Hit or Stand. Example: 'h' or 's'. ")
            continue
        break

# Display Cards

def show_some(player,dealer):


    # dealer.cards[0]

    #show only one of the dealer's card
    print("\n Dealer's Hand: ")
    print("First card hidden.")
    print(dealer.cards[1])

    # show all cards of the player
    print("\n Player's Hand: ")
    for p_cards in player.cards:
        print(p_cards)



def show_all(player,dealer):

    # show all dealer's card
    # calculate the card value.
    print("\n Dealer's Hand:  ")
    for d_cards in dealer.cards:
        print(d_cards)

    print(f"Value of Dealer's hand is: {dealer.value}")


    # show all the player card
    # calculate the card value.
    print("\n Player's Hand: ")
    for p_cards in player.cards:
        print(p_cards)

    print(f"Value of Player's hand is: {player.value}")


# Game scenarios

def player_busts(player,dealer,Chips):
    print("Bust player.")
    Chips.lose_bet()


def player_wins(player,dealer,Chips):
    print("Player Wins!")
    Chips.win_bet()


def dealer_busts(player,dealer,Chips):
    print("Player Wins. Dealer Busted")
    Chips.win_bet()


def dealer_wins(player,dealer,Chips):
    print("Dealer Wins.")
    Chips.lose_bet()


def push(player,dealer):
    print("Dealer and Player tie.")


# Playing Game # Setting up player chips

player_chips = Chips()

while True:
    playing = True
    print("Welcome to Black Jack Game!")

    # Create and shuffle the deck, deal two cards to each player.
    game_deck = deck()
    game_deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(game_deck.deal())
    player_hand.add_card(game_deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(game_deck.deal())
    dealer_hand.add_card(game_deck.deal())
    
    if player_chips.total <= 0:
        print("You are out of chips. Game over!")
        break
    
    print(f"\nYou have {player_chips.total} chips.")

    # prompting player for their bet
    take_bet(player_chips)

    # show cards while keeping the dealer card hidden.
    show_some(player_hand, dealer_hand)

    while playing:
        # prompting player for hit or stand
        hit_or_stand(game_deck,player_hand)

        # dealer card, show some only
        show_some(player_hand,dealer_hand)

        # if player total > 21.
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        
        # If player is still on the game, not buested, Dealer will play until dealer reaches 17
        if not playing and player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(game_deck,dealer_hand)
            
            show_all(player_hand,dealer_hand)

            # If Dealer > 21 then dealer Bust.
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)
            break
        
        # Update the player of their chips total-
        print(f"\n Player total chips are at: {player_chips.total}")

        # Prompt player if they would like to continue-
        new_game = input("Would you like to play another hand?Type y/n: ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("That was an interesting game!")
            break
        