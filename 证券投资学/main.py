import numpy as np
import sympy as sy
import matplotlib.pyplot as plt

class stock:
    er=0
    std=0
    def __init__(self,er,std):
        self.er=er
        self.std=std

def best(a,b,rf,rou,tar_e):
    cov=rou*a.std*b.std
    print('先解无风险收益率：')
    x=sy.Symbol('x')
    eq=(x*a.std)**2+((1-x)*b.std)**2+2*x*(1-x)*cov
    print('构造方程为：',eq)
    res=sy.solve(eq,x)[0]
    print(f'解得wa=x={res},wb={1-res}\nE(r)={res}*{a.er}+{1-res}*{b.er}={res*a.er+(1-res)*b.er}')
    print('---------------------------------------------')
    wa=(pow(b.std,2)-cov)/(pow(a.std,2)+pow(b.std,2)-2*cov)
    wb=1-wa
    er=wa*a.er+wb*b.er
    sigmap=pow(pow(wa*a.std,2)+pow(wb*b.std,2)+2*wa*wb*cov,0.5)
    sharp=(er-rf.er)/sigmap
    print(f'最小方差组合,首先计算协方差：\nCOV(X,Y)=rou_XY x sigma_a* sigma_b  \n={rou} * {a.std}* {b.std}={cov}')
    print(f'再计算对于A和B的投资比率：\nwmina=公式=代数={wa}\nwminb=1-wmina={1-wa}')
    print(f'期望收益：E(r_p)=waE(ra)+wbE(rb)={wa}{a.er}+{wb}{b.er}={er}')
    print(f'标准差：sigmap=公式={sigmap}')
    print(f'夏普比率=({er}-{rf.er})/({sigmap})={sharp}')
    print('---------------------------------------------')
    print('最优风险投资组合：,',end='')
    Ra=a.er-rf.er
    Rb=b.er-rf.er
    print(f'先计算超额收益，\nE(Ra)=E(ra)-rf={a.er*100}%-{rf.er*100}%={Ra*100}%\nE(Rb)=E(rb)-rf={b.er*100}%-{rf.er*100}%={Rb*100}%')
    wwa=(Ra*pow(b.std,2)-Rb*cov)/(Ra*pow(b.std,2)+Rb*pow(a.std,2)-(Ra+Rb)*cov)
    wwb=1-wwa
    eer=wwa*a.er+wwb*b.er
    sigmapp=pow(pow(wwa*a.std,2)+pow(wwb*b.std,2)+2*wwa*wwb*cov,0.5)
    sharp2=(eer-rf.er)/sigmapp
    print(f'投资在A上的比例wa=公式=代数={wwa}\n投资在A上的比例wa=1-wa=代数={wwb}')
    print(f'期望收益:E(r_p)=waE(ra)+wbE(rb)={wwa}{a.er}+{wwb}{b.er}={eer}')
    print(f'标准差：sigmap=公式={sigmapp}')
    print(f'夏普比率=({eer}-{rf.er})/({sigmapp})={sharp2}')
    tar_e=tar_e if tar_e!=0 else eer
    print('---------------------------------------------')
    print(f'计算在收益率要求为{tar_e}时的资产配置：')
    sigmat=(tar_e-rf.er)/sharp2
    wft=1-(tar_e-rf.er)/(eer-rf.er)
    print(f'构造资本配置线：公式：带入:\n{tar_e}={rf.er}+{sharp2}* sigmap\nsigma={sigmat}')
    print('下面分别求国库券，A，B的投资比例')
    print(f'wf=1-({tar_e}-{rf.er})/({eer}-{rf.er})={wft}')
    print(f'wa=(1-{wft})*{wwa}={(1-wft)*wwa}')
    print(f'wb=(1-{wft})*{wwb}={(1 - wft) * wwb}')




a = stock(0.2, 0.25)
b = stock(0.06, 0.05)
rf = stock(0.03, 0)
rou = 0.1
tar=0.07 #如果输入0则为最优风险配置123


c=stock(0.1,0.05)
d=stock(0.15,0.1)
rf2=stock(0.03,0)
rou2=-1.0
best(a,b,rf,rou,tar)



