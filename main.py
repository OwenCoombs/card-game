
class Cards:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def display(self):
        print(f'{self.rank} of {self.suit}')
        
your_cards = Cards(3, 'heart')
your_cards.display()
