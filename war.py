# Write your code here :-)
from cards import *
from collections import Counter
ntrials = 1000
differential = []
for i in range(ntrials):
    adeck = deck()
    adeck.shuffle()
    bdeck = deck()
    bdeck.shuffle()
    ascore = 0
    bscore = 0
    while adeck.cardsleft() > 0:
        acard = adeck.dealcard()
        bcard = bdeck.dealcard()
        if acard.value() > bcard.value():
            ascore += 2
        if bcard.value() > acard.value():
            bscore += 2
        else:
            ascore += 1
            bscore += 1
    differential.append((abs(ascore-bscore)))


counts = Counter(differential)
for key in sorted(counts.keys()):
    print("%2d %8.2f" %(key,counts[key]/ntrials))