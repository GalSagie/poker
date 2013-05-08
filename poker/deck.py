__author__ = 'woodruff'

"""
    Deck of cards, contains 52 cards.

    Implemented as a list of 52 objects , each index in the list represent a card type and rank (0..51)
    (The encoding from number to card can be seen in card.py)

    each object in the list indicate if the card is currently in the deck or it is missing (was dealt to someone)
    (currently the object can be boolean)

    There is a 'seed' parameter which is used to shuffle and deal random card from the deck

"""

import random
import card

class Deck:

    def __init__(self):
        self.cards = [True for x in range(0,52)]
        self.seed = 0
        self.deck_cards_dealt_counter = 52;

    def shuffle(self):
        for card in self.cards:
            card = True
        self.deck_cards_dealt_counter = 52;

    def deal_card(self):
        return card.Card(self.get_card())

    def get_card(self):
        if self.deck_cards_dealt_counter == 0:
            raise Exception("Deck Empty")
        self.deck_cards_dealt_counter = self.deck_cards_dealt_counter - 1

        card_num = random.randint(0,51)
        if (self.cards[card_num] == False):
            return self.find_different_card(card_num)
        else:
            self.cards[card_num] = False
            return card_num

    def find_different_card(self,card_num):
        for index in range(card_num,len(self.cards)):
            if self.cards[index] == True:
                self.cards[index] = False
                return index

        for index in range(0,card_num):
            if self.cards[index] == True:
                self.cards[index] = False
                return index

    def deal_2_cards(self):
        c1 = self.deal_card()
        c2 = self.deal_card()
        return c1,c2