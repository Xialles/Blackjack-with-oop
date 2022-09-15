import random

# CLASS DEFINTIONS:

class Deck:
    # Creates the deck of cards
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "jack", "queen", "king", "ace"]
    suits = ["spades", "hearts", "diamonds", "clubs"]
    values = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "jack": 10,
        "queen": 10,
        "king": 10,
        "ace": 11,
    }

    def __init__(self):
        self.deck_cards = []
        self.deck_values = {}

    def create_card(self, rank, suit):
        # return a string with the cards rank and suit
        self.rank = rank
        self.suit = suit
        return self.rank + "_of_" + self.suit

    def create_deck(self, number_of_decks=1):
        # creates the deck of cards, optional input number_of_decks, standard =1
        for rank in Deck.ranks:
            for suit in Deck.suits:
                self.deck_cards.append(Deck.create_card(self, rank, suit))
                self.deck_values[(Deck.create_card(self, rank, suit))] = Deck.values[rank]
        for _ in range(1, number_of_decks):  # create multiple decks
            self.deck_cards += self.deck_cards
        # print(self.deck)
        # print(self.deck_values)
        
    
    def shuffle_cards(self):
        random.shuffle(self.deck_cards)
    
    
def main():
    # programs entry point
    
    # This works
    playing_deck1 = Deck()
    playing_deck1.create_deck()
    print(playing_deck1.deck_cards)
    print('\n')
    
    # This does not work 
    playing_deck2 = Deck().create_deck() # This does not trigger an error
    print(playing_deck2) # This prints None
    print(playing_deck2.deck_cards) # Therefor this will not work and creates an error
    print('\n') 
            
if __name__ == "__main__":
    main()
