clear all;
clc;
format long

N=input('������һ����ֵ��');

y=single(0.5*(1.5-1/N-1/(N+1)));
disp("��ȷֵy=");
disp(y);%���㾫ȷֵ

BtL(N,y);%���ôӴ�С����ĺ���
LtB(N,y);%���ô�С�������ĺ���

function []=BtL(N,y)%����Ӵ�С����ĺ���
Sn1=single(0);
for a=2:N
    Sn1=Sn1+1/(a*a-1);
end

disp("�ɴ�С����Ľ��Sn1=");
disp(Sn1);

e1=single(abs(Sn1-y));
disp('��ʱ�����e1=');
disp(e1);

if e1==0
    fprintf('��ʱ�ļ�������ȷ����Чλ��Ϊ7λ\n');
else
 for n=1:1:100
    if e1<=(0.5*10^(-n)) && e1>(0.5*10^(-n-1))%��Чλ�����ж�
        disp("��ʱ����Чλ���ǣ�");
        disp(n);
        break
    end
 end
end
end

function[]=LtB(N,y)%�����С�������ĺ���
Sn2=single(0);
for a=N:-1:2
    Sn2=Sn2+1/(a*a-1);
end

disp("��С�������Ľ��Sn2=");
disp(Sn2);

e2=single(abs(Sn2-y));
disp("��С�������Ľ�������e2=");
disp(e2);

if e2==0
    fprintf('��ʱ�ļ�������ȷ����Чλ��Ϊ7λ\n');
else
for n=1:1:100
    if e2<=(0.5*10^(-n)) && e2>(0.5*10^(-n-1))%��Чλ�����ж�
        disp("��ʱ����Чλ���ǣ�");
        disp(n);
        break
    end
end
end
end