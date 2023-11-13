from gauss_liezhuyuan import  gaussian_elimination
import time
start_time=time.time()
R=[
    [31,-13,0,0,0,-10,0,0,0],
    [-13,35,-9,0,-11,0,0,0,0],
    [0,-9,31,-10,0,0,0,0,0],
    [0,0,-10,79,-30,0,0,0,-9],
    [0,0,0,-30,57,-7,0,-5,0],
    [0,0,0,0,-7,47,-30,0,0],
    [0,0,0,0,0,-30,41,0,0],
    [0,0,0,0,-5,0,0,27,-2],
    [0,0,0,-9,0,0,0,-2,29]
]
V=[
    [-15],
    [27],
    [-23],
    [0],
    [-20],
    [12],
    [-7],
    [7],
    [10],
]
I = gaussian_elimination(R, V)
format_I=[f"{x:.5g}"for x in I]
print("方程组的解为：",format_I)
end_time=time.time()
run_time = end_time - start_time
print(f"程序运行耗时: {run_time} 秒")