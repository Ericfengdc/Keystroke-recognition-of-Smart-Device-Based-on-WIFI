function [y]=ButterworthFilter2(x)
fn=1000;%采样频率
ap=0.05;%通带最大衰减
as=6;%阻带最大衰减

wp=2;%通带截止频率，大值更平坦
ws=20; %阻带截止频率，小值更平坦
wpp=wp/(fn/2);
wss=ws/(fn/2); %归一化;
[n wn]=buttord(wpp,wss,ap,as); %计算阶数截止频率
[b a]=butter(n,wn); %计算N阶巴特沃斯数字滤波器系统函数分子、分母多项式的系数向量b、a。

mmyy=filtfilt(b,a,x); %滤波b、a滤波器系数，my滤波前序列
y=mmyy;
