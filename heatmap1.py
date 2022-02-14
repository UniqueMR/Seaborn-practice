from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# name & path definition
path = './seaborn-data'
name = 'flights'
full_path = path + '/' + name + '.csv'
figsize = (8, 6)

# load data
flights = pd.read_csv(full_path)
print(flights)
flights = flights.pivot_table(index = 'month', columns = 'year', values='passengers')
print(flights)

# styling
sns.set(rc = {'figure.figsize': figsize})
sns.set_context('paper',font_scale=0.85)

# create & save figure
fig = sns.heatmap(data = flights, annot=False, cmap='plasma', linecolor='white', linewidths=1)
fig = fig.get_figure()
fig.savefig('./figure' + '/' + 'heatmap1' + '.png')