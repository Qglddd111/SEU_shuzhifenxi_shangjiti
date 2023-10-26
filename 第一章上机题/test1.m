clear all;
clc;
format long

N=input('请输入一个数值：');

y=single(0.5*(1.5-1/N-1/(N+1)));
disp("精确值y=");
disp(y);%计算精确值

BtL(N,y);%调用从大到小计算的函数
LtB(N,y);%调用从小到大计算的函数

function []=BtL(N,y)%定义从大到小计算的函数
Sn1=single(0);
for a=2:N
    Sn1=Sn1+1/(a*a-1);
end

disp("由大到小计算的结果Sn1=");
disp(Sn1);

e1=single(abs(Sn1-y));
disp('此时的误差e1=');
disp(e1);

if e1==0
    fprintf('此时的计算结果精确，有效位数为7位\n');
else
 for n=1:1:100
    if e1<=(0.5*10^(-n)) && e1>(0.5*10^(-n-1))%有效位数的判断
        disp("此时的有效位数是：");
        disp(n);
        break
    end
 end
end
end

function[]=LtB(N,y)%定义从小到大计算的函数
Sn2=single(0);
for a=N:-1:2
    Sn2=Sn2+1/(a*a-1);
end

disp("由小到大计算的结果Sn2=");
disp(Sn2);

e2=single(abs(Sn2-y));
disp("由小到大计算的结果的误差e2=");
disp(e2);

if e2==0
    fprintf('此时的计算结果精确，有效位数为7位\n');
else
for n=1:1:100
    if e2<=(0.5*10^(-n)) && e2>(0.5*10^(-n-1))%有效位数的判断
        disp("此时的有效位数是：");
        disp(n);
        break
    end
end
end
end