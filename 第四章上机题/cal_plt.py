from def_dingyihanshu import cal_hangfanshutiaojianshu,Hilbert
import numpy as np
#import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
'''
for i in range(1,21):
    print('n=',i,"时的行范数条件数",cal_hangfanshutiaojianshu(Hilbert(i)))
'''
tiaojianshu=np.zeros(20)
for i in range(20):
    tiaojianshu[i]=cal_hangfanshutiaojianshu(Hilbert(i+1))
    print('n=',(i+1),"时的行范数条件数",tiaojianshu[i])
tiaojianshu_log=np.log(tiaojianshu)
x=np.linspace(1,20,num=20)
y = np.interp(x, x, tiaojianshu_log)
plt.plot(x,y,'o')
plt.plot(x,y, '-x') #黄色的区域
plt.xticks(x)
plt.show()