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

# # type A
# tips_g = sns.FacetGrid(tips, col='time', row='smoker')
# tips_g = tips_g.map(plt.scatter, 'total_bill', 'tip')

# type B
tips_g = sns.FacetGrid(tips, col='time', hue='smoker', height=4, aspect=1.3, col_order=['Dinner','Lunch'], palette='Set1', hue_order=['Yes','No'])
tips_g = tips_g.map(plt.scatter, 'total_bill', 'tip', edgecolor='w')

# save figure
tips_g.savefig('./figure' + '/' + 'facetgrid1' + '.png')