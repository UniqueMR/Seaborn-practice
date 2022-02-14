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
flights = flights.pivot_table(index='month', columns='year', values='passengers')

# styling
sns.set(rc = {'figure.figsize': figsize})
sns.set_context('paper',font_scale=0.85)

# create & save figure
fig = sns.clustermap(flights, cmap='plasma', standard_scale=1)
fig.savefig('./figure' + '/' + 'clustermap' + '.png')