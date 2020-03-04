%untitled
clear all;
%csi_trace = read_bf_file('E:/csi_reader/CSI_reader-master/matlab/dat_file/music-2.25m-ang00.dat');
%csi_trace = read_bf_file('C:\Users\Administrator\Desktop\music\fdc1126\fdc\word\word_Y0.dat');
words = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
csitrace = {};
for i = 1:26
    filepath = ['C:\Users\Administrator\Desktop\music\fdc1126\fdc\word\word_',words(i),'0.dat'];
    csitrace = [csitrace;{read_bf_file(filepath)}];
    %action = [action;{data(time_duration:i)}];
end
for word_index = 1:26
    csi_trace = csitrace{word_index};
%分析第1个 
global index_start ;
index_start = 3000;
global index_end;
index_end = size(csi_trace,1);
global var_length;
var_length = 1.6e3;
for l = index_start:index_end  %取50个数据包的数据
    csia = get_scaled_csi(csi_trace{l});%提取csi矩阵 csia(接收index,发射index,子载波index)
    for i = 1:1  %1个发射天线
        for k = 1:1   %30个子载波数据,选择第一个
           B(1,k,l) = csia(1,i,k);               
        end
    end 
    %size((B))
    %squeeze通过移除第一个单维度将csi变成3*30的矩阵
    %db将线性空间变成以十为底的对数空间
    %.'转置得到30*3的矩阵
    %plot(Y)如果Y是m×n的数组，以1:m为X横坐标，Y中的每一列元素为Y坐标，绘制n条曲线
    %hold on%当前轴及图像保持而不被刷新，准备接受此后将绘制的图形，多图共存
end 
B = B(:,:,index_start:index_end);
[a,b,c] = size(B);
B = ButterworthFilter2(reshape(abs(B),1,a*b*c));
%%%%%%%%%%频域信息%%%%%%%%%%%
% b_fft=fft(B);
% b_abs=2*db(abs(b_fft))/1000;
% figure(2)
% plot(b_abs(1:10:length(b_fft)/2));
% xlim([1,100])
% xlabel('f(Hz)');
% ylabel('Amplitude');
%%%%%%%%%%频域信息%%%%%%%%%%%
var_temp = zeros(1,c-var_length);
mean_temp = zeros(1,c-var_length);
std_temp = zeros(1,c-var_length);
for i= 1:c-var_length
    
    part_B = B(i:i+var_length);
    mean_temp(var_length+i) = mean(part_B);
    var_temp(var_length+i) = var(part_B);
    std_temp(var_length+i) = std(part_B);
end
find_action_in_std(std_temp,B,words(word_index));
%find_action_in_std(std_temp,B,0);
clearvars -except csitrace word_index words ;
end;
