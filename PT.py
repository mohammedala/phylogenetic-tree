from typing import Pattern
import pandas as pd
import treelib as tb
import re

def phylogenetic_tree(input_dict): 
    tree = [] 

    while (True):
        names = [char for char in input_dict.keys()]

        first_matrix = pd.DataFrame(input_dict, index=names)
        min = first_matrix.iloc[0].max()

        for i in range(len(names)):
            col = first_matrix[names[i]]
            col = col.drop([names[i]] , axis =0)
            for j in range(len(names)-1):
                if col[j] <= min:
                    min = col[j]
                    colname = col.name
                    row = col.idxmin()
                    rowname = str(row)
        
        print(first_matrix)
        print("minimum distance between " + str(colname) +" and "+ str(rowname)+" is "+ str(min))
        
        tree.append([colname ,rowname, min])
        input_dict.clear()
        new_names = []
        #finding list of new group
        for i in range(len(names)):
            if names[i] == colname:
                new_names.append(colname+rowname)
            elif names[i] == rowname:
                continue
            else:
                new_names.append(names[i])
        
        #stopping condition
        if len(names) <=2:
            break

        for i in range(len(new_names)):
            input_dict[new_names[i]] =[0 for n in range(len(new_names))]

        for i in range(len(names)):
            counter = 0
            col = first_matrix[names[i]]
            for j in range(len(names)):
                if col.name == colname:
                    sec_col = first_matrix[rowname]
                    if col.name == names[j]:
                        input_dict[colname+rowname][counter] = 0
                        counter= counter +1
                    elif names[j] != rowname:
                        dis_sum = (col[names[j]] + sec_col[names[j]]) / 2
                        input_dict[colname+rowname][counter] = dis_sum
                        counter= counter +1
                        print("New average distance bewteen " + str(colname+rowname) + " and "+ str(names[j])+" is " + str(dis_sum))
                elif col.name == colname or col.name == rowname:
                    if names[j] == colname or names[j] == rowname:
                        continue
                else:
                    sec_col = first_matrix[rowname]
                    if names[j] == colname:
                        dis_sum = (col[names[j]] + sec_col[names[i]]) / 2
                        input_dict[col.name][counter] = dis_sum
                        counter= counter +1
                    elif names[j] != rowname:
                        input_dict[col.name][counter] = col[j]
                        counter= counter +1
    return tree
        

input_dict = { "A":[0,20,60,100,90] , "B" :[20,0,50,90,80] , 
        "C": [60,50,0,40,50], "D":[100,90,40,0,30], "E": [90,80,50,30,0]}

tree = phylogenetic_tree(input_dict)
print(tree)       





