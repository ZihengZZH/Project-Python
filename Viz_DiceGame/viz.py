# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:46:24 2017

@author: Ziheng
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


'''
This program is designed to visualise the autotest result generated from a dice game
Since there are two strategies and each has winning probability under a specific condition
Therefore, for comparison between them, the 3D graphs and contour graphs are chosen to visualise.
Also, Pandas is used for data manipulation and matplotlib used for data visualisation
'''

df = pd.read_table('autotest result.txt', delim_whitespace=True)
df = df.sort_values(by=['Points'])

A,datas = [],[]
file_names = ["50","100","150"]

for k in [50,100,150]:
    data_part = df[df.Points==k]
    datas.append(data_part)

i = 0
for data in datas:
    data = data.sort_values(by=['Gain_val','Throw_val'])
    g_v,t_v,g_w,t_w = data['Gain_val'],data['Throw_val'],data['Gain_win'],data['Throw_win']
    
    # GET THE 3D GRAPHS
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    ax.scatter(g_v[:],t_v[:],g_w[:],c='g',label='times of GAIN')
    ax.scatter(g_v[:],t_v[:],t_w[:],c='r',label='times of THROW')
    
    ax.legend()
    ax.set_zlabel('Times of win')
    ax.set_ylabel('THROW value')
    ax.set_xlabel('GAIN value')
    
    # WRITE TO FILES
    graph_name = './graphs/res' + file_names[i] + '.png'
    plt.savefig(graph_name, dpi=1000)
    plt.close()
    i += 1
    
i = 0
for data in datas:
    data = data.sort_values(by=['Gain_val','Throw_val'])
    g_v,t_v,g_w,t_w = data['Gain_val'],data['Throw_val'],data['Gain_win'],data['Throw_win']
    
    # GET THE CONTOUR GRAPHS
    g_wfrac = g_w / 5000
    FR = g_wfrac.values.reshape(16,10)
    X, Y = np.mgrid[0:1:16j, 0:1:10j]
    CS = plt.contourf(X,Y,FR)
    cb = plt.colorbar(CS,orientation='vertical',shrink=0.9)
    cb.set_label('GAIN winning probability')
    
    # WRITE TO FILES
    graph_name = './graphs/contour' + file_names[i] + '.png'
    plt.savefig(graph_name, dpi=1000)
    plt.close()
    i += 1
    
print("All successfully written to files")


# These functions were intended to build a model for linear regression to fit the pattern
# However, the pattern inside the dataset is obviously not linear
# So, it is not practical to get linear regression through normal equation
'''
def get_alpha(x1,x2,y):
    B = np.mat(np.column_stack((x1.as_matrix(),x2.as_matrix(),y.as_matrix())))
    y = B[:,2]
    X = np.mat(np.column_stack((np.ones(y.shape[0]),B[:,:2])))
    A = (np.linalg.pinv(X.T*X))*(X.T)*y
    return A

def standard(data):
    return ((data-data.mean())/data.std())
'''