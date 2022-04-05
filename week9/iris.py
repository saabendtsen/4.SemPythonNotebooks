from cProfile import label
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('../../data/iris_data.csv',decimal=',')
iris.head()

#1. load 'data/iris_data.csv' into a dataframe (use decimal=',') and remove the 2 `Petal` columns. Now we are left with a 2D feature space


iris.drop('Petal length', inplace=True, axis=1)
iris.drop('Petal width',inplace=True, axis=1)


#2. get unique labels (Species column)

species = iris['Species'].unique()

#3. plot with a scatter plot each iris flower sample colored by label (3 different colors)

plt.figure(figsize=(10, 8))
plt.title('Iris Sepal size')

for speice in species:

    tmp = iris.loc[iris['Species'] == speice]
    x = tmp['Sepal width']
    y = tmp['Sepal length']
    plt.scatter(x, y,label=speice)



plt.xlabel('Width')
plt.ylabel('length')
plt.legend()

plt.show()