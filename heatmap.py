from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# name & path definition
path = './seaborn-data'
name = 'car_crashes'
full_path = path + '/' + name + '.csv'
figsize = (8, 6)

# load data
crash_df = pd.read_csv(full_path)
crash_mx = crash_df.corr()
print(crash_mx)

# styling
sns.set(rc = {'figure.figsize': figsize})
sns.set_context('paper',font_scale=0.85)

# create & save figure
fig = sns.heatmap(data = crash_mx, annot=True, cmap='plasma')
fig = fig.get_figure()
fig.savefig('./figure' + '/' + 'heatmap' + '.png')