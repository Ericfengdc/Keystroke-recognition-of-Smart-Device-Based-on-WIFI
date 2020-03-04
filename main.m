clear all;
end_noise = 8000;%5000%最后有噪声，需要去除一部分
%csi_trace = read_bf_file('E:/csi_reader/CSI_reader-master/matlab/dat_file/music-2.25m-ang00.dat');
%csi_trace = read_bf_file('C:\Users\Administrator\Desktop\music\fdc1126\fdc\word\word_N0.dat');
csi_trace = read_bf_file('I:\CSI_file\fdc0115_3\train20.dat');
antenna_num = 3;
%read_bf_file('E:\collected_CSI_file_dat\fdc0107\no_straight_close2r_75cm_G0.dat'); 
%words = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
% csitrace = {};
% for i = 1:26
%     filepath = ['C:\Users\Administrator\Desktop\music\fdc1126\fdc\word\word_',words(i),'0.dat'];
%     c sitrace = [csitrace;{read_bf_file(filepath)}];
%     %action = [action;{data(time_duration:i)}];
% end
% for word_index = 1:26
%     csi_trace = csitrace{word_index};
%分析第1个 

global index_start ;%去除前5s内容
index_start = 8000;
global index_end;
index_end = size(csi_trace,1)-end_noise;
global var_length;
var_length = 1.6e3;
for l = index_start:index_end  %取50个数据包的数据
    csia = get_scaled_csi(csi_trace{l});%提取csi矩阵 csia(接收index,发射index,子载波index)
    for i = antenna_num:antenna_num  %1个发射天线
        for k = 3:3   %30个子载波数据,选择第一个
           B(1,k,l-index_start+1) = csia(1,i,k);               
        end
    end 
end 
%B = B(:,:,index_start:index_end);

[a,b,c] = size(B);
B = ButterworthFilter2(reshape(abs(B),1,a*b*c));
var_temp = zeros(1,c-var_length);
mean_temp = zeros(1,c-var_length);
std_temp = zeros(1,c-var_length);
for i= 1:c-var_length
    
    part_B = B(i:i+var_length);
    mean_temp(var_length+i) = mean(part_B);
    var_temp(var_length+i) = var(part_B);
    std_temp(var_length+i) = std(part_B);
end
% subplot(2,2,1);
plot(abs(squeeze(reshape(B,a,b,c)).'));
title('wp=2ws=10');
xlabel('Sample');
ylabel('Amplitude');
xlim([1,index_end-index_start]);


% subplot(2,2,2);plot(var_temp);title('Var of CSI Amplitude');xlim([1,index_end-index_start]);
% subplot(2,1,2);
% subplot(2,2,3);plot(std_temp);title('STD of CSI Amplitude');xlim([1,index_end-index_start]);%save('std_of_straight_way','std_temp');
% ylim([0,0.5])
% hold on;
% line([0,9e4],[0.15,0.15]);
% hold off,
% subplot(2,2,4);plot(mean_temp);title('Mean of CSI Amplitude');xlim([1,index_end-index_start]);

%find_action_in_std(std_temp,B,words(word_index));
find_action_in_std(std_temp,B,0);
clearvars -except csitrace word_index words end_noise csi_trace;
%end;


