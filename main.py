import random



class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def display(self):
        print(f'{self.suit} of {self.value}')


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds","Hearts"]:
            for v in range(1,14):
                self.cards.append(Card(str(v), s))
                # print ("{} of {}".format(v, s))

    def show(self):
        for cards in self.cards:
            cards.display()


    def shuffle(self):
        random.shuffle(self.cards)

    
    def drawCard(self):
        return self.cards.pop(0)
    

class players:
    def __init__(self):
        self.hand = []

    def draw (self, deck):
        self.hand.append(deck.drawCard()) 






deck = Deck()
deck.shuffle()
card = deck.drawCard()
card.display()







