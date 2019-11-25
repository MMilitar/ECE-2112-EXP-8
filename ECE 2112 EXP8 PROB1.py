import pandas as pd
cars = pd.read_csv('cars.csv')
head = cars.head()
tail = cars.tail()
print(head)
print(tail)