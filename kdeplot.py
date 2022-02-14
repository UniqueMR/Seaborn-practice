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
fig = sns.kdeplot(crash_df['alcohol'])
fig = fig.get_figure()
fig.savefig('./figure' + '/' + 'kdeplot' + '.png')