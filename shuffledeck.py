import itertools, random
deck=list(itertools.product(range(1,14),['spade','Heart','Diamond','club','round']))
random.shuffle(deck)
print("you got:")
for i in range(8):
    print(deck[i][0],"of",deck[i][1])