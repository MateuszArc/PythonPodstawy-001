colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
        {'Figure':'Ace',  'Power':14},
        {'Figure':'King', 'Power':13},
        {'Figure':'Queen', 'Power':12},
        {'Figure':'Jack', 'Power':11},
        {'Figure':'10',   'Power':10},
        {'Figure':'9',    'Power':9}]

allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Colour'] = c
        allCards.append(aCard)
import random
random.shuffle(allCards)
player1 = []
player2 = []
player1.append(allCards[:12])
player2.append(allCards[12:])
print("-----------PLAYER1------------")
print(player1)
print("-----------PLAYER2------------")
print(player2)

while len(player1) > 0 or len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1["Power"] == card2["Power"]:
            player1.append(card1)
            player2.append(card2)
        elif card1["Power"] > card2["Power"]:
            player1.append(card2)
            player1.append(card1)
        else:
            player2.append(card1)
            player2.append(card2)

if player2 == 0:
    print("PLAYER1 WON")
else:
    print("PLAYER2 WON")