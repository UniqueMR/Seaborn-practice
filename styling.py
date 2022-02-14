import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# name & path definition
path = './seaborn-data'
name = 'tips'
full_path = path + '/' + name + '.csv'

# load data
tips_df = pd.read_csv(full_path)

# styling
sns.set_style('darkgrid')
plt.figure(figsize=(10,8))
sns.set_context('paper', font_scale=0.8)

# create & save figure
fig = sns.jointplot(x='total_bill', y='tip', data = tips_df, hue='sex', palette='Blues')
fig.savefig('./figure' + '/' + 'styling' + '.png')