# -*- coding: utf-8 -*-
"""TI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HEgEH9Dbi_m6mPnXNNdOb4Gcss4GoWUl
"""

import numpy as np
import pandas as pd

from sklearn import datasets

iris= datasets.load_iris()

iris.data

iris.target

df_iris = pd.DataFrame(iris.data)
df_iris['target'] = iris.target

df_iris.head()

df_iris.columns.tolist()

df_iris.columns = ['sepal_length', 'sepal width', 'petal_length','petal_width', 'type']

df_iris.head(10)

df_iris.shape
#tamanho do dataset

df_iris['sepal_length'].head()
#Acessar uma coluna

df_iris.sepal_length.head()
#acessar uma coluna também

df_iris[['sepal_length', 'petal_length']].head()

df_iris.drop(['type'], axis=1).head()

df_iris['type'].unique()

df_iris[df_iris['type'] == 2].head()

df_iris[df_iris['petal_length'] > 5].head()

df_iris[
 (df_iris['type'] == 2) & (df_iris['petal_length'] > 5)
].head()

print('Menor:', df_iris['petal_width'].min())
print('Maior:', df_iris['petal_width'].max())
print('Média:', df_iris['petal_width'].mean())

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(
hidden_layer_sizes=(100, 50),
tol=0.01
)
mlp.fit(
df_iris.drop(['type'], axis=1),
df_iris['type']
)

mlp.predict(
  [
    [6, 5, 5, 1],
    [6, 5, 5, 10],
    [2, 2, 4, 2]
  ]
)

src = 'https://raw.githubusercontent.com/rafjaa/machine_learning_fecib/master/src/wine-quality-classifier/dados/winequality-red.csv'
df_wine = pd.read_csv(src, sep=';')
df_wine.head()

#total de vinhos
s_wine = df_wine.groupby('Qualidade').count()['Álcool']
print('\nTotal de vinhos: ', df_wine.shape[0])
#Gráfico
s_wine.plot(kind='bar', title='Total de vinhos para cada nota(distribuição de frequência)')

import matplotlib.pyplot as plt
import seaborn as sns
corr_mat = df_wine.corr()
f, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(
  corr_mat,
  annot=True,
  square=True,
  vmax=1,
  vmin=-1
)

df_wine['Qualidade'] = df_wine['Qualidade'].apply(lambda x: 0 if x < 6 else 1)
# gráfico
df_wine.groupby('Qualidade').count()['Álcool'].plot(kind='bar', title='Vinhos bons(1) e ruins(0)')

from sklearn.ensemble import RandomForestClassifier


clf = RandomForestClassifier(
    n_estimators=50,
    max_depth=5
)

clf.fit(
    df_wine.drop(['Qualidade'], axis=1),
    df_wine['Qualidade']
)

clf.feature_importances_

import matplotlib.colors as mcolors

feat_importances = pd.Series(
clf.feature_importances_,
index=df_wine.drop(['Qualidade'], axis=1).columns
)
plt.style.use('dark_background')
feat_importances.plot(kind='barh');