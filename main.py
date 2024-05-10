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
        self.build()  # Call the build method to create the deck

    def build(self):
        # Create a standard deck of 52 cards
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(str(v), s))

    def show(self):
        # Display all the cards in the deck
        for card in self.cards:
            card.display()

    def shuffle(self):
        # Shuffle the deck
        random.shuffle(self.cards)

    def drawCard(self):
        # Draw a card from the deck (remove and return the top card)
        return self.cards.pop(0)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []  # Initialize an empty hand for the player

    def draw(self, deck):
        # Draw a card from the deck and add it to the player's hand
        self.hand.append(deck.drawCard())

    def showHand(self):
        hit_input = input("To draw a card type 'hit' ")
        if hit_input.lower() == "hit":
        # Display all the cards in the player's hand
            print(f"{self.name}'s Hand:")
            for card in self.hand:
                card.display()

    def calculateHandValue(self):
        # Calculate the total value of the player's hand
        total_value = 0
        for card in self.hand: # Iterate through each card in the hand
            if card.value.isdigit(): # check if cards value is a digit 2-10
                total_value += int(card.value) # if it is add the number value to the total
            elif card.value in ["Jack", "Queen", "King"]:
                total_value += 10 # if its one of those cards add a value of 10 to it
            elif card.value == "Ace":
                total_value += 11 # if its ace add a value of 11 to it
        return total_value

class Dealer:  
    def __init__(self):
        self.hand = []
    def draw(self, deck):
        # Draw a card from the deck and add it to the player's hand
        self.hand.append(deck.drawCard())

    def showHand(self):
        hit_input = input("To draw a card type 'hit' ")
        if hit_input.lower() == "hit":

        # Display all the cards in the player's hand
            print(f"Dealer's Hand:")
            for card in self.hand:
                card.display()

    def calculateHandValue(self):
        # Calculate the total value of the player's hand
        total_value = 0
        for card in self.hand: # Iterate through each card in the hand
            if card.value.isdigit(): # check if cards value is a digit 2-10
                total_value += int(card.value) # if it is add the number value to the total
            elif card.value in ["Jack", "Queen", "King"]:
                total_value += 10 # if its one of those cards add a value of 10 to it
            elif card.value == "Ace":
                total_value += 11 # if its ace add a value of 11 to it
        return total_value
        
    

       
class start:
    def start_game():
        # start the game
        start_input = input("To start the game, type 'start': ")
        if start_input.lower() == "start":
            # Initialize player and dealer
            player = Player("Player 1")
            dealer = Dealer()

            
            deck = Deck()
            deck.shuffle()

            # Deal cards to player and dealer
            player.draw(deck)
            dealer.draw(deck)
        
        
            # Show hands of player and dealer
            player.showHand()
            dealer.showHand()

            # Calculate hand values
            player_hand_value = player.calculateHandValue()
            dealer_hand_value = dealer.calculateHandValue()

            # Compare hand values to determine the winner
            if player_hand_value > dealer_hand_value:
                print("Player wins!")
                
            elif player_hand_value < dealer_hand_value:
                print("Dealer wins!")
               
            else:
                print("It's a tie!")
                
        else:
            print("Invalid input. Please type 'start' to begin the game.")

# Call the function to start the game
    start_game()








