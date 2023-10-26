import numpy as np
import time
start_time = time.time()
def cal_jingquezhi(N):
    jingquezhi=np.float32(1/2*(3/2-1/N-1/(N+1)))
    return np.float32(jingquezhi)

def cal_min2max(N):
    SN_min2max=np.float32(0)
    i=0
    list_min2max=range(2,N+1)
    for i in list_min2max:
        SN_min2max+=np.float32(1/(i*i-1))
    return np.float32(SN_min2max)
def cal_max2min(N):
    SN_max2min=np.float32(0)
    i=0
    list_max2min=range(N,1,-1)
    for i in list_max2min:
        SN_max2min+=np.float32(1/(i*i-1))
    return np.float32(SN_max2min)
def cal_youxiaowei(m):
    if '.' in str(m):
        m_new=(str(m).replace(".",''))
        m=m_new
    m=(str(m).rstrip('0'))
    m=(str(m).lstrip('0'))
    digits = len(str(m))
    return digits
def cal_wucha(jingquezhi,jisuanzhi):
    wucha=abs(jingquezhi-jisuanzhi)
    return wucha
S_jihe=(100,10000,1000000)
for i in (S_jihe):
    print('\n计算的N值为：',i,'\t精确值：',cal_jingquezhi(i))
    print('\n从小到大计算值：',cal_min2max(i),'\t从小到大误差：',cal_wucha(cal_jingquezhi(i),cal_min2max(i)),'\t从小到大计算有效位数：',cal_youxiaowei(cal_min2max(i)))
    print('\n从大到小计算值：',cal_max2min(i),'\t从大到小误差：',cal_wucha(cal_jingquezhi(i),cal_max2min(i)),'\t从大到小计算有效位数：',cal_youxiaowei(cal_max2min(i)))
    print('\n')
end_time = time.time()
run_time = end_time - start_time
print(f"程序运行耗时: {run_time} 秒")