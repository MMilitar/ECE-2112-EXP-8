import pandas as pd
cars = pd.read_csv('cars.csv')

a = cars.loc[1:10:2] 
b = cars[cars['Model'] == 'Mazda RX4']
c = cars.loc[[23], ['Model', 'cyl']]
d = cars.loc[[1, 28, 18], ['Model', 'cyl', 'gear']]

print(a,'\n')
print(b,'\n')
print(c,'\n')
print(d,'\n')