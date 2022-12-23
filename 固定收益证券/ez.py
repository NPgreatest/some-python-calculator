import sympy as sy
import numpy as np
def yttn(final,n,rate,T,Vm):
    x= sy.Symbol('x')
    eq=-Vm
    for i in range(1, int(n / T) + 1):
        eq=eq+final*rate*sy.E**(-x*i*T)
    eq=eq+final*sy.E**(-x*n)
    print("方程：",eq)
    res = sy.solve(eq, x)
    return res

def remote(y1,r1,y2,r2):
    return ((y2*r2-y1*r1)/(y2-y1))

def convert(T,r,tarT):
    if(tarT==0):
        return (np.log(pow(1+T*r,1/T)))
    return (pow(1+r*T,tarT/T)-1)/tarT

#            面值 年限 票息率 付息频率 投资期 到期收益率 再投资利率 投资期后到期收益率
def total_return(final,n,rate,T,invest_n,yttn,re_r,remote_r):
    buy=sale=income=0
    for i in range(int(invest_n / T)):
        income+=final*T*rate*np.exp(re_r*i*T)
    print("未来",invest_n,"年票息收入的终值预期=",income)
    for i in range(1,int((n-invest_n) / T)+1):
        sale+=final*T*rate*np.exp(-1*remote_r*i*T)
    sale += final*np.exp(-1 * remote_r * (n-invest_n))
    print(invest_n,"年后预期出售价格=",sale,"   因此总终值=",sale+income)
    buy=final #(可更改)
    print(invest_n,"年后总收益率为(连续复利)：",np.log((sale+income)/buy)/invest_n,"\n")


def chazhi(y1,r1,y2,r2,tary):
    return ((y2-tary)*r1+(tary-y1)*r2)/(y2-y1)