import numpy as np
import ez as ez
from numpy.linalg import solve

marketPrice = [98, 99, 90, 93]  # 市场价格
rate = [3, 5, 2, 4]  # 票息率
originalValue = 100


def poly_3():
    #****************标识需要修改（在计算三次多项式插值情况下）
    year1=1#期限  ***********************
    year2=2#期限 ***********************
    year3=3#期限  ***********************
    year4=4#期限  ***********************
    a=np.mat([[pow(year1,3),pow(year1,2),pow(year1,1),1.0],[pow(year2,3),pow(year2,2),pow(year2,1),1.0],
              [pow(year3,3),pow(year3,2),pow(year3,1),1.0],[pow(year4,3),pow(year4,2),pow(year4,1),1.0]])
    b=np.mat([0.0158,0.0214,0.0258,0.0295]).T    #常数项列矩阵************************
    x=solve(a,b)        #方程组的解
    year=3.25#所求的期限  ***********************
    p=[year,year,year,year]
    mi=[3.0,2.0,1.0,0.0]#化为幂次
    bianliang=np.power(p,mi)
    m=bianliang * x
    print(x)
    print(m)




def xuepanfa():
    num = len(marketPrice)
    a = [[0 for col in range(num)] for row in range(num)]

    for i in range(num):
        for j in range(i + 1):
            if j == i:
                a[i][j] = originalValue + rate[i]
            else:
                a[i][j] = rate[i]
    a = np.mat(a)
    b = np.mat(marketPrice).T

    B = solve(a, b)  # 贴现因子
    R = -np.log(B)
    for i in range(num):
        R[i] *= 100 / (i + 1)
    print('B:\n' + str(B) + '\n')
    print('R(%):\n' + str(R) + '\n')


def duration(final,rate,yttn,T,n,delta_yttn):
    c=d=V_t=Vt0=Vt1=0 #货币凸度，货币久期，现值，基点价格-1，基点价格+1
    for i in range(1,int(n/T)+1):
        V_t+=final*rate*T*np.exp(-1*yttn*i*T)
        Vt0 += final * rate * T * np.exp(-1 * (yttn-0.01) * i * T)
        Vt1 += final * rate * T * np.exp(-1 * (yttn+0.01) * i * T)
        d+=T*i*final*rate*T*np.exp(-1*yttn*i*T)
        c+=pow(T*i,2)*final*rate*T*np.exp(-1*yttn*i*T)
    V_t+=final*np.exp(-1*yttn*n)
    Vt0 += final * np.exp(-1 * (yttn - 0.01) * n)
    Vt1 += final * np.exp(-1 * (yttn + 0.01) * n)
    d+=n*final*np.exp(-1*yttn*n)
    c+=pow(n,2)*final*np.exp(-1*yttn*n)
    c/=2
    print("现值=",V_t,"\n货币久期=",d,"\n久期=",d/V_t,"\n货币凸度=",c,"\n凸度=",c/V_t,"\n基点价格=",abs(Vt0-Vt1)/2*0.01)
    print("若到期收益率变动为",delta_yttn*100,"%时， \"久期\" 方法计算的债券价格变动为",-1*d*delta_yttn)
    print("若到期收益率变动为",delta_yttn*100,"%时，\"久期+凸度\" 方法计算的债券价格变动为",-1*d*delta_yttn+c*pow(delta_yttn,2))



#复利频率 利率 目标频率(连续复利为0)
print("转化后的\"x年计息一次/连续复利\"为：",ez.convert(0.5,0.006,0.25),"\n")

print("转化后的\"x年计息一次/连续复利\"为：",ez.convert(0.25,0.052,0),"\n")
print("转化后的\"x年计息一次/连续复利\"为：",ez.convert(0.25,0.055,0),"\n")
#year1 rate1 year2 rate2
print("解得远期利率：",ez.remote(1,0.036,2,0.038),"\n")
#面值 年限 票息率 付息频率 市场价格
print("解得到期收益率：",ez.yttn(100,2,0.04,1,96.0446),"\n")
#面值 年限 票息率 付息频率 投资期 到期收益率 再投资利率 投资期后到期收益率
ez.total_return(100,20,0.08,0.5,3,0.0784,0.06,0.07)
poly_3()
xuepanfa()
#final,rate,yttn,T,n,delta_yttn 久期
duration(100,0.08,0.06,1,3,0.01)
#year1 rate1 year2 rate2 target_year
print("\n插值法：",ez.chazhi(0.5,0.036,1,0.039,0.75)*100,"%")
