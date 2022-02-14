import csv
from random import randrange, uniform

list = [[randrange(3000, 5001), f"{uniform(8, 20):.1f}"] for _ in range(100)]
list.insert(0, ['Weight_in_lbs', 'Acceleration'])

with open('weight.csv', 'w') as f:
    csv.writer(f).writerows(list)
