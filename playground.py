from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# name & path definition
path = './seaborn-data'
name = 'tips'
full_path = path + '/' + name + '.csv'
figsize = (8, 6)

# load data
tips = pd.read_csv(full_path)
print(tips)

# styling
sns.set(rc = {'figure.figsize': figsize})
sns.set_context('paper',font_scale=0.85)

# create figure
fig = sns.lmplot(x='total_bill', y='tip', hue='sex', data=tips, markers=['o','^'], scatter_kws={'s':100, 'linewidth':0.5})

# save figure
fig.savefig('./figure' + '/' + 'lmplot' + '.png')