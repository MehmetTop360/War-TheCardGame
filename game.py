import random


class Deck: 
    def __init__(self):
        self._deck = self.initialize_deck()
        
    @property
    def deck(self):
        return self._deck
    
    def initialize_deck(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        deck = [(rank, suit) for suit in suits for rank in ranks]
        return deck
    
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    def distribute_cards(self, player1, player2):
        player1.deck = self.deck[:26]
        player2.deck = self.deck[26:]
    ...

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
    
def main():
    try:
        deck = Deck()
        deck.shuffle_deck()
        player1 = Player()
        player2 = Player()
        deck.distribute_cards(player1, player2)

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

def handle_war(player1, player2):
    face_down_cards = 3

    if len(player1.deck) < face_down_cards + 1 or len(player2.deck) < face_down_cards + 1:
        face_down_cards = min(len(player1.deck) - 1, len(player2.deck) - 1)

    war_pile = []
    for _ in range(face_down_cards):
        war_pile.append(player1.draw_card())
        war_pile.append(player2.draw_card())

    card1 = player1.draw_card()
    card2 = player2.draw_card()

    print(f"\nYou draw: {card1[0]} of {card1[1]}")
    print(f"AI draws: {card2[0]} of {card2[1]}")

    if card_values[card1[0]] > card_values[card2[0]]:
        print("\nYou win the war!")
        player1.add_cards(war_pile + [card1, card2])
    elif card_values[card1[0]] < card_values[card2[0]]:
        print("\nAI wins the war!")
        player2.add_cards(war_pile + [card1, card2])
    else:
        print("The war continues!")
        handle_war(player1, player2)

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
        handle_war(player1, player2)

if __name__ == "__main__":
    main()