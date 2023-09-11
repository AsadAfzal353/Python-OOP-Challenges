
from random import choice

class PlayingCard:
    def __init__(self, suit, rank):
        self.suit = suit.lower()
        self.rank = rank.lower()

    def __iter__(self):
        return self
    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise AttributeError("The instances cannot be compared")
        return self.suit == other.suit and self.rank == other.rank
    
    def __hash__(self):
        return (self.suit, self.rank)
    
    def __repr__(self):
        return f"{self.__class__.__name__}(suit='{self.suit}', rank='{self.rank}')"
    
class CardDeck:
    SUITS = ['clubs', 'diamonds', 'hearts', 'spades']
    RANKS = ['a', '2', '3', '4',
            '5', '6', '7', '8',
            '9', '10', 'j', 'q', 'k']
    
    def __init__(self, cards=None):
        self.cards = self._validate_cards(cards)
        self.all_cards = []
        self._combinations()
    
    def __getitem__(self, key):
        if type(key) == slice: # returns instances
            return self.__class__([*self.all_cards[key]])
        
        elif type(key) == int:
            return self.all_cards[key] # return the Animal subclass in that position
        
        return NotImplemented
    
    def __repr__(self):
        return f"{self.__class__.__name__}(cards='{[card for card in self.all_cards]}')"
    
    def __len__(self):
        return len(self.all_cards)
    
    def __add__(self, item):
        self.new = []
        self.new.append(self.all_cards)
        self.new.append(item)
        return self.new
    
    def __radd__(self, item):
        return self + item
    
    def __mul__(self, item):
        self.new = []
        for i in range(item):
            self.new.append(self.all_cards)
        return self.new
    
    def __rmul__ (self, item):
        return self*item
    
    def draw(self, number=1):
        if number == 1:
            card = choice(self.all_cards)
            self.all_cards.remove(card)
            return card
        else:
            self.new = []
            for _ in range(number):
                card = choice(self.all_cards)
                self.all_cards.remove(card)
                self.new.append(card)
            return CardDeck(self.new)

    def add(self, item):
        return self.all_cards.append(item)

    def _validate_cards(self, cards):
        if cards:
            temp = []
            for card in cards:
                if type(card) == PlayingCard:
                    if card.rank.lower() in self.RANKS and card.suit.lower() in self.SUITS:
                        temp.append(card)
                        
            if temp == []: return None
            else: return temp
        else:
            return None

    def _combinations(self):
        if self.cards:
            for card in self.cards:
                self.add(card)
        else:
            for suit in self.SUITS:
                for rank in self.RANKS:
                    self.add(PlayingCard(suit, rank))


if __name__ == "__main__":

    cd = CardDeck()
    cd2 = CardDeck(cards=[PlayingCard('diamonds', '2')])
    cd3 = CardDeck(cards=["Andrew", PlayingCard('clubs', '7')])
    cd4 = CardDeck(cards=["Andrew", "Lisa"])

    len(cd), len(cd2), len(cd3), len(cd4)
    # 52 1 1 52

    cd[1] # indexing
    PlayingCard(suit='spades', rank='j')

    cd[-10:]
    # CardDeck(cards=[PlayingCard(suit='hearts', rank='q'), PlayingCard(suit='hearts', rank='2'), PlayingCard(suit='hearts', rank='3'), PlayingCard(suit='hearts', rank='4'), PlayingCard(suit='hearts', rank='5'), PlayingCard(suit='hearts', rank='6'), PlayingCar...

    PlayingCard('spADes', 'J') in cd # True

    # Concatenation should be supported using the + operator
    cd2 + PlayingCard('spades', '6') # CardDeck(cards=[PlayingCard(suit='diamonds', rank='2'), PlayingCard(suit='spades', rank='6')])

    cd2 + cd3  # between two Decks
    # CardDeck(cards=[PlayingCard(suit='diamonds', rank='2'), PlayingCard(suit='clubs', rank='7')])

    # and should be commutative
    PlayingCard('spades', '6') + cd3
    # CardDeck(cards=[PlayingCard(suit='clubs', rank='7'), PlayingCard(suit='spades', rank='6')])

    # commutatively, duplicating CardDecks using '*' operator
    cd2 * 3 # CardDeck(cards=[PlayingCard(suit='diamonds', rank='2'), PlayingCard(suit='diamonds', rank='2'), PlayingCard(suit='diamonds', rank='2')])

    3 * cd2
    # CardDeck(cards=[PlayingCard(suit='diamonds', rank='2'), PlayingCard(suit='diamonds', rank='2'), PlayingCard(suit='diamonds', rank='2')])

    # iteration
    for card in 3 * cd2:
        print(card)
    # PlayingCard(suit='diamonds', rank='2')
    # PlayingCard(suit='diamonds', rank='2')
    # PlayingCard(suit='diamonds', rank='2')

    # drawing a single card randomly -> PlayingCard
    len(cd) # 52

    cd.draw() # PlayingCard(suit='spades', rank='4')

    len(cd) # 51

    # drawing more than 1 card at a time -> CardDeck
    print(cd.draw(4)) # CardDeck(cards=[PlayingCard(suit='diamonds', rank='5'), PlayingCard(suit='clubs', rank='k'), PlayingCard(suit='diamonds', rank='8'), PlayingCard(suit='hearts', rank='7')])

    print(type(cd.draw(4))) # <class '__main__.CardDeck'>

    print(len(cd)) # 43

    PlayingCard('spADes', '6') == PlayingCard('spades', '6')
    # True