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

# create & save figure
fig = sns.stripplot(x='day', y='total_bill', data = tips_df, hue='sex', jitter=False, dodge=True)
fig = fig.get_figure()
fig.savefig('./figure' + '/' + 'stripplot' + '.png')