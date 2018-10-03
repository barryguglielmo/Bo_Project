import matplotlib.pyplot as plt
import pandas as pd
import os

########################################################################
def box_all_sheets(file, protlist, col, col_name):
    """boxplots from same col of all sheets"""
    lg_data = []
    myfile = pd.ExcelFile(file)
    for i in protlist:
        data = myfile.parse(i).iloc[:,col]
        lg_data.append(data)   
    box = pd.DataFrame(lg_data)
    box = box.transpose()
    box.columns = protlist
    box.boxplot(rot = 45, fontsize = 9)
    plt.show()
    return box
def plate_data(file, sheet_id_number, r1, r2, c1, c2):
    """Get the Data For a 96 Well Plate thats been Read"""
    myfile = pd.ExcelFile(file)
    data = myfile.parse(sheet_id_number).iloc[r1:r2,c1:c2]
    return data
def plate_3d(dataframe, graph_id, save_path, show = True):
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
    plt.savefig(graph_id+'.png')
    if show == True:
        plt.show()
    plt.close()
