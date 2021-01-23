import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

file  = "list_WB_Data.csv"

data = pd.read_csv(file)
data = data.drop(columns = ['Unnamed: 4'])
print(data)
series = set(data['Series Name'])

table = pd.pivot_table(data, index = ["Country Name", "Time"],
                       columns = "Series Name",
                       values = "Value")

table = table.drop(index = '5=best)', level = 0)
plt.figure(figsize= (10,8))
sns.lineplot(data = table[table.index.get_level_values('Country Name') != 'United Kingdom'],
             x = 'Population, total',
             y = 'Electric power consumption (kWh per capita)', 
             hue = 'Country Name')


plt.xscale('log')
plt.yscale('log')
plt.tight_layout()

uk=table[table.index.get_level_values('Country Name') == 'United Kingdom']
#table['country'] = table.index.get_level_values('Country Name')
sns.pairplot(data = uk,
             x_vars= [ "Population, total", "Electric power consumption (kWh per capita)"],
             y_vars = ['CO2 emissions (kt)', 'Forest area (sq. km)'],
             height=8, aspect=1.2, kind="reg")


plt.show()