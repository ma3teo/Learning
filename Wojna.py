import random

colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace', 'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10', 'Power': 10},
    {'Figure': '9', 'Power': 9}]

allCards = []

for color in colors:
    for figure in figures:
        aCard = figure.copy()
        aCard['Color'] = color
        allCards.append(aCard)

random.shuffle(allCards)

player1 = []
player2 = []
maxCardQuantity = len(allCards)

for i in range(maxCardQuantity):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])

rounds = 0
war = 0
stock = []

while len(player1) != 0 and len(player2) != 0 and rounds < 500:
    rounds += 1
    print(len(player1))
    print(len(player2))
    print('''
    *************
    * %4d ROUND*
    *************
    ''' % (rounds))
    print(player1)
    print(player2)
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    print('Player1 has got: %s - %s' % (p1['Figure'], p1['Color']))
    print('Player2 has got %s - %s' % (p2['Figure'], p2['Color']))
    if p1['Power'] > p2['Power']:
        player1.append(p1)
        player1.append(p2)
        print('Player1 win this round')
        print('--------------------------------------')
    elif p1['Power'] < p2['Power']:
        player2.append(p2)
        player2.append(p1)
        print('Player2 win this round')
        print('--------------------------------------')
    elif p1['Power'] == p2['Power'] and len(player2) <= 1:
        print('Last war is over, Player1 wins')
        player1.append(p1)
        player1.append(p2)
    elif p1['Power'] == p2['Power'] and len(player1) <= 1:
        print('Last war is over, Player2 wins')
        player2.append(p2)
        player2.append(p1)
    elif p1['Power'] == p2['Power'] and len(player1) > 0 and len(player2) > 0:
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        stock.append(p1)
        stock.append(p2)
        stock.append(player1.pop(0))
        stock.append(player2.pop(0))
        card1 = p1.copy()
        card2 = p2.copy()
        while card1['Power'] == card2['Power']:
            war += 1
            card1 = player1.pop(0)
            card2 = player2.pop(0)
            stock.append(card1)
            stock.append(card2)
            if card1['Power'] > card2['Power']:
                print('Player1 has got: %s - %s' % (card1['Figure'], card1['Color']))
                print('Player2 has got %s - %s' % (card2['Figure'], card2['Color']))
                print('The war was win by Player1')
                print('###################################')
                player1.extend(stock.copy())
                stock.clear()
            elif card1['Power'] < card2['Power']:
                print('Player1 has got: %s - %s' % (card1['Figure'], card1['Color']))
                print('Player2 has got %s - %s' % (card2['Figure'], card2['Color']))
                print('The war was win by Player2')
                print('###################################')
                player2.extend(stock.copy())
                stock.clear()
            elif len(player1) == 0:
                print('Player1 has no more cards in stock')
                player2.extend(stock.copy())
                stock.clear()
            elif len(player2) == 0:
                print('Player2 has no more cards in stock')
                player1.extend(stock.copy())
                stock.clear()
            else:
                print('Player1 has got: %s - %s' % (card1['Figure'], card1['Color']))
                print('Player2 has got %s - %s' % (card2['Figure'], card2['Color']))
                print('War continue')
                print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
    else:
        break



if len(player2) == 0:
    print('The winner is: Player1 and he win in: %i round' % (rounds))
elif len(player1) == 0:
    print('The winner is: Player1 and he win in: %i round' % (rounds))
else:
    print('Draw after', rounds, 'rounds')

print("Player1 deck", player1, '\ndeck volume:', len(player1))
print('Player2 deck', player2, '\ndeck volume:', len(player2))