import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import scipy
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
#Features
X = newdf.iloc[:,2:]
#Diet
y = newdf.iloc[:,1]
#standardize features
X = StandardScaler().fit_transform(X)
pca = PCA(n_components = 2)
pricipalComponents = pca.fit_transform(X)
principalDf = pd.DataFrame(data = pricipalComponents,
                         columns = ['p1','p2'])
finalDf = pd.concat([principalDf, y], axis = 1)
###Here I will set the start and finish of each diet
d1= finalDf.loc[finalDf['diet']==1]
d2= finalDf.loc[finalDf['diet']==2]
d3= finalDf.loc[finalDf['diet']==3]
######################################
#graph time
fig, ax = plt.subplots()
data = [d1, d2, d3]
colors = ['red', 'green', 'blue']
diets = ['High Fat', 'High Carb', 'High Protein']
for c, diet, d in zip(colors, diets, data):
    lob = np.polyfit(d.iloc[:,0], d.iloc[:,1],1)
    f = np.poly1d(lob) #could print this function
    xnew = np.linspace(-5,12,50)
    ynew = f(xnew)
    ax.scatter(d.iloc[:,0], d.iloc[:,1], c=c, label = diet,
               alpha = 0.3, edgecolors = 'none')
    plt.plot(xnew, ynew,'-', c=c, alpha = 0.4)
plt.title('PCA Diet Differences')
ax.legend(diets)
ax.grid(True)
plt.show()

####################################################
sexdf = pd.concat([principalDf, sex], axis = 1)
fig, ax = plt.subplots()
s1 = finalDf.loc[sexdf['___sex']==1]
s2 = finalDf.loc[sexdf['___sex']==2]
label = ['sex_1', 'sex_2']
deg = 1
#Sex 1
ax.scatter(s1.iloc[:,0], s1.iloc[:,1], c='red', label = 'sex 1',
               alpha = 0.3, edgecolors = 'none')
lob = np.polyfit(s1.iloc[:,0], s1.iloc[:,1],deg)
f = np.poly1d(lob) #could print this function
xnew = np.linspace(-5,12,50)
ynew = f(xnew)
plt.plot(xnew, ynew,'-', c='red', alpha = 0.4)
#Sex 2
ax.scatter(s2.iloc[:,0], s2.iloc[:,1], c='blue', label = 'sex 1',
               alpha = 0.3, edgecolors = 'none')
lob = np.polyfit(s2.iloc[:,0], s2.iloc[:,1],deg)
f = np.poly1d(lob) #could print this function
xnew = np.linspace(-5,12,50)
ynew = f(xnew)
plt.plot(xnew, ynew,'-', c='blue', alpha = 0.4)
ax.legend(label)
plt.title('Sex Difference')
ax.grid(True)
plt.show()
####################################################
racedf = pd.concat([principalDf, race], axis = 1)
fig, ax = plt.subplots()
r1 = racedf.loc[racedf['___race2']==1]
r2 = racedf.loc[racedf['___race2']==2]
label = ['race_1', 'race_2']
deg = 1
#Sex 1
ax.scatter(r1.iloc[:,0], r1.iloc[:,1], c='red', label = 'sex 1',
               alpha = 0.3, edgecolors = 'none')
lob = np.polyfit(s1.iloc[:,0], s1.iloc[:,1],deg)
f = np.poly1d(lob) #could print this function
xnew = np.linspace(-5,12,50)
ynew = f(xnew)
plt.plot(xnew, ynew,'-', c='red', alpha = 0.4)
#Sex 2
ax.scatter(r2.iloc[:,0], r2.iloc[:,1], c='blue', label = 'sex 1',
               alpha = 0.3, edgecolors = 'none')
lob = np.polyfit(s2.iloc[:,0], s2.iloc[:,1],deg)
f = np.poly1d(lob) #could print this function
xnew = np.linspace(-5,12,50)
ynew = f(xnew)
plt.plot(xnew, ynew,'-', c='blue', alpha = 0.4)
ax.legend(label)
plt.title('Race Difference')
ax.grid(True)
plt.show()
####################################################
