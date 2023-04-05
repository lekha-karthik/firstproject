import itertools, random
deck=list(itertools.product(range(1,14),['spade','Heart','Diamond','club',]))
random.shuffle(deck)
print("player 1 got:");
for i in range(13):
    print(deck[i][0],"of",deck[i][1])
random.shuffle(deck)    
print("player 2 got:")
for i in range(13):
    print(deck[i][0],"of",deck[i][1])