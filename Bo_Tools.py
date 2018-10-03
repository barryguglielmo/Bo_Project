import matplotlib.pyplot as plt
from pandas import ExcelWriter
from scipy import stats
import numpy as np
import pandas as pd
import os

########################################################################
def box_all_sheets(file, protlist, col, col_name, z_score = True):
    """boxplots from same col of all sheets"""
    lg_data = []
    myfile = pd.ExcelFile(file)
    for i in protlist:
        data = myfile.parse(i).iloc[:,col]
        lg_data.append(data)   
    box = pd.DataFrame(lg_data)
    box = box.transpose()
    box.columns = protlist
    if z_score ==True:
        box = stats.zscore(box)
        box = pd.DataFrame(box)
    box.boxplot(rot = 45, fontsize = 9)
    plt.show()
    return box
########################################################################
def box_cols_single(file, sheet_numb_or_name, col_names, z_score = True):
    """Boxplot of all cols of a single sheet"""
    myfile = pd.ExcelFile(file)
    data = myfile.parse(sheet_numb_or_name)
    if z_score ==True:
        data = stats.zscore(data)
        data = pd.DataFrame(data)
    data.boxplot(rot = 45, fontsize = 9)
    plt.show()
    return data
########################################################################
def plate_data(file, sheet_id_number, r1, r2, c1, c2):
    """Get the Data For a 96 Well Plate thats been Read"""
    myfile = pd.ExcelFile(file)
    data = myfile.parse(sheet_id_number).iloc[r1:r2,c1:c2]
    return data
########################################################################
def plate_3d(dataframe, graph_id, save_path, show = True, save = True):
    """Return 3D Bar Graph of all Plates"""
    style.use('ggplot')
    datamatrix = dataframe.as_matrix()
    flat = datamatrix.flatten()
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    x3 = [1,1,1,1,1,1,1,1,1,1,1,1,
          2,2,2,2,2,2,2,2,2,2,2,2,
          3,3,3,3,3,3,3,3,3,3,3,3,
          4,4,4,4,4,4,4,4,4,4,4,4,
          5,5,5,5,5,5,5,5,5,5,5,5,
          6,6,6,6,6,6,6,6,6,6,6,6,
          7,7,7,7,7,7,7,7,7,7,7,7,
          8,8,8,8,8,8,8,8,8,8,8,8]
    y3 = [1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12,
          1,2,3,4,5,6,7,8,9,10,11,12]
    z3 = np.ones(96)
    dx = np.ones(96)
    dy = np.ones(96)
    dz = flat
    ax1.bar3d(x3, y3, z3, dx, dy, dz,color='#00ceaa' )
    ax1.set_xlabel(graph_id)
    ax1.set_ylabel(graph_id)
    ax1.set_zlabel('Absorbance')
    os.chdir(save_path)
    if save == True:
        plt.savefig(graph_id+'.png')
    if show == True:
        plt.show()
    plt.close()
########################################################################
def data_from_all_sheets(file, col_names, protlist, r1, r2, c1, c2):
    """Get the Data From all Sheets"""
    lg_data = []
    for i in protlist:
        myfile = pd.ExcelFile(file)
        data = myfile.parse(i).iloc[r1:r2,c1:c2]
        data.columns = col_names
        lg_data.append(data)
    return lg_data
#########################################################
def myconcat(files, col_names, protlist, out_file, r1, r2, c1 , c2):
    """Concat data from all sheets and return excel file"""
    a = data_from_all_sheets(files[0], col_names, protlist ,r1, r2, c1, c2)
    for f in range(1, len(files)):
        b = data_from_all_sheets(files[f], col_names, protlist ,r1, r2, c1, c2)
        for i in range(0, len(a)):
            a[i] = pd.concat([a[i], b[i]])     
    writer = ExcelWriter(out_file)
    for i in range(0, len(a)):
        a[i].to_excel(writer, sheet_name = str(protlist[i]))
    writer.save()
