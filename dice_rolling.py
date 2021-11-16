import random
from collections import Counter
import numpy as np

#use numpy to generate the sides of the die btn 0&6
sides = np.arange(1/6, 1, 1/6, dtype= float)

#round of the die sides to 3 d.p
roll = np.round(sides, 4).tolist()

#create empty list to store our outcomes of the rolled dice

results=[]

# roll the dice 1000 times
for i in range(1000):
    outcome = random.choice(roll)
    results.append(outcome)

#use collections counter to take frequency of our outcomes and store to a dict
tally= Counter(results)
sort_dict= dict(sorted(tally.items()))
#print our outcomes in a neat format
print('FACE','   FREQUENCY',' PERCENTAGE')
print('=============================')
for key, value in sort_dict.items():
    percentage = ((value/1000)*100)
    percentage = str(round(percentage, 2))
    print('{:<10} {:<7} {:<1}'.format(key, value, str(percentage)+"%"))

totals= sum(sort_dict.values())
total_P= (totals/1000)*100
print('=============================')
print('Total=    ',totals,'  ', total_P,'%')
