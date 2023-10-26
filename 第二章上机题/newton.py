#数值分析第二次上机作业：
#自定义函数f(x)，这里定义f(x)=x^3/3-x
def Newton(x0,c,epsilon):
    def f(x):
        f=x**3/3-x
        return f
    def f_grad(x,c):
        f_grad=x**2-1
        if f_grad==0:
            f_grad=f_grad+c
        return f_grad
    def newton_method(x0,epsilon):
        xi=x0
        while True:
            xi_plus_1=xi-f(xi)/f_grad(xi,c)
            if abs(xi_plus_1-xi)<epsilon:
                break
            #print(xi)
            xi=xi_plus_1
        return xi
    return newton_method(x0,epsilon)
#使用示例：
#x0=1
#c=0.0001
#epsilon=0.0001
#root=Newton(x0,c,epsilon)
#print("方程的根为：",root)