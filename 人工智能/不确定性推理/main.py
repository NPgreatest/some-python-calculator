def PowerSetsBinary(items):
  N = len(items)
  b=[]
  for i in range(2**N):
    zj =''
    for j in range(N):
      if(i >> j ) % 2 == 1:
        zj=zj+zj.join(items[j])
    b.append(zj)
  return b
str=input('输入样本空间(ab)\n')
r=[]
map1={}
map2={}
kk=1
mm={}
def bel(tar):
    res=0
    subset = PowerSetsBinary(r)
    for x in subset:
        if (x == ''): continue
        if(bool(set(x).issubset(tar))):
            res+=mm[x]
    return res


for i in str: r.append(i)
str=input('输入概率分配函数M1(以0结束)(ab=0.3)\n')
while(str!='0'):
    t=str.split('=')
    map1.update({t[0]:float(t[1])})
    str=input()
str=input('输入概率分配函数M2(以0结束)(ab=0.3)\n')
while(str!='0'):
    t=str.split('=')
    map2.update({t[0]:float(t[1])})
    str=input()
print("先计算K：\nK=1-(",end='')
for i in map1:
    for k in map2:
        if(not bool(set(i).intersection(set(k)))):
            kk-=map1[i]*map2[k]
            print("+M1({"+i+"})M2({"+k+"})",end='')
print(")=",kk)

subset=PowerSetsBinary(r)
for x in subset:
    if(x==''):continue
    print("M({"+x+"})=(1/K) * [",end='')
    sum=0
    for i in map1:
        for k in map2:
            if ((set(i).intersection(set(k)))==set(x)):
                print("+M1({"+i+"})M2({"+k+"})",end='')
                sum+=map1[i]*map2[k]
    print("]=",sum/kk)
    mm.update({x:sum/kk})

print("下面计算Bel()信任函数：")
for x in subset:
    if(x==''):continue
    print("Bel("+x+")=",bel(set(x)))
print("下面计算Pl()似然函数：")
for x in subset:
    if(x==''):continue
    print("Pl("+x+")=",1-bel(set(r)-set(x)))

while(1):
    input()