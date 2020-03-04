#使用3根天线联合估计准确率，先获取从matlab那边得到的每个击键对应的3个天线的波形
# 然后将他们按照数字的不同append到不同的list，比较受害者输入的数字的3个波形和
# 模板库中的三个波形的dtw平均距离之和作为最终评价标准
# CSI是所有的数据，CSI[0]表示第1个采集的1234567890的所有CSI，CSI[0][0]表示第一个1234567890的的一号天线的所有CSI
# CSI[0][0][0]表示第一个1234567890的一号天线的第一个CSI序列，即1的序列#
from functions import my_loadmat
from functions import get_pure_wave
import scipy.io as scio
import time
from fastdtw import fastdtw
import numpy as np
import matplotlib.pyplot as plt
import sys

index_train = ['1','2','3','4','5','6','7','8','9','11','12','13','14','15' ]#
# number_test = ['2','5','1','5','1','6']
number_test = ['1','2','3','4','5','6','7','8','9','0']
antenna = ['1','2','3']
dis_mat = np.zeros(((len(number_test),10,len(antenna))))
CSI_train = []
CSI_test = []
for i in range(len(index_train)):
    temp = []
    for j in range(len(antenna)):
        temp.append(my_loadmat(
            'E:/collected_CSI_file_mat/fdc0115/train' + index_train[i] + '_r' + antenna[j]))
    CSI_train.append(temp)
CSI_train = np.array(CSI_train)

for i in range(len(antenna)):
    CSI_test.append(my_loadmat(
        'E:/collected_CSI_file_mat/fdc0115/train10_r' + antenna[i]))
CSI_test = np.array(CSI_test)

#CSI序列零均值化——train#
# for i in range(len(CSI_train)):
#     for j in range(len(CSI_train[i])):
#         for k in range(len(CSI_train[i][j])):
#             CSI_train[i][j][k] = CSI_train[i][j][k] - np.mean(CSI_train[i][j][k])
# for i in range(len(CSI_test)):
#     for j in range(len(CSI_test[i])):
#         CSI_test[i][j] = CSI_test[i][j] - np.mean(CSI_test[i][j])
#         if i==0:
#             plt.figure()
#             plt.plot(get_pure_wave(CSI_test[i][j]))
# plt.show()

# 之前写给每次采集都是同一个数字的逻辑
# for ant in range(len(antenna)):
#     for num_tr in range(len(index_train)):
#         for num_te in range(len(number_test)):
#             sum_temp_dis=0
#             for j in range(len(CSI_train[num_tr][ant])):
#                 temp_dis,_ = fastdtw(CSI_test[ant][num_te],CSI_train[num_tr][ant][j])
#                 sum_temp_dis+=temp_dis
#             value = sum_temp_dis/len(CSI_train[num_tr][ant])
#             dis_mat[num_te][num_tr][ant] = value
#             print(num_te,num_tr,ant,'value:',value)
# print(dis_mat)
# 现在采集的每次都是1，2，···，9,0的逻辑 平均dtw
# for ant in range(len(antenna)):
#     for ind_te in range(len(number_test)):
#         for j in range(10):
#             sum_temp_dis=0
#             for ind_tr in range(len(index_train)):
#                 pure_test = get_pure_wave(CSI_test[ant][ind_te])
#                 pure_train = get_pure_wave(CSI_train[ind_tr][ant][j])
#                 temp_dis,_ = fastdtw(pure_test,pure_train)
#                 sum_temp_dis+=temp_dis
#             value = sum_temp_dis/len(index_train)
#             dis_mat[ind_te][j][ant] = value
#             print(ind_te,j,ant,'value:',value)
# print(dis_mat)

# knn dtw(k=1)
# plt.figure()
# plt.plot(CSI_train[8][0][1])
# plt.figure()
# plt.plot(get_pure_wave(CSI_train[8][0][1]))
# plt.show()
dis_knn_mat = np.zeros((len(number_test),len(antenna)))
source_mat = np.zeros(( len(number_test),len(antenna)))
dis_value_mat = np.zeros(( len(number_test),len(antenna)))
for ant in range(len(antenna)):
    for ind_te in range(len(number_test)):
        min = sys.maxsize
        min_index = -1
        min_number = -1
        for j in range(10):
            for ind_tr in range(len(index_train)):
                # print(j,ind_tr,np.size(CSI_train[ind_tr][ant][j]))
                pure_test = get_pure_wave(CSI_test[ant][ind_te])
                pure_train = get_pure_wave(CSI_train[ind_tr][ant][j])
                # if len(pure_train) < 700:
                #     print(ind_tr,ant,j )
                #     plt.figure()
                #     plt.plot(CSI_train[ind_tr][ant][j])
                #     plt.figure()
                #     plt.plot(pure_train)
                #     plt.show()
                temp_dis,_ = fastdtw(pure_test,pure_train)
                if temp_dis < min:
                    min = temp_dis
                    min_number = j#(j+1)%10
                    min_index = ind_tr
        dis_knn_mat[ind_te][ant] = min_number
        source_mat[ind_te][ant] = min_index
        dis_value_mat[ind_te][ant] = min
print(dis_knn_mat)
print(source_mat)
print(dis_value_mat)