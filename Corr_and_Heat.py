import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
import os
os.chdir('S:/Nutrition/Sacks Lab Data/2018.06 - OMNIHeart HDL Subspecies/DATA/BG')

#Our file
df = pd.read_csv('07_8_merged Lipid and HDLSubSpecies.csv')
#List of columns of interest
ID = df.iloc[:,1]
prots = df.iloc[:, 4:26]
sex = df.iloc[:, 45]
age = df.iloc[:, 47]
bmi = df.iloc[:, 48]
lipids = df.iloc[:,60:64]
diet = df.iloc[:,77]
race = df.iloc[:,49]

newdf = pd.concat([ID, diet, prots, sex, age, bmi, lipids], axis = 1)
zofall = scipy.stats.zscore(newdf.iloc[:,2:])


prots_z = scipy.stats.zscore(prots)
plt.plot(prots_z, linewidth = 0.5)
plt.plot(np.linspace(0,450,100), [0]*100, c = 'red')
plt.title('Z Scores of All Proteins')

##################
#corrilation matrix
fig, ax = plt.subplots()
protdf = pd.DataFrame(prots_z)
corr = protdf.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(200, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap = cmap, linewidth = 1, xticklabels = list(prots), yticklabels = list(prots))
plt.title('Protein Corrilation After Zscore Normalization')
plt.show()

sns.clustermap(corr,xticklabels = list(prots), yticklabels = list(prots))
plt.title('Clustered Heatmap of Proteins Zscores', loc = 'left')
plt.show()
