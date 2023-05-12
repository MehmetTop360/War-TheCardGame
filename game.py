import random

card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
}

def initialize_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

class Player:
    def __init__(self):
        self.deck = []

    def draw_card(self):
        return self.deck.pop(0)

    def add_cards(self, cards):
        self.deck.extend(cards)

def distribute_cards(deck, player1, player2):
    player1.deck = deck[:26]
    player2.deck = deck[26:]
def play_round(player1, player2):
    card1 = player1.draw_card()
    card2 = player2.draw_card()

    print("__________________________________")
    print(f"You draw: {card1[0]} of {card1[1]}")
    print("AI draws a card...")
    print("__________________________________\n")

    if card_values[card1[0]] > card_values[card2[0]]:
        print("\n--------------------------------------")
        print("You win the round!")
        print("--------------------------------------\n")
        player1.add_cards([card1, card2])
    elif card_values[card1[0]] < card_values[card2[0]]:
        print("\n--------------------------------------")
        print("AI wins the round!")
        print("--------------------------------------\n")
        player2.add_cards([card1, card2])
    else:
        print("It's a war!")
        # Issue 3

def main():
    try:
        deck = initialize_deck()
        shuffled_deck = shuffle_deck(deck)

        player1 = Player()
        player2 = Player()

        distribute_cards(shuffled_deck, player1, player2)

        round = 1
        while len(player1.deck) > 0 and len(player2.deck) > 0:
            print(f"\n--------------------------------------")
            print(f"Round {round}")
            print("--------------------------------------")
            play_round(player1, player2)
            input("Press enter to draw a card...\n")
            round += 1

        print("\n--------------------------------------")
        if len(player1.deck) > 0:
            print("Congratulations, you won the game!\n")
        else:
            print("Oh no, AI won the game!\n")
        print("--------------------------------------\n")

    except KeyboardInterrupt:
        print("\nExiting.\n")

if __name__ == "__main__":
    main()