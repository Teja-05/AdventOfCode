import collections
from collections import defaultdict
from operator import itemgetter

with open('camelcard.txt', 'r') as f:
    ip = f.read()

l = ip.split('\n')

total = 0
order = ['High card','One pair','Two pair','Three of a kind','Full house','Four of a kind','Five of a kind']
cardtype = []

for line in l:
    hand, bid = line.split(' ')[0], line.split(' ')[1]
    c = collections.Counter(hand)

    #identify card type
    if len(c.keys())==1:
        cardtype.append(['Five of a kind',hand])
    elif sorted(c.values())==[1,4]:
        cardtype.append(['Four of a kind',hand])
    elif sorted(c.values())==[2,3]:
        cardtype.append(['Full house',hand])
    elif sorted(c.values())==[1,1,3]:
        cardtype.append(['Three of a kind',hand])
    elif sorted(c.values())==[1,2,2]:
        cardtype.append(['Two pair',hand])
    elif sorted(c.values())==[1,1,1,2]:
        cardtype.append(['One pair',hand])
    elif len(c.keys())==5:
        cardtype.append(['High card',hand])

x = sorted(cardtype,key=itemgetter(0))
res = defaultdict(list)

for i in x:
    res[i[0]].append(i[1]) #group cards with similar type

temp = dict(res)

strength = "AKQJT98765432"
for k, v in temp.items():
    if len(v)>=2:
        v.sort(key=lambda x: [strength.index(card[0]) for card in x], reverse=True) #sort the hands by strength 

#sort the card types from strongest to weakest
sorted_keys = sorted(temp.keys(), key=lambda x: order.index(x))
d = {key: temp[key] for key in sorted_keys}

hands = []
for v in d.values():
    hands.append(v)

arr = []
for sublist in hands:
    for e in sublist:
        arr.append(e) #contains all hands arranged by their rank

for line in l:
    hand, bid = line.split(' ')[0], line.split(' ')[1]
    rank = arr.index(hand)+1
    total += rank*int(bid)

print(total)
