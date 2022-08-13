import random

n = 400 # number of distinct cards
list = [i for i in range(1,n+1)]
pack = 6 #number of cards in one package

X = 1000 #runtimes of Monte Carlo simulation

cost = 0
for i in range(1,X):
    s = set(list)
    while True:
        cards = random.sample(range(1, n+1), pack)
        cost += pack
        s = s - set(cards)
        if len(s) == 0:
            break
    
print(cost/X)

