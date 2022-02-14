from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# name & path definition
path = './seaborn-data'
name = 'iris'
full_path = path + '/' + name + '.csv'
figsize = (8, 6)

# load data
iris = pd.read_csv(full_path)
print(iris)

# styling
sns.set(rc = {'figure.figsize': figsize})
sns.set_context('paper',font_scale=0.85)

# # create figure (Close when using type D, open in other situation)
# iris_g = sns.PairGrid(iris, hue='species')

# # type A
# iris_g = iris_g.map(plt.scatter)

# # type B
# iris_g = iris_g.map_diag(plt.hist)
# iris_g = iris_g.map_offdiag(plt.scatter)

# # type C
# iris_g = iris_g.map_upper(plt.scatter)
# iris_g = iris_g.map_lower(sns.kdeplot)
# iris_g = iris_g.map_diag(plt.hist)

# type D
iris_g = sns.PairGrid(iris, hue='species', x_vars=['sepal_length', 'sepal_width'], y_vars=['petal_length', 'petal_width'])
iris_g = iris_g.map(plt.scatter)
iris_g = iris_g.add_legend()
sns.move_legend(iris_g, 'upper left', bbox_to_anchor=(.01, 1), ncol=3, frameon=True, title=None)

# save figure
iris_g.savefig('./figure' + '/' + 'pairgrid1' + '.png')