from enum import Enum

class HandType(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIRS = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9
    ROYAL_FLUSH = 10
    
class Hand:
    def __init__(self, hT, c1 = None, c2 = None, c3 = None, c4 = None, c5 = None, hP = None, lP = None, tp = None, qp = None):
        self.handType = hT
        self.card1 = c1
        self.card2 = c2
        self.card3 = c3
        self.card4 = c4
        self.card5 = c5
        self.highPair = hP
        self.lowPair = lP
        self.triplet = tp
        self.quadruplet = qp
        
cardsDict = {'1' : 1, '2' : 2, '3' : 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9, 'T' : 10, 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
    
    
def identifyHand(H):
    flush = True
    for i in range(1, len(H)):
        if H[i][1] != H[0][1]:
            flush = False
            break
            
    cards = []
    for i in range(len(H)):
        cards += [cardsDict[H[i][0]]]
        
    cards.sort()
    
    ### FLUSHes ###
    if flush:
        if cards[-1] - cards[0] == 4:                   # flush
            if cards[-1] == 14:                         # royal flush
                return Hand(HandType.ROYAL_FLUSH)
            
            return Hand(HandType.STRAIGHT_FLUSH, c1 = cards[-1])
        
        elif 14 in cards and 2 in cards:
            endCard = 2
            count = 2
            d = 1
            while 14 - d in cards:
                count += 1
                d += 1
            
            d = 1
            while 2 + d in cards:
                count += 1
                endCard = 2 + d
            
            if count == 5:
                return Hand(HandType.STRAIGHT_FLUSH, c1 = endCard)
        
        return Hand(HandType.FLUSH, c1 = cards[-1], c2 = cards[-2], c3 = cards[-3], c4 = cards[-4], c5 = cards[-5])
    
    ####
    cardCounts = [0 for i in range(15)]
    for c in cards:
        cardCounts[c] += 1
    
    quadruplet = 0
    triplet = 0
    highPair = 0
    lowPair = 0
    
    ### FOUR, FULLHOUSE ###
    for j in range(1, 15):
        if cardCounts[j] == 4:
            quadruplet = j
            break
        if cardCounts[j] == 3:
            triplet = j
        if cardCounts[j] == 2:
            if highPair == 0:
                highPair = j
            else:
                lowPair = j
    
    if highPair < lowPair:
        highPair, lowPair = lowPair, highPair
    
    if quadruplet != 0:
        card1 = filter(lambda a: a != quadruplet, cards)
        return Hand(HandType.FOUR_OF_A_KIND, c1 = card1[0], qp = quadruplet)
    
    if triplet != 0 and highPair != 0:
        return Hand(HandType.FULL_HOUSE, hP = highPair, tp = triplet)
    
    ### STRAIGHT ###
    straight = True
    if cards[-1] - cards[0] == 4:
        for d in range(1, 4):
            if cards[0] + d not in cards:
                straight = False
                break
        
        if straight:
            return Hand(HandType.STRAIGHT, c1 = cards[-1])
        
    elif 2 in cards and 14 in cards:
        endCard = 2
        count = 2
        d = 1
        while 14 - d in cards:
            count += 1
            d += 1
        
        d = 1
        while 2 + d in cards:
            count += 1
            endCard = 2 + d
            d += 1
        
        if count == 5:
            return Hand(HandType.STRAIGHT_FLUSH, c1 = endCard)
    
    ####
    
    if triplet != 0:
        remCards = list(filter(lambda a: a != triplet, cards))
        remCards.sort()
        return Hand(HandType.THREE_OF_A_KIND, c1 = remCards[-1], c2 = remCards[-2], tp = triplet)
    
    if highPair != 0 and lowPair != 0:
        remCards = filter(lambda a: a != highPair, cards)
        remCards = list(filter(lambda a: a != lowPair, remCards))
        return Hand(HandType.TWO_PAIRS, c1 = remCards[0], hP = highPair, lP = lowPair)
    
    if highPair != 0:
        remCards = list(filter(lambda a: a != highPair, cards))
        remCards.sort()
        return Hand(HandType.ONE_PAIR, c1 = remCards[-1], c2 = remCards[-2], c3 = remCards[-3], hP = highPair)
    
    return Hand(HandType.HIGH_CARD, c1 = cards[-1], c2 = cards[-2], c3 = cards[-3], c4 = cards[-4], c5 = cards[-5])
    
def compareHands(h1, h2):
    if h1.handType.value > h2.handType.value:
        return 1
    
    if h1.handType.value < h2.handType.value:
        return 2
    
    if h1.handType == HandType.STRAIGHT_FLUSH:
        if h1.card1 > h2.card1:
            return 1
        return 2
    
    if h1.handType == HandType.FOUR_OF_A_KIND:
        if h1.quadruplet > h2.quadruplet:
            return 1
        if h1.quadruplet < h2.quadruplet:
            return 2
        if h1.card1 > h2.card1:
            return 1
        return 2
    
    if h1.handType == HandType.FULL_HOUSE:
        if h1.triplet > h2.triplet:
            return 1
        if h1.triplet < h2.triplet:
            return 2
        if h1.highPair > h2.highPair:
            return 1
        return 2
    
    if h1.handType == HandType.FLUSH:
        if h1.card1 > h2.card1:
            return 1
        if h1.card1 < h2.card1:
            return 2
        
        if h1.card2 > h2.card2:
            return 1
        if h1.card2 < h2.card2:
            return 2
            
        if h1.card3 > h2.card3:
            return 1
        if h1.card3 < h2.card3:
            return 2
            
        if h1.card4 > h2.card4:
            return 1
        if h1.card4 < h2.card4:
            return 2
            
        if h1.card5 > h2.card5:
            return 1
        return 2
        
    if h1.handType == HandType.STRAIGHT:
        if h1.card1 > h2.card1:
            return 1
        return 2
    
    if h1.handType == HandType.THREE_OF_A_KIND:
        if h1.triplet > h2.triplet:
            return 1
        if h1.triplet < h2.triplet:
            return 2
        
        if h1.card1 > h2.card1:
            return 1
        if h1.card1 < h2.card1:
            return 2
        
        if h1.card2 > h2.card2:
            return 1
        return 2
    
    if h1.handType == HandType.TWO_PAIRS:
        if h1.highPair > h2.highPair:
            return 1
        if h1.highPair < h2.highPair:
            return 2
            
        if h1.lowPair > h2.lowPair:
            return 1
        if h1.lowPair < h2.lowPair:
            return 2
        
        if h1.card1 > h2.card1:
            return 1
        return 2
    
    if h1.handType == HandType.ONE_PAIR:
        if h1.highPair > h2.highPair:
            return 1
        if h1.highPair < h2.highPair:
            return 2
            
        if h1.card1 > h2.card1:
            return 1
        if h1.card1 < h2.card1:
            return 2
        
        if h1.card2 > h2.card2:
            return 1
        if h1.card2 < h2.card2:
            return 2
            
        if h1.card3 > h2.card3:
            return 1
        return 2
    
    if h1.card1 > h2.card1:
        return 1
    if h1.card1 < h2.card1:
        return 2
    
    if h1.card2 > h2.card2:
        return 1
    if h1.card2 < h2.card2:
        return 2
        
    if h1.card3 > h2.card3:
        return 1
    if h1.card3 < h2.card3:
        return 2
        
    if h1.card4 > h2.card4:
        return 1
    if h1.card4 < h2.card4:
        return 2
        
    if h1.card5 > h2.card5:
        return 1
    return 2
    
def problem54():
    c = 0
    f = open('p054_poker.txt', 'r')
    for l in f:
        L = l.split(' ')
        w = compareHands(identifyHand(L[:5:]), identifyHand(L[5::]))
        if w == 1:
            c += 1
    
    f.close()
    return c
