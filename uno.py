import random
class UnoCard:
    #we create attributes for what a single uno card holds

    def __init__(self, color, number):
        #we initialize the uno card's self, and add a coloer and a number value to it
        self.n = number #self.n is the number attribute
        self.c = color #self.c is the color attribute

    def __str__(self):
        #string representation of the uno card
        return str(self.c + ' ' + str(self.n) + ' ')

    def canPlay(self, other):
        #declares when a card can be played
        if (self.n == other.n) or (self.c == other.c):
            return True
        return False

class UnoDeck:
    #this is a full deck of uno cards, two of each.
    
    def __init__(self):
        #we initialize a list of a new full uno deck
        self.deck = []
        for i in range(2):
            for num in range(1, 10):
                for color in ["Yellow", "Red", "Blue", "Green"]:
                    newcard = UnoCard(color, num)
                    random.shuffle(self.deck)   
                    self.deck.append(newcard)
               
    def is_empty(self):
        return len(self.deck) == 0
  
    def __str__(self):
        #string representation of the unodeck
        return 'An Uno deck with ' + str(len(self.deck)) + ' cards remaining.'
 
    def deal_card(self):
        #returns last card from UnoDeck
        return self.deck.pop()

    def reset_deck(self, pile):
        self.deck = pile.reset_pile()  
        random.shuffle(self.deck)
        
class UnoPile:
    #represents the pile of uno cards on the table
    

    def __init__(self, deck):
        #initializes a new pile by drawing a card from the deck
        card = deck.deal_card()
        self.pile = [card]  # all the cards in the pile


    def __str__(self):
        #string representation of the pile
        return 'The pile has '+str(self.pile[-1])+' on top.'
        
    def top_card(self):
        #prints the card on top of the pile
        return self.pile[-1]

    def add_card(self,card):
        #adds the card to the top of the pile
        self.pile.append(card)


    def reset_pile(self):
        #removes all but the top card from the pile and returns the rest of the cards as a list of UnoCards'''
        newdeck = self.pile[:-1]
        self.pile = [self.pile[-1]]
        return newdeck


class UnoPlayer:

    def __init__(self, name, deck):
        #initializes the unoplayer class. The player has a name and a hand of cards(7cards) that were dealt from the deck
        self.name = name
        self.hand = [deck.deal_card() for i in range(7)]

    def get_name(self):
        #prints the name of the player
        return str(self.name)
    
    def get_hand(self):
        #returns a string representation of the hand, one card per line'''
        output = ''
        for card in self.hand:
            output += str(card) + '\n'
        return output
    
    def has_won(self):
        #returns True if the player's hand is empty (player has won)
        return len(self.hand) == 0
    
    def draw_card(self,deck):
        #draws a card, adds to the player's hand and returns the card drawn
        card = deck.deal_card()  # get card from the deck
        self.hand.append(card)   # add this card to the hand
        return card

    def play_card(self,card,pile):
        #plays a card from the player's hand to the pile
        self.hand.remove(card)
        pile.add_card(card)
   
    def take_turn(self,deck,pile):
		# print player info
        print(self.name+", it's your turn.")
        print(pile)
        print("Your hand: ")
        print(self.get_hand())
		# get a list of cards that can be played
        topcard = pile.top_card()
        matches = [card for card in self.hand if card.canPlay(topcard)]
        if len(matches) > 0:  # can play
            for index in range(len(matches)):
			# print the playable cards with their number
                print(str(index+1) + ": " + str(matches[index]))
			# get player's choice of which card to play
                choice = 0
            while choice < 1 or choice > len(matches):
                choicestr = input("Which do you want to play? ")
                if choicestr.isdigit():
                    choice = int(choicestr)
            self.play_card(matches[choice-1], pile)
        else:  # can't play
            print("You can't play, so you have to draw.")
            input("Press enter to draw.")
			# check if deck is empty -- if so, reset it
			
            if deck.is_empty():
                deck.reset_deck(pile)
			# draw a new card from the deck                
            newcard = self.draw_card(deck)
            print("You drew: "+str(newcard))
            if newcard.canPlay(topcard): # can be played
                print("Good -- you can play that!")
                self.play_card(newcard,pile)
            else:   # still can't play
                print("Sorry, you still can't play.")
                input("Press enter to continue.")
              
def go_to_next_player(deck, pile, playerNum, playerList):
    # Moves to the next player		
    addend = 1
    newPlayerNum = (playerNum + addend)	% len(playerList)
    # Returns the player number
    return (newPlayerNum)    	
           
def play_Uno(numPlayers):
    # set up full deck and initial discard pile
    deck = UnoDeck()
    pile = UnoPile(deck)
    # set up the players
    playerList = []
    for n in range(0, numPlayers):
    # get each player's name, then create an UnoPlayer
        name = input('Player #'+str(n+1)+', enter your name: ')
        playerList.append(UnoPlayer(name,deck))
        currentPlayerNum = int(n+1)
                
    # play the game
    while True:
        for player in playerList:
        # take a turn
            playerList[currentPlayerNum - 1].take_turn(deck,pile)
            
            # check for a winner
            if playerList[currentPlayerNum - 1].has_won():
                print(playerList[currentPlayerNum - 1].get_name()+" wins!")
                print("Thanks for playing!")
                break
                    
            #go to next player
            else:
                currentPlayerNum = go_to_next_player(deck, pile, currentPlayerNum, playerList)    
play_Uno(2)






