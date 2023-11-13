from test_4 import hangfanshu,Hilbert,matrix_qiuni
import numpy as np
import time
start_time=time.time()
#x_cal=np.zeros(20,20)
for n in range (1,21):
    H=Hilbert(n)
    #print("H\n",H)
    x_1=np.ones(len(H))
    x=x_1[:,np.newaxis]
    #print("x\n",x)
    b=np.dot(H,x)
    #print("b\n",b)
    #x_cal = np.linalg.solve(H, b)
    x_cal=np.dot(matrix_qiuni(H),b)
    print("n=",n,"时：")
    print("x-x_cal：\n",x-x_cal)
    print("x-x_cal的无穷范数：",hangfanshu(x-x_cal))
    print("b-H*x_cal\n",b-np.dot(H,x_cal))
    print("b-H*x_cal的无穷范数：",hangfanshu(b-np.dot(H,x_cal)))
end_time=time.time()
run_time=end_time-start_time
print("运行的时间为：",run_time)