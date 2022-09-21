# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 16:11:49 2021

@author: Andreu
"""
#%% Import and matrixes
import numpy as np
import pandas as pd
test = []

initialm = np.matrix([[0,2,1] , [6,7,4] , [3,8,5]])
optm = np.matrix([[0,2,1] , [6,7,4] , [3,8,5]])         #408
optm2 = np.matrix([[7,8,0] , [6,5,4] , [3,2,1]])        #152
optm3 = np.matrix([[5,2,0] , [6,7,4] , [3,8,1]])        #42
print("Initial matrix:")
print(initialm)

finalm = np.matrix([[1,2,3] , [8,0,4] , [7,6,5]])
print("Final matrix: ")
print(finalm)

#%% To get the position of the empty tile:

xlist = ["0" , "1" , "2"]
ylist = ["0" , "1" , "2"]

for x in xlist:
    for y in ylist:
        zz = initialm[int(x) , int(y)]
        if zz == 0:
            xpos = int(x)
            ypos = int(y)
#%% To see the possibilities of the empty tile:

possibilities = list()

if xpos-1 >= 0:
    possibilities.append([xpos-1 , ypos])
if xpos+1 < 3:
    possibilities.append([xpos+1 , ypos])
if ypos-1 >= 0:
    possibilities.append([xpos , ypos-1])
if ypos+1 < 3:
    possibilities.append([xpos , ypos+1])


#%% To see the possibilities of matrix

choices = list()

for i in range(len(possibilities)):
    xsub = possibilities[i][0]
    ysub = possibilities[i][1]
    subs = initialm[xsub , ysub]
    statem = initialm.copy()
    statem[xpos , ypos] = subs
    statem[xsub , ysub] = 0
    choices.append(statem)

#%% Evaluation function

diflist = list()

for i in range(len(choices)):
    dummie = choices[i].copy()
    
    for x in xlist:
        for y in ylist:
            zz = dummie[int(x) , int(y)]
            if zz == 1:
                xpos = int(x)
                ypos = int(y)
                xfin = 0
                yfin = 0
                
                xdif = xfin-xpos
                ydif = yfin-ypos
                if xdif<0:
                    xdif = -1*xdif
                if ydif<0:
                    ydif = -1*ydif
                dif1 = xdif+ydif
            elif zz == 2:
                xpos = int(x)
                ypos = int(y)
                xfin = 0
                yfin = 1
                
                xdif = xfin-xpos
                ydif = yfin-ypos
                if xdif<0:
                    xdif = -1*xdif
                if ydif<0:
                    ydif = -1*ydif
                dif2 = xdif+ydif
            elif zz == 3:
                xpos = int(x)
                ypos = int(y)
                xfin = 0
                yfin = 2
                
                xdif = xfin-xpos
                ydif = yfin-ypos
                if xdif<0:
                    xdif = -1*xdif
                if ydif<0:
                    ydif = -1*ydif
                dif3 = xdif+ydif
            elif zz == 4:
                xpos = int(x)
                ypos = int(y)
                xfin = 1
                yfin = 2
                
                xdif = xfin-xpos
                ydif = yfin-ypos
                if xdif<0:
                    xdif = -1*xdif
                if ydif<0:
                    ydif = -1*ydif
                dif4 = xdif+ydif
            elif zz == 5:
                xpos = int(x)
                ypos = int(y)
                xfin = 2
                yfin = 2
                
                xdif = xfin-xpos
                ydif = yfin-ypos
                if xdif<0:
                    xdif = -1*xdif
                if ydif<0:
                    ydif = -1*ydif
                dif5 = xdif+ydif
            elif zz == 6:
                xpos = int(x)
                ypos = int(y)
                xfin = 2
                yfin = 1
                
                xdif = xfin-xpos
                ydif = yfin-ypos
                if xdif<0:
                    xdif = -1*xdif
                if ydif<0:
                    ydif = -1*ydif
                dif6 = xdif+ydif
            elif zz == 7:
                xpos = int(x)
                ypos = int(y)
                xfin = 2
                yfin = 0
                
                xdif = xfin-xpos
                ydif = yfin-ypos
                if xdif<0:
                    xdif = -1*xdif
                if ydif<0:
                    ydif = -1*ydif
                dif7 = xdif+ydif
            elif zz == 8:
                xpos = int(x)
                ypos = int(y)
                xfin = 1
                yfin = 0
                
                xdif = xfin-xpos
                ydif = yfin-ypos
                if xdif<0:
                    xdif = -1*xdif
                if ydif<0:
                    ydif = -1*ydif
                dif8 = xdif+ydif
    
    dif = dif1 + dif2 + dif3 + dif4 + dif5  +dif6 + dif7  +dif8
    diflist.append(dif)

#%% Selection following the evaluation function

while len(diflist) < 4:
    diflist.append(99)

diflist = pd.DataFrame(diflist , columns = ["diference"])
diflist["option"] = [0 , 1 , 2 , 3]
diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
diflist = int(diflist["option"])

statem0 = choices[diflist].copy()
print("Actual State:")
print(statem0)

mlist = list()
mlist.append(str(statem0))
mlist.append(str(initialm))
num = 1
#%% Do this process once and again

while not (statem0 == finalm).all():
    for x in xlist:
        for y in ylist:
            zz = statem0[int(x) , int(y)]
            if zz == 0:
                xpos = int(x)
                ypos = int(y)
                
    del possibilities
    possibilities = []
    
    if xpos-1 >= 0:
        possibilities.append([xpos-1 , ypos])
    if xpos+1 < 3:
        possibilities.append([xpos+1 , ypos])
    if ypos-1 >= 0:
        possibilities.append([xpos , ypos-1])
    if ypos+1 < 3:
        possibilities.append([xpos , ypos+1])
        
    del choices
    choices = []
    
    for i in range(len(possibilities)):
        xsub = possibilities[i][0]
        ysub = possibilities[i][1]
        subs = statem0[xsub , ysub]
        statem = statem0.copy()
        statem[xpos , ypos] = subs
        statem[xsub , ysub] = 0
        z = []
        for j in range(len(mlist)):
            if not (str(statem) in mlist):
                z.append("Yes")
            else:
                z.append("No")
        if ("No" in z):
            pass
        else:
            choices.append(statem)
            
    if len(choices) > 0:
        pass
    else:
        print("Reseting mlist")
        del mlist
        mlist = []
        del choices
        choices = []
        for i in range(len(possibilities)):
            xsub = possibilities[i][0]
            ysub = possibilities[i][1]
            subs = statem0[xsub , ysub]
            statem = statem0.copy()
            statem[xpos , ypos] = subs
            statem[xsub , ysub] = 0
            z = []
            for j in range(len(mlist)):
                if not (str(statem) in mlist):
                    z.append("Yes")
                else:
                    z.append("No")
            if ("No" in z):
                pass
            else:
                choices.append(statem)

    del diflist
    diflist = list()
    
    for i in range(len(choices)):
        dummie = choices[i].copy()
        
        for x in xlist:
            for y in ylist:
                zz = dummie[int(x) , int(y)]
                if zz == 1:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif1 = xdif+ydif
                elif zz == 2:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 1
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif2 = xdif+ydif
                elif zz == 3:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif3 = xdif+ydif
                elif zz == 4:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 1
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif4 = xdif+ydif
                elif zz == 5:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif5 = xdif+ydif
                elif zz == 6:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 1
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif6 = xdif+ydif
                elif zz == 7:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif7 = xdif+ydif
                elif zz == 8:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 1
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif8 = xdif+ydif
        
        dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
        if len(diflist)>0:
            dif = dif
        diflist.append(dif)
    
    while len(diflist) < 4:
        diflist.append(98)
    
    diflist = pd.DataFrame(diflist , columns = ["diference"])
    diflist["option"] = [0 , 1 , 2 , 3]
    diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
    diflist = int(diflist["option"])
    
    statem0 = choices[diflist].copy()
    mlist.append(str(statem0))
    num = num+1
    print("Itineration number:" , num)
    print("Actual matrix:")
    print(statem0)

print("De loquetes!!")

#%% TRAINING

buglist = []
buglist.append(str(initialm))
a = "Logical"

while not (statem0 == finalm).all():
    for x in xlist:
        for y in ylist:
            zz = statem0[int(x) , int(y)]
            if zz == 0:
                xpos = int(x)
                ypos = int(y)
                
    del possibilities
    possibilities = []
    
    if xpos-1 >= 0:
        possibilities.append([xpos-1 , ypos])
    if xpos+1 < 3:
        possibilities.append([xpos+1 , ypos])
    if ypos-1 >= 0:
        possibilities.append([xpos , ypos-1])
    if ypos+1 < 3:
        possibilities.append([xpos , ypos+1])
        
    del choices
    choices = []
    
    for i in range(len(possibilities)):
        xsub = possibilities[i][0]
        ysub = possibilities[i][1]
        subs = statem0[xsub , ysub]
        statem = statem0.copy()
        statem[xpos , ypos] = subs
        statem[xsub , ysub] = 0
        z = []
        for j in range(len(mlist)):
            if not (str(statem) in mlist):
                z.append("Yes")
            else:
                z.append("No")
        if ("No" in z):
            pass
        else:
            choices.append(statem)
            
    if len(choices) > 0:
        pass
    else:
        print("Reseting mlist")
        if (str(statem0) == buglist[0]):
            print("Bugged")
            a = "Random"
        else:
            print("Not bugged")
            a = "Logical"
        del buglist
        buglist = []
        buglist.append(str(statem0))
        del mlist
        mlist = []
        del choices
        choices = []
        for i in range(len(possibilities)):
            xsub = possibilities[i][0]
            ysub = possibilities[i][1]
            subs = statem0[xsub , ysub]
            statem = statem0.copy()
            statem[xpos , ypos] = subs
            statem[xsub , ysub] = 0
            z = []
            for j in range(len(mlist)):
                if not (str(statem) in mlist):
                    z.append("Yes")
                else:
                    z.append("No")
            if ("No" in z):
                pass
            else:
                choices.append(statem)

    del diflist
    diflist = list()
    
    for i in range(len(choices)):
        dummie = choices[i].copy()
        
        for x in xlist:
            for y in ylist:
                zz = dummie[int(x) , int(y)]
                if zz == 1:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif1 = xdif+ydif
                elif zz == 2:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 1
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif2 = xdif+ydif
                elif zz == 3:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif3 = xdif+ydif
                elif zz == 4:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 1
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif4 = xdif+ydif
                elif zz == 5:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif5 = xdif+ydif
                elif zz == 6:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 1
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif6 = xdif+ydif
                elif zz == 7:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif7 = xdif+ydif
                elif zz == 8:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 1
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif8 = xdif+ydif
        
        dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
        if len(diflist)>0:
            dif = dif
        diflist.append(dif)
    
    while len(diflist) < 4:
        diflist.append(98)
    
    diflist = pd.DataFrame(diflist , columns = ["diference"])
    diflist["option"] = [0 , 1 , 2 , 3]
    diflist = diflist.loc[diflist["diference"] < 70]
    if a == "Logical":
        diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
    else:
        diflist = diflist.sort_values("diference" , ascending = True).sample(1).reset_index(drop = True)

    diflist = int(diflist["option"])
    
    statem0 = choices[diflist].copy()
    mlist.append(str(statem0))
    num = num+1
    print("Itineration number:" , num)
    print("Actual matrix:")
    print(statem0)

print("Finally!!")

#%%
while not (statem0 == finalm).all():
    if num<1000:
        while not (statem0 == finalm).all():
            for x in xlist:
                for y in ylist:
                    zz = statem0[int(x) , int(y)]
                    if zz == 0:
                        xpos = int(x)
                        ypos = int(y)
                        
            del possibilities
            possibilities = []
            
            if xpos-1 >= 0:
                possibilities.append([xpos-1 , ypos])
            if xpos+1 < 3:
                possibilities.append([xpos+1 , ypos])
            if ypos-1 >= 0:
                possibilities.append([xpos , ypos-1])
            if ypos+1 < 3:
                possibilities.append([xpos , ypos+1])
                
            del choices
            choices = []
            
            for i in range(len(possibilities)):
                xsub = possibilities[i][0]
                ysub = possibilities[i][1]
                subs = statem0[xsub , ysub]
                statem = statem0.copy()
                statem[xpos , ypos] = subs
                statem[xsub , ysub] = 0
                z = []
                for j in range(len(mlist)):
                    if not (str(statem) in mlist):
                        z.append("Yes")
                    else:
                        z.append("No")
                if ("No" in z):
                    pass
                else:
                    choices.append(statem)
                    
            if len(choices) > 0:
                pass
            else:
                print("Reseting mlist")
                del mlist
                mlist = []
                del choices
                choices = []
                for i in range(len(possibilities)):
                    xsub = possibilities[i][0]
                    ysub = possibilities[i][1]
                    subs = statem0[xsub , ysub]
                    statem = statem0.copy()
                    statem[xpos , ypos] = subs
                    statem[xsub , ysub] = 0
                    z = []
                    for j in range(len(mlist)):
                        if not (str(statem) in mlist):
                            z.append("Yes")
                        else:
                            z.append("No")
                    if ("No" in z):
                        pass
                    else:
                        choices.append(statem)
        
            del diflist
            diflist = list()
            
            for i in range(len(choices)):
                dummie = choices[i].copy()
                
                for x in xlist:
                    for y in ylist:
                        zz = dummie[int(x) , int(y)]
                        if zz == 1:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif1 = xdif+ydif
                        elif zz == 2:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif2 = xdif+ydif
                        elif zz == 3:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif3 = xdif+ydif
                        elif zz == 4:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif4 = xdif+ydif
                        elif zz == 5:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif5 = xdif+ydif
                        elif zz == 6:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif6 = xdif+ydif
                        elif zz == 7:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif7 = xdif+ydif
                        elif zz == 8:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif8 = xdif+ydif
                
                dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
                if len(diflist)>0:
                    dif = dif
                diflist.append(dif)
            
            while len(diflist) < 4:
                diflist.append(98)
            
            diflist = pd.DataFrame(diflist , columns = ["diference"])
            diflist["option"] = [0 , 1 , 2 , 3]
            diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
            diflist = int(diflist["option"])
            
            statem0 = choices[diflist].copy()
            mlist.append(str(statem0))
            num = num+1
            print("Itineration number:" , num)
            print("Actual matrix:")
            print(statem0)

    elif (num<2000 and num>1000):
        while not (statem0 == optm3).all():
            for x in xlist:
                for y in ylist:
                    zz = statem0[int(x) , int(y)]
                    if zz == 0:
                        xpos = int(x)
                        ypos = int(y)
                        
            del possibilities
            possibilities = []
            
            if xpos-1 >= 0:
                possibilities.append([xpos-1 , ypos])
            if xpos+1 < 3:
                possibilities.append([xpos+1 , ypos])
            if ypos-1 >= 0:
                possibilities.append([xpos , ypos-1])
            if ypos+1 < 3:
                possibilities.append([xpos , ypos+1])
                
            del choices
            choices = []
            
            for i in range(len(possibilities)):
                xsub = possibilities[i][0]
                ysub = possibilities[i][1]
                subs = statem0[xsub , ysub]
                statem = statem0.copy()
                statem[xpos , ypos] = subs
                statem[xsub , ysub] = 0
                z = []
                for j in range(len(mlist)):
                    if not (str(statem) in mlist):
                        z.append("Yes")
                    else:
                        z.append("No")
                if ("No" in z):
                    pass
                else:
                    choices.append(statem)
                    
            if len(choices) > 0:
                pass
            else:
                print("Reseting mlist")
                del mlist
                mlist = []
                del choices
                choices = []
                for i in range(len(possibilities)):
                    xsub = possibilities[i][0]
                    ysub = possibilities[i][1]
                    subs = statem0[xsub , ysub]
                    statem = statem0.copy()
                    statem[xpos , ypos] = subs
                    statem[xsub , ysub] = 0
                    z = []
                    for j in range(len(mlist)):
                        if not (str(statem) in mlist):
                            z.append("Yes")
                        else:
                            z.append("No")
                    if ("No" in z):
                        pass
                    else:
                        choices.append(statem)
        
            del diflist
            diflist = list()
            
            for i in range(len(choices)):
                dummie = choices[i].copy()
                
                for x in xlist:
                    for y in ylist:
                        zz = dummie[int(x) , int(y)]
                        if zz == 1:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif1 = xdif+ydif
                        elif zz == 2:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif2 = xdif+ydif
                        elif zz == 3:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif3 = xdif+ydif
                        elif zz == 4:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif4 = xdif+ydif
                        elif zz == 5:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif5 = xdif+ydif
                        elif zz == 6:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif6 = xdif+ydif
                        elif zz == 7:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif7 = xdif+ydif
                        elif zz == 8:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif8 = xdif+ydif
                
                dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
                if len(diflist)>0:
                    dif = dif
                diflist.append(dif)
            
            while len(diflist) < 4:
                diflist.append(98)
            
            diflist = pd.DataFrame(diflist , columns = ["diference"])
            diflist["option"] = [0 , 1 , 2 , 3]
            diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
            diflist = int(diflist["option"])
            
            statem0 = choices[diflist].copy()
            mlist.append(str(statem0))
            num = num+1
            print("Itineration number:" , num)
            print("Actual matrix:")
            print(statem0)

    elif (num<3000 and num>2000):
        while not (statem0 == optm2).all():
            for x in xlist:
                for y in ylist:
                    zz = statem0[int(x) , int(y)]
                    if zz == 0:
                        xpos = int(x)
                        ypos = int(y)
                        
            del possibilities
            possibilities = []
            
            if xpos-1 >= 0:
                possibilities.append([xpos-1 , ypos])
            if xpos+1 < 3:
                possibilities.append([xpos+1 , ypos])
            if ypos-1 >= 0:
                possibilities.append([xpos , ypos-1])
            if ypos+1 < 3:
                possibilities.append([xpos , ypos+1])
                
            del choices
            choices = []
            
            for i in range(len(possibilities)):
                xsub = possibilities[i][0]
                ysub = possibilities[i][1]
                subs = statem0[xsub , ysub]
                statem = statem0.copy()
                statem[xpos , ypos] = subs
                statem[xsub , ysub] = 0
                z = []
                for j in range(len(mlist)):
                    if not (str(statem) in mlist):
                        z.append("Yes")
                    else:
                        z.append("No")
                if ("No" in z):
                    pass
                else:
                    choices.append(statem)
                    
            if len(choices) > 0:
                pass
            else:
                print("Reseting mlist")
                del mlist
                mlist = []
                del choices
                choices = []
                for i in range(len(possibilities)):
                    xsub = possibilities[i][0]
                    ysub = possibilities[i][1]
                    subs = statem0[xsub , ysub]
                    statem = statem0.copy()
                    statem[xpos , ypos] = subs
                    statem[xsub , ysub] = 0
                    z = []
                    for j in range(len(mlist)):
                        if not (str(statem) in mlist):
                            z.append("Yes")
                        else:
                            z.append("No")
                    if ("No" in z):
                        pass
                    else:
                        choices.append(statem)
        
            del diflist
            diflist = list()
            
            for i in range(len(choices)):
                dummie = choices[i].copy()
                
                for x in xlist:
                    for y in ylist:
                        zz = dummie[int(x) , int(y)]
                        if zz == 1:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif1 = xdif+ydif
                        elif zz == 2:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif2 = xdif+ydif
                        elif zz == 3:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif3 = xdif+ydif
                        elif zz == 4:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif4 = xdif+ydif
                        elif zz == 5:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif5 = xdif+ydif
                        elif zz == 6:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif6 = xdif+ydif
                        elif zz == 7:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif7 = xdif+ydif
                        elif zz == 8:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif8 = xdif+ydif
                
                dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
                if len(diflist)>0:
                    dif = dif
                diflist.append(dif)
            
            while len(diflist) < 4:
                diflist.append(98)
            
            diflist = pd.DataFrame(diflist , columns = ["diference"])
            diflist["option"] = [0 , 1 , 2 , 3]
            diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
            diflist = int(diflist["option"])
            
            statem0 = choices[diflist].copy()
            mlist.append(str(statem0))
            num = num+1
            print("Itineration number:" , num)
            print("Actual matrix:")
            print(statem0)
                                
    else:
        while not (statem0 == optm).all():
            for x in xlist:
                for y in ylist:
                    zz = statem0[int(x) , int(y)]
                    if zz == 0:
                        xpos = int(x)
                        ypos = int(y)
                        
            del possibilities
            possibilities = []
            
            if xpos-1 >= 0:
                possibilities.append([xpos-1 , ypos])
            if xpos+1 < 3:
                possibilities.append([xpos+1 , ypos])
            if ypos-1 >= 0:
                possibilities.append([xpos , ypos-1])
            if ypos+1 < 3:
                possibilities.append([xpos , ypos+1])
                
            del choices
            choices = []
            
            for i in range(len(possibilities)):
                xsub = possibilities[i][0]
                ysub = possibilities[i][1]
                subs = statem0[xsub , ysub]
                statem = statem0.copy()
                statem[xpos , ypos] = subs
                statem[xsub , ysub] = 0
                z = []
                for j in range(len(mlist)):
                    if not (str(statem) in mlist):
                        z.append("Yes")
                    else:
                        z.append("No")
                if ("No" in z):
                    pass
                else:
                    choices.append(statem)
                    
            if len(choices) > 0:
                pass
            else:
                print("Reseting mlist")
                del mlist
                mlist = []
                del choices
                choices = []
                for i in range(len(possibilities)):
                    xsub = possibilities[i][0]
                    ysub = possibilities[i][1]
                    subs = statem0[xsub , ysub]
                    statem = statem0.copy()
                    statem[xpos , ypos] = subs
                    statem[xsub , ysub] = 0
                    z = []
                    for j in range(len(mlist)):
                        if not (str(statem) in mlist):
                            z.append("Yes")
                        else:
                            z.append("No")
                    if ("No" in z):
                        pass
                    else:
                        choices.append(statem)
        
            del diflist
            diflist = list()
            
            for i in range(len(choices)):
                dummie = choices[i].copy()
                
                for x in xlist:
                    for y in ylist:
                        zz = dummie[int(x) , int(y)]
                        if zz == 1:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif1 = xdif+ydif
                        elif zz == 2:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif2 = xdif+ydif
                        elif zz == 3:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif3 = xdif+ydif
                        elif zz == 4:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif4 = xdif+ydif
                        elif zz == 5:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif5 = xdif+ydif
                        elif zz == 6:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif6 = xdif+ydif
                        elif zz == 7:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif7 = xdif+ydif
                        elif zz == 8:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif8 = xdif+ydif
                
                dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
                if len(diflist)>0:
                    dif = dif
                diflist.append(dif)
            
            while len(diflist) < 4:
                diflist.append(98)
            
            diflist = pd.DataFrame(diflist , columns = ["diference"])
            diflist["option"] = [0 , 1 , 2 , 3]
            diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
            diflist = int(diflist["option"])
            
            statem0 = choices[diflist].copy()
            mlist.append(str(statem0))
            num = num+1
            print("Itineration number:" , num)
            print("Actual matrix:")
            print(statem0)

        while not (statem0 == finalm).all():
            for x in xlist:
                for y in ylist:
                    zz = statem0[int(x) , int(y)]
                    if zz == 0:
                        xpos = int(x)
                        ypos = int(y)
                        
            del possibilities
            possibilities = []
            
            if xpos-1 >= 0:
                possibilities.append([xpos-1 , ypos])
            if xpos+1 < 3:
                possibilities.append([xpos+1 , ypos])
            if ypos-1 >= 0:
                possibilities.append([xpos , ypos-1])
            if ypos+1 < 3:
                possibilities.append([xpos , ypos+1])
                
            del choices
            choices = []
            
            for i in range(len(possibilities)):
                xsub = possibilities[i][0]
                ysub = possibilities[i][1]
                subs = statem0[xsub , ysub]
                statem = statem0.copy()
                statem[xpos , ypos] = subs
                statem[xsub , ysub] = 0
                z = []
                for j in range(len(mlist)):
                    if not (str(statem) in mlist):
                        z.append("Yes")
                    else:
                        z.append("No")
                if ("No" in z):
                    pass
                else:
                    choices.append(statem)
                    
            if len(choices) > 0:
                pass
            else:
                print("Reseting mlist")
                del mlist
                mlist = []
                del choices
                choices = []
                for i in range(len(possibilities)):
                    xsub = possibilities[i][0]
                    ysub = possibilities[i][1]
                    subs = statem0[xsub , ysub]
                    statem = statem0.copy()
                    statem[xpos , ypos] = subs
                    statem[xsub , ysub] = 0
                    z = []
                    for j in range(len(mlist)):
                        if not (str(statem) in mlist):
                            z.append("Yes")
                        else:
                            z.append("No")
                    if ("No" in z):
                        pass
                    else:
                        choices.append(statem)
        
            del diflist
            diflist = list()
            
            for i in range(len(choices)):
                dummie = choices[i].copy()
                
                for x in xlist:
                    for y in ylist:
                        zz = dummie[int(x) , int(y)]
                        if zz == 1:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif1 = xdif+ydif
                        elif zz == 2:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif2 = xdif+ydif
                        elif zz == 3:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 0
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif3 = xdif+ydif
                        elif zz == 4:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif4 = xdif+ydif
                        elif zz == 5:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 2
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif5 = xdif+ydif
                        elif zz == 6:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 1
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif6 = xdif+ydif
                        elif zz == 7:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 2
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif7 = xdif+ydif
                        elif zz == 8:
                            xpos = int(x)
                            ypos = int(y)
                            xfin = 1
                            yfin = 0
                            
                            xdif = xfin-xpos
                            ydif = yfin-ypos
                            if xdif<0:
                                xdif = -1*xdif
                            if ydif<0:
                                ydif = -1*ydif
                            dif8 = xdif+ydif
                
                dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
                if len(diflist)>0:
                    dif = dif
                diflist.append(dif)
            
            while len(diflist) < 4:
                diflist.append(98)
            
            diflist = pd.DataFrame(diflist , columns = ["diference"])
            diflist["option"] = [0 , 1 , 2 , 3]
            diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
            diflist = int(diflist["option"])
            
            statem0 = choices[diflist].copy()
            mlist.append(str(statem0))
            num = num+1
            print("Itineration number:" , num)
            print("Actual matrix:")
            print(statem0)

print("Finally!!")

#%% HOW NOT TO DO IT

numlist = list(range(500 , 20001 , 500))
numlist2 = list(range(501 , 20002 , 500))



for u in range(len(numlist2)):
    numlist.append(numlist2[u])


while not (statem0 == finalm).all():
    if not num in numlist:
        for x in xlist:
            for y in ylist:
                zz = statem0[int(x) , int(y)]
                if zz == 0:
                    xpos = int(x)
                    ypos = int(y)
                    
        del possibilities
        possibilities = []
        
        if xpos-1 >= 0:
            possibilities.append([xpos-1 , ypos])
        if xpos+1 < 3:
            possibilities.append([xpos+1 , ypos])
        if ypos-1 >= 0:
            possibilities.append([xpos , ypos-1])
        if ypos+1 < 3:
            possibilities.append([xpos , ypos+1])
            
        del choices
        choices = []
        
        for i in range(len(possibilities)):
            xsub = possibilities[i][0]
            ysub = possibilities[i][1]
            subs = statem0[xsub , ysub]
            statem = statem0.copy()
            statem[xpos , ypos] = subs
            statem[xsub , ysub] = 0
            z = []
            for j in range(len(mlist)):
                if not (str(statem) in mlist):
                    z.append("Yes")
                else:
                    z.append("No")
            if ("No" in z):
                pass
            else:
                choices.append(statem)
                
        if len(choices) > 0:
            pass
        else:
            del mlist
            mlist = []
            del choices
            choices = []
            buglist.append(str(statem0))
            for i in range(len(possibilities)):
                xsub = possibilities[i][0]
                ysub = possibilities[i][1]
                subs = statem0[xsub , ysub]
                statem = statem0.copy()
                statem[xpos , ypos] = subs
                statem[xsub , ysub] = 0
                z = []
                for j in range(len(mlist)):
                    if not (str(statem) in mlist):
                        z.append("Yes")
                    else:
                        z.append("No")
                if ("No" in z):
                    pass
                else:
                    choices.append(statem)
    
        del diflist
        diflist = list()
        
        for i in range(len(choices)):
            dummie = choices[i].copy()
            
            for x in xlist:
                for y in ylist:
                    zz = dummie[int(x) , int(y)]
                    if zz == 1:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 0
                        yfin = 0
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif1 = xdif+ydif
                    elif zz == 2:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 0
                        yfin = 1
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif2 = xdif+ydif
                    elif zz == 3:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 0
                        yfin = 2
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif3 = xdif+ydif
                    elif zz == 4:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 1
                        yfin = 2
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif4 = xdif+ydif
                    elif zz == 5:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 2
                        yfin = 2
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif5 = xdif+ydif
                    elif zz == 6:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 2
                        yfin = 1
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif6 = xdif+ydif
                    elif zz == 7:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 2
                        yfin = 0
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif7 = xdif+ydif
                    elif zz == 8:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 1
                        yfin = 0
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif8 = xdif+ydif
            
            dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
            if len(diflist)>0:
                dif = dif
            diflist.append(dif)
        
        while len(diflist) < 4:
            diflist.append(98)
        
        diflist = pd.DataFrame(diflist , columns = ["diference"])
        diflist["option"] = [0 , 1 , 2 , 3]
        diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
        diflist = int(diflist["option"])
        
        statem0 = choices[diflist].copy()
        mlist.append(str(statem0))
        num = num+1
        print("Itineration number:" , num)
        print("Actual matrix:")
        print(statem0)
    else:
        for x in xlist:
            for y in ylist:
                zz = statem0[int(x) , int(y)]
                if zz == 0:
                    xpos = int(x)
                    ypos = int(y)
                    
        del possibilities
        possibilities = []
        
        if xpos-1 >= 0:
            possibilities.append([xpos-1 , ypos])
        if xpos+1 < 3:
            possibilities.append([xpos+1 , ypos])
        if ypos-1 >= 0:
            possibilities.append([xpos , ypos-1])
        if ypos+1 < 3:
            possibilities.append([xpos , ypos+1])
            
        del choices
        choices = []
        
        for i in range(len(possibilities)):
            xsub = possibilities[i][0]
            ysub = possibilities[i][1]
            subs = statem0[xsub , ysub]
            statem = statem0.copy()
            statem[xpos , ypos] = subs
            statem[xsub , ysub] = 0
            z = []
            for j in range(len(mlist)):
                if not (str(statem) in mlist):
                    z.append("Yes")
                else:
                    z.append("No")
            if ("No" in z):
                pass
            else:
                choices.append(statem)
                
        if len(choices) > 0:
            pass
        else:
            del mlist
            mlist = []
            del choices
            choices = []
            for i in range(len(possibilities)):
                xsub = possibilities[i][0]
                ysub = possibilities[i][1]
                subs = statem0[xsub , ysub]
                statem = statem0.copy()
                statem[xpos , ypos] = subs
                statem[xsub , ysub] = 0
                z = []
                for j in range(len(mlist)):
                    if not (str(statem) in mlist):
                        z.append("Yes")
                    else:
                        z.append("No")
                if ("No" in z):
                    pass
                else:
                    choices.append(statem)
    
        del diflist
        diflist = list()
        
        for i in range(len(choices)):
            dummie = choices[i].copy()
            
            for x in xlist:
                for y in ylist:
                    zz = dummie[int(x) , int(y)]
                    if zz == 1:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 0
                        yfin = 0
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif1 = xdif+ydif
                    elif zz == 2:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 0
                        yfin = 1
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif2 = xdif+ydif
                    elif zz == 3:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 0
                        yfin = 2
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif3 = xdif+ydif
                    elif zz == 4:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 1
                        yfin = 2
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif4 = xdif+ydif
                    elif zz == 5:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 2
                        yfin = 2
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif5 = xdif+ydif
                    elif zz == 6:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 2
                        yfin = 1
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif6 = xdif+ydif
                    elif zz == 7:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 2
                        yfin = 0
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif7 = xdif+ydif
                    elif zz == 8:
                        xpos = int(x)
                        ypos = int(y)
                        xfin = 1
                        yfin = 0
                        
                        xdif = xfin-xpos
                        ydif = yfin-ypos
                        if xdif<0:
                            xdif = -1*xdif
                        if ydif<0:
                            ydif = -1*ydif
                        dif8 = xdif+ydif
            
            dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
            if len(diflist)>0:
                dif = dif
            diflist.append(dif)
        
        while len(diflist) < 4:
            diflist.append(98)
        
        diflist = pd.DataFrame(diflist , columns = ["diference"])
        diflist["option"] = [0 , 1 , 2 , 3]
        diflist = diflist.loc[diflist["diference"] < 70]
        diflist = diflist.sort_values("diference" , ascending = True).sample(1).reset_index(drop = True)
        diflist = int(diflist["option"])
        
        statem0 = choices[diflist].copy()
        mlist.append(str(statem0))
        num = num+1
        print("Itineration number:" , num)
        print("Actual matrix:")
        print(statem0)
print("Finally!!")

#%%

"""
while not (statem0 == finalm).all():
    for x in xlist:
        for y in ylist:
            zz = statem0[int(x) , int(y)]
            if zz == 0:
                print("The 0 is in the position [" , x , "," , y , "]")
                xpos = int(x)
                ypos = int(y)
                
    del possibilities
    possibilities = []
    
    if xpos-1 >= 0:
        possibilities.append([xpos-1 , ypos])
    if xpos+1 < 3:
        possibilities.append([xpos+1 , ypos])
    if ypos-1 >= 0:
        possibilities.append([xpos , ypos-1])
    if ypos+1 < 3:
        possibilities.append([xpos , ypos+1])
        
    del choices
    choices = []
    
    for i in range(len(possibilities)):
        xsub = possibilities[i][0]
        ysub = possibilities[i][1]
        subs = statem0[xsub , ysub]
        statem = statem0.copy()
        statem[xpos , ypos] = subs
        statem[xsub , ysub] = 0
        z = []
        for j in range(len(mlist)):
            if not (str(statem) in mlist):
                z.append("Yes")
            else:
                z.append("No")
        if ("No" in z):
            pass
        else:
            choices.append(statem)

    del diflist
    diflist = list()
    
    for i in range(len(choices)):
        dummie = choices[i].copy()
        
        for x in xlist:
            for y in ylist:
                zz = dummie[int(x) , int(y)]
                if zz == 1:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif1 = xdif+ydif
                elif zz == 2:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 1
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif2 = xdif+ydif
                elif zz == 3:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 0
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif3 = xdif+ydif
                elif zz == 4:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 1
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif4 = xdif+ydif
                elif zz == 5:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 2
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif5 = xdif+ydif
                elif zz == 6:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 1
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif6 = xdif+ydif
                elif zz == 7:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 2
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif7 = xdif+ydif
                elif zz == 8:
                    xpos = int(x)
                    ypos = int(y)
                    xfin = 1
                    yfin = 0
                    
                    xdif = xfin-xpos
                    ydif = yfin-ypos
                    if xdif<0:
                        xdif = -1*xdif
                    if ydif<0:
                        ydif = -1*ydif
                    dif8 = xdif+ydif
        
        dif = dif1 + dif2 + dif3 + dif4 + dif5 + dif6 + dif7 + dif8
        if len(diflist)>0:
            dif = dif+1
        diflist.append(dif)
    
    while len(diflist) < 4:
        diflist.append(98)
    
    diflist = pd.DataFrame(diflist , columns = ["diference"])
    diflist["option"] = [0 , 1 , 2 , 3]
    diflist = diflist.sort_values("diference" , ascending = True).head(1).reset_index(drop = True)
    diflist = int(diflist["option"])
    
    statem0 = choices[diflist].copy()
    mlist.append(str(statem0))
    print(statem0)

"""
#%%

"""
It does not work with any combination as initialm. Maybe I should try to programm
it so that if the algorith didn't find the solution in 1000 iterations, it should
try to find the [[0,2,1] , [6,7,4] , [3,8,5]] matrix (which we know, it find the
solution in 408 iterations).
"""

                        #             ___________
                        #             |         |
                        #             |         |
                        #             |         |
                        #             |         |
                        #             |_________|
                        #      _______|_________|_______
                        
                            #~~~~~~~~~~~$$$$
                            #~~~~~~~~~~$$$$$$
                            #~~~~~~~~~.$$$**$$
                            #~~~~~~~~~$$$'~~`$$
                            #~~~~~~~~$$$'~~~~$$
                            #~~~~~~~~$$$~~~~.$$
                            #~~~~~~~~$$~~~~..$$
                            #~~~~~~~~$$~~~~.$$$
                            #~~~~~~~~$$~~~$$$$
                            #~~~~~~~~~$$$$$$$$
                            #~~~~~~~~~$$$$$$$
                            #~~~~~~~.$$$$$$*
                            #~~~~~~$$$$$$$'
                            #~~~~.$$$$$$$
                            #~~~$$$$$$'`$
                            #~~$$$$$*~~~$$
                            #~$$$$$~~~~~$$.$..
                            #$$$$$~~~~$$$$$$$$$$.
                            #$$$$~~~.$$$$$$$$$$$$$
                            #$$$~~~~$$$*~`$~~$*$$$$
                            #$$$~~~`$$'~~~$$~~~$$$$
                            #3$$~~~~$$~~~~$$~~~~$$$
                            #~$$$~~~$$$~~~`$~~~~$$$
                            #~`*$$~~~~$$$~~$$~~:$$
                            #~~~$$$$~~~~~~~$$~$$'
                            #~~~~~$$*$$$$$$$$$'
                            #~~~~~~~~~~````~$$
                            #~~~~~~~~~~~~~~~`$
                            #~~~~~~~~..~~~~~~$$
                            #~~~~~~$$$$$$~~~~$$
                            #~~~~~$$$$$$$$~~~$$
                            #~~~~~$$$$$$$$~~~$$
                            #~~~~~~$$$$$'~~.$$
                            #~~~~~~~'*$$



