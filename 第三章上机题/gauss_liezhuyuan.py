import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    
    # 增广矩阵
    augmented_matrix = np.concatenate((A, b), axis=1).astype(float)
    
    # 初等行变换
    for i in range(n):
        # 选取主元
        max_index = np.argmax(abs(augmented_matrix[i:, i])) + i
        augmented_matrix[[i, max_index]] = augmented_matrix[[max_index, i]]
        
        # 消元过程
        for j in range(i+1, n):
            ratio = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j, i:] -= ratio * augmented_matrix[i, i:]
    
    # 回代过程
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented_matrix[i, n] - np.dot(augmented_matrix[i, i:n], x[i:n])) / augmented_matrix[i, i]
    
    return x

if __name__ == '__main__':
    A=[
    [1,2,3],
    [0,1,2],
    [2,4,1]
    ]
    b=[
    [14],
    [8],
    [13]
    ]
    '''
    A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

    b = np.array([[8], [-11], [-3]])
    '''
    solution = gaussian_elimination(A, b)
    print("方程组的解为：", solution)