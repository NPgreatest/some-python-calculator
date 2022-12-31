import numpy as np

def inpu():
    print("输入：")
    arr = input('')
    inp = np.asarray([float(n) for n in arr.split(' ')])
    map = {'input':inp}
    return map

def insertValue():
    print("第一个模糊量：")
    arr = input('')
    mud = np.asarray([float(n) for n in arr.split(' ')])
    print("第二个模糊量：")
    arr = input('')
    oil = np.asarray([float(n) for n in arr.split(' ')])
    fuzzyArray = {'mud':mud,'oil':oil}
    return fuzzyArray

def fuzzy(a1,a2):
    r = np.zeros(shape=(len(a1),len(a2)), dtype=float)
    for i in range(len(a1)):
        for j in range(len(a2)):
            r[i][j]=min(a1[i],a2[j])
    return r


def maximum(a1,a2):
    #print(a1,a2)
    res=0
    for i in range(len(a1)-1):
        res=max(min(a1[i],a2[i]),min(a1[i+1],a2[1+i]),res)
    return res

def fuzzySynthesis(a1,a2):
    #print(a1, a2)
    r = np.zeros(shape=(1,len(a1)), dtype=float)
    a = []
    res=[]
    for i in range(len(a2[0])):
        a.clear()
        for j in range(len(a2)):
            a.append(a2[j][i])
        res.append(maximum(a1.copy(),a.copy()))
    return res

def maxMin(x, y):
    z = []
    for x1 in x:
        for y1 in y.T:
            z.append(max(np.minimum(x1, y1)))
    return np.array(z).reshape((x.shape[0], y.shape[1]))


r1 = np.loadtxt("load1.txt")
r2 = np.loadtxt("load2.txt")
print("模糊合成：\n",maxMin(r1,r2))

fuzzyArray = insertValue()

print("\n模糊关系R")
a1 = fuzzy(fuzzyArray.get('mud'),fuzzyArray.get('oil'))
print(a1)

while(1):
    inp = inpu()
    a2=fuzzySynthesis(inp.get('input'),a1)
    print("\n\n模糊输出(无穷循环)：",a2)
