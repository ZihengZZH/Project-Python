#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:35:47 2017

@author: zhangziheng
"""

import numpy as np


# To show a table in a regular format
def show(table):
    
    for i in range(table.shape[0]):
        for j in range(table.shape[1]):
            print("(",table[i][j][0],",",table[i][j][1],")\t",end="")
        print()
        

# To calculate the pure nash equilibria and print it/them out
def pure_Nash(table):
    
    # pay off of two individual player
    table_A = table[:,:,0]
    table_B = table[:,:,1] 
    
    A = []
    B = []
    A_index = []
    B_index = []
    
    # for loop to find max payoff for each strategy of the other
    for i in range(table.shape[1]):
        a_max = a_index = -100
        for index in range(table.shape[0]):
            if table[:,i][index][0] >= a_max:
                a_max = table[:,i][index][0]
                a_index = index
        A.append(a_max)
        A_index.append((a_index,i))
    
    # for loop to find max payoff for each strategy of the other
    for j in range(table.shape[0]):
        b_max = b_index = -100
        for index in range(table.shape[1]):
            if table[j][index][1] >= b_max:
                b_max = table[j][index][1]
                b_index = index
        B.append(b_max)
        B_index.append((j,b_index))
        
    # find the intersection part in which both player has max payoff
    PNE = set(A_index).intersection(B_index)
    
    if not PNE:
        print("There is no pure Nash equilibrium")
    else:
        print("The pure Nash equilibrium is/are", end=" ")
        for pure in PNE:
            print(table[pure[0],pure[1],:], end=" ")
        print()
        

# To test the PNE algorithm 
def test():
    Table_test = []
    Table_test.append(np.array([[(2,2),(0,3)],[(3,0),(1,1)]]))
    Table_test.append(np.array([[(2,1),(0,0)],[(0,0),(1,2)]]))
    Table_test.append(np.array([[(5,5),(0,3)],[(3,0),(3,3)]]))
    Table_test.append(np.array([[(5,3),(2,7),(0,4)],[(5,5),(5,-1),(-4,-2)]]))
    Table_test.append(np.array([[(0,0),(1,-1),(-1,1)],[(-1,1),(0,0),(1,-1)],[(1,-1),(-1,1),(0,0)]]))
    Table_test.append(np.array([[(7,2),(2,7),(3,6)],[(2,7),(7,2),(4,5)]]))
    Table_test.append(np.array([[(8,3),(3,5),(6,3)],[(3,3),(5,5),(4,8)],[(5,2),(3,7),(4,9)]]))
    
    for table in Table_test:
        show(table)
        pure_Nash(table)
    

if __name__ == "__main__":
    
    test()
    
    '''
    MORE LINES CAN BE ADDED FOR FURTHER FUNCTIONALITY 
    THIS ALGORITHM ONLY FITS TWO-PLAYER STRATEGIC GAME
    AND WHETHER THIS ALGORITHM FITS HIGH NUMBER OF STRATEGIES REMAINS UNKNOWN
    '''
    
    