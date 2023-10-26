#数值分析第二次上机题(2)①
from newton import Newton

#x0=1
step=0.000001
c=0.0001
epsilon=0.0001
deta0=0
i=0
while(True):
    i = i + 1
    deta = deta0 + (i-1)*step
    if Newton(deta, c, epsilon)>1:
        break
#root = Newton(x0, c, epsilon)
deta_max=deta-step
# 打印结果
print("找到的deta为：", deta_max)
print("x0=-1000:",Newton(-1000, c, epsilon))#x0∈（-∞，-1）
print("x0=-50:",Newton(-50, c, epsilon))#x0∈（-∞，-1）
print("x0=-3:",Newton(-3, c, epsilon))#x0∈（-∞，-1）
print("x0=-0.9:",Newton(-0.9, c, epsilon))#x0∈（-1，-deta）
print("x0=-0.85:",Newton(-0.85, c, epsilon))#x0∈（-1，-deta）
print("x0=-0.8:",Newton(-0.8, c, epsilon))#x0∈（-1，-deta）
print("x0=-0.7:",Newton(-0.7, c, epsilon))#x0∈（-deta，deta）
print("x0=0:",Newton(0, c, epsilon))#x0∈（-deta，deta）
print("x0=0.7:",Newton(0.7, c, epsilon))#x0∈（-deta，deta）
print("x0=0.8:",Newton(0.8, c, epsilon))#x0∈（deta，1）
print("x0=0.85:",Newton(0.85, c, epsilon))#x0∈（deta，1）
print("x0=0.9:",Newton(0.9, c, epsilon))#x0∈（deta，1）
print("x0=3:",Newton(3, c, epsilon))#x0∈（1,+∞）
print("x0=50:",Newton(50, c, epsilon))#x0∈（1,+∞）
print("x0=1000:",Newton(1000, c, epsilon))#x0∈（1,+∞）