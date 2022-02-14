import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# name & path definition
path = './seaborn-data'
name = 'car_crashes'
full_path = path + '/' + name + '.csv'

# load data
crash_df = pd.read_csv(full_path)

# create & save figure
fig = sns.jointplot(x='speeding', y='alcohol', data=crash_df, kind='scatter')
fig.savefig('./figure' + '/' + 'jointplot' + '.png')