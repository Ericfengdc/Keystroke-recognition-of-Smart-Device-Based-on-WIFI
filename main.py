import functions
import scipy.io as scio
import time
from fastdtw import fastdtw
import numpy as np
import matplotlib.pyplot as plt
import tsfresh

CSI_ALL = []                                              #保存所有的模板库
CSI_inner_under150 = []
###所有字母数据###
#目前只有9个
# word = ['A','B','C','D','E','F','G','H','I']
#
# for i in range(len(word)):
#     CSI = scio.loadmat('I:/1220/CSI_word/word_' + word[i] + '0.mat')
#     CSI = CSI['action']
#     CSI_temp = []
#     for j in range(len(CSI)):
#         CSI_temp.append(CSI[j][0][0]- np.mean(CSI[j][0][0]))
#     CSI_ALL.append(CSI_temp)
###句子数据###
sentence_raw = scio.loadmat('I:/1220/CSI_word/word_all90.mat')
sentence_raw = sentence_raw['action']
CSI_ALL = np.load('CSI_inner_under150.npy')
# plt.plot(functions.get_pure_wave(CSI_ALL[0][0]))
# plt.show()

###对sentence和word的数据进行处理，只保留中间的部分###
sentence = []
for i in range(len(sentence_raw)):
    temp = functions.get_pure_wave(sentence_raw[i][0][0])
    sentence.append(temp - np.mean(temp))
for i in range(len(CSI_ALL)):
    for j in range(len(CSI_ALL[i])):
        temp = functions.get_pure_wave(CSI_ALL[i][j])
        CSI_ALL[i][j] = temp - np.mean(temp)

###显示提取后的sentence的CSI和提取前CSI区别###
for i in range(len(sentence)):
    plt.figure()
    plt.plot(sentence_raw[i][0][0])
    # plt.plot(sentence[i])
    plt.show()

###显示提取后的word的CSI和提取前CSI区别###
# for i in range(len(CSI_ALL[1])):
#     plt.figure()
#     plt.plot(functions.get_pure_wave(CSI_ALL[1][i]))
#     plt.plot(CSI_ALL[1][i])
#     plt.show()

###比较句子中每个字母和26个字母的比较结果
# time_start = time.time()
# dis = 0
# for i in range(len(sentence)):                                          #整个句子
#     for j in range(len(CSI_ALL)):
#         dis = 0                                                          #整个字母集
#         for k in range(len(CSI_ALL[j])):                                #其中一个字母集
#             temp_dis,n = fastdtw(sentence[i],CSI_ALL[j][k])
#             dis += temp_dis
#         print('句子中第',i + 1,'个词与字母',chr(65+j),'的平均DTW距离为',dis/len(CSI_ALL[j]))
#     print('\n\n')
# time_end = time.time()
# print('fastDTW时间为',time_end - time_start)

###比较每个模板库中序列与其他序列的DTW距离###
# for k in range(len(CSI_ALL)):
#     CSI_temp = []
#     for i in range(len(CSI_ALL[k])):
#         dis = 0
#         for j in range(len(CSI_ALL[k])):
#             temp_dis,a = fastdtw(CSI_ALL[k][i],CSI_ALL[k][j] )
#             dis += temp_dis
#         dis = dis/len(CSI_ALL[0])
#         print('第',i+1,'个',chr(65+k),'与其余的平均DTW距离为',dis)
#         if dis < 150:
#             CSI_temp.append(CSI_ALL[k][i])
#     CSI_inner_under150.append(CSI_temp)
# #保存获得的内部DTW小于150的字母CSI序列。
# CSI_inner_under150 = np.array(CSI_inner_under150)
# np.save('CSI_inner_under150.npy',CSI_inner_under150)

