import numpy as np
import random
x = np.zeros([9,9,9], dtype = int)
index=0
for i in np.nditer(x,op_flags=['readwrite']):
    if index == 9:
        index=0
    i[...] = index
    index+=1
def wfc(xy,num):
    for i in np.nditer(x[xy[0]][xy[1]],op_flags=['readwrite']):
        if i != num:
            i[...]=9
    index=0
    while index <= 8:
        for i in np.nditer(x[xy[0]][index],op_flags=['readwrite']):
            if (i == num)and(index != xy[1]):
                i[...]=9
        for i in np.nditer(x[index][xy[1]],op_flags=['readwrite']):
            if (i == num)and(index != xy[0]):
                i[...]=9
        index+=1
    return x
def S(xy):
    index = -1
    for i in x[xy[0]][xy[1]]:
        if i != 9:
            index+=1
    return index
def choose():
    index=[0,0,9,[0,0]]
    while index[0] <= 8:
        while index[1] <= 8:
            if (S((index[0],index[1]))<index[2])and(S((index[0],index[1]))!=0):
                index[2]=S((index[0],index[1]))
                index[3]=[index[0],index[1]]
            index[1]+=1
        index[1]=0
        index[0]+=1
    return (index[3][0],index[3][1])
def ran_number(xy):
    return random.choice(x[xy[0]][xy[1]])
wfc((0,1),7)
wfc((1,3),7)
wfc((1,5),7)
wfc((1,8),7)
wfc((2,1),5)
wfc((2,2),6)
wfc((2,4),3)
wfc((2,6),9)
wfc((3,2),1)
wfc((3,3),4)
wfc((4,2),4)
wfc((4,3),2)
wfc((4,4),5)
wfc((5,1),8)
wfc((5,4),1)
wfc((6,1),1)
wfc((6,3),9)
wfc((6,7),8)
wfc((7,1),4)
wfc((7,3),3)
wfc((7,5),2)
wfc((7,6),7)
wfc((7,8),9)
wfc((8,1),9)
wfc((8,2),7)
wfc((8,6),6)
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
wfc(choose(),ran_number(choose()))
print(wfc(choose(),ran_number(choose())))