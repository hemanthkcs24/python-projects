from random import randint
import plotly.express as px
class Die:
    def __init__(self,number_sides=6):
        self.number_sides=number_sides
    def roll(self):
        return randint(1,self.number_sides)
results=[]
die=Die()
for i in range(1000):
    result=die.roll()
    results.append(result)
frequencies=[]
for i in range(1,die.number_sides+1):
    frequency=results.count(i)
    frequencies.append(frequency)
print (frequencies)
poss_results=range(1,die.number_sides+1)
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()



    