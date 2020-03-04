import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from keras.preprocessing import sequence
#import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

from keras.optimizers import Adam
from keras.models import load_model
from keras.callbacks import ModelCheckpoint

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

train_ant_1_len= []
train_ant_2_len= []
train_ant_3_len= []
for i in range(len(CSI_train)):
    for j in range(len(CSI_train[i][0])):
        train_ant_1_len.append(len(CSI_train[i][0][k]))
        train_ant_2_len.append(len(CSI_train[i][1][k]))
        train_ant_3_len.append(len(CSI_train[i][2][k]))
print(pd.Series(train_ant_1_len).describe())
print(pd.Series(train_ant_2_len).describe())
print(pd.Series(train_ant_3_len).describe())