import numpy as np
def Hilbert(num):
    matrix_H=np.zeros((num,num))
    for i in range(num):
        for j in range(num):
            matrix_H[i][j]=1/(i+1+j+1-1)
    return matrix_H
'''
def hangfanshu(arr):
    n=len(arr[0])
    arr_max=0
    for i in range(n):
        arr_max=arr_max+arr[0][i]
    return arr_max
'''
def hangfanshu(arr):
    n=len(arr[0])
    sum_hang=np.zeros(n)
    for i in range(n):
        sum_hang[i]=np.sum(np.abs(arr[i]))
    max_hang=np.max(sum_hang)
    return max_hang
def matrix_qiuni(arr):
    n=len(arr[0])
    A_inv = np.linalg.inv(arr)
    return A_inv

def cal_hangfanshutiaojianshu(arr):
    hangfanshutiaojianshu=hangfanshu(arr)*hangfanshu(matrix_qiuni(arr))
    return hangfanshutiaojianshu
if __name__ == '__main__':
    '''
    matrix_H=[
        [1,1/2,1/3],
        [1/2,1/3,1/4],
        [1/3,1/4,1/5],
    ]'''
    '''
    n=3
    matrix_H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            matrix_H[i][j]=1/(i+1+j+1-1)
    #print("行范数：",hangfanshu(matrix_H))
    cond_hang=hangfanshu(matrix_H)*hangfanshu(matrix_qiuni(matrix_H))
    #print("行范数条件数：",cond_hang)
    #print(cal_hangfanshutiaojianshu(matrix_H))
    #print(matrix_H)
    #print(matrix_qiuni(matrix_H))
    b=[
        [2,1],
        [1,1]
    ]
    print(cal_hangfanshutiaojianshu(b))
    '''
    Hilbert_test_3=Hilbert(3)
    print(Hilbert_test_3)
    print(hangfanshu(Hilbert_test_3))
    