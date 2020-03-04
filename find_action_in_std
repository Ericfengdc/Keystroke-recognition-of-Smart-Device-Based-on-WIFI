function dtw_result = find_action_in_std(x,data,word)%input：std,data
% x = load('std_of_straight_way.mat');
% x = x.std_temp;
action_flag = 0;
time_duration = 0 ;
action={};
threshold = 0.15;%default:0.15
threshold_last_time =1200
for i = 1:size(x,2)
    if x(i)>threshold && action_flag == 0  %0.1认为有action，持续时间1200认为action结束。
        action_flag = 1;
        fprintf('action start at%d，本次动作距离上一次时间为%d\n ',i,i-time_duration);
        time_duration=i;
    end
    if x(i)<threshold && action_flag == 1
        action_flag = 0;%置为0，如果时间小于1.2s认为不是action，不统计
        if i-time_duration>threshold_last_time
            if time_duration-1000>1   %防止超出维度
                action = [action;{data(time_duration-1000:i-1000)}];%方差有延时效应，所以以0.25s向前推移
            else
                action = [action;{data(time_duration:i)}];
            end
            fprintf('action end at%d,本次动作持续时间为%d\n\n',i,i-time_duration);
            time_duration=i;
        end
    end
end
size(action)

filepath=['E:\collected_CSI_file_mat\fdc0115\train_test251516_r3.mat',word];
save(filepath,'action');


