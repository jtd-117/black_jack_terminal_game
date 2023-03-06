# @file	    black_jack.py
# @author   Jude Thaddeau Data
# @note     GitHub: https://github.com/jtd-117
# ---------------------------------------------------------------------------- #

# MISCELLANEOUS VARIABLES & LIBRARIES

from random import shuffle

INVALID = "\nINVALID INPUT."
BORDER = "# ---------------------------------------------------------------------------- #"

BROKE = 0
ACEVALUE1 = 1
ACEVALUE2 = 11
RISKYBOUNDARY = 17
BLACKJACK = 21

suites = {
    'Spades': '♠︎',
    'Clubs': '♣︎',
    'Hearts': '♥︎',
    'Diamonds': '♦︎'
}

ranks = {
    'Ace': (1,11),
    'Two': 2, 
    'Three': 3, 
    'Four': 4, 
    'Five': 5, 
    'Six': 6, 
    'Seven': 7, 
    'Eight': 8, 
    'Nine': 9, 
    'Ten': 10, 
    'Jack': 10, 
    'Queen':10, 
    'King': 10
}

symbols = {
    'Ace': 'A ', 
    'Two': '2 ', 
    'Three': '3 ', 
    'Four': '4 ', 
    'Five': '5 ', 
    'Six': '6 ', 
    'Seven': '7 ', 
    'Eight': '8 ', 
    'Nine': '9 ', 
    'Ten': '10', 
    'Jack': 'J ', 
    'Queen': 'Q ', 
    'King': 'K '
}

stand_hit = ['s','h']
yes_no = ['y','n']

# ---------------------------------------------------------------------------- #

class Card(object):
        """
        An INTERFACE for a card from a standard 52-card deck.
        """

        def __init__(self, suite, rank):
                """
                Initialises a standard playing card.

                :Parameters:
                        - `suite`: the TYPE of card taken from the `suites` dictionary
                        - `rank`: the NUMBER of the card taken from the `ranks` dictionary
                """
                self.suite = suite
                self.rank = rank
                self.value = ranks[self.rank]
                self.image = symbols[self.rank]

        def __str__(self):
                """
                Prints out the rank & suite of the card.
                """
                return self.rank + ' of ' + self.suite

# ---------------------------------------------------------------------------- #

class Deck(object):
        """
        An INTERFACE for a standard 52-card deck.
        """

        def __init__(self):
                """
                Initialises a standard 52-card deck.
                """
                self.all_cards = []
                
        def new_deck(self):
                """
                Initialises & shuffles a new deck of cards.
                """

                # STEP 1: Create new deck
                print("\nCreating new deck...")
                for suite in suites.keys():
                        for rank in ranks.keys():
                                self.all_cards.append(Card(suite, rank))

                # STEP 2: Shuffle deck
                print("\nShuffling deck...")
                shuffle(self.all_cards)
                return self.all_cards

        def delete_deck(self):
                """
                Deletes a deck of cards.
                """
                
                print("\nResetting deck...")
                self.all_cards = []

# ---------------------------------------------------------------------------- #