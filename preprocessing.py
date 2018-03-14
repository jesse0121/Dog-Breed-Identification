'''
对狗狗分类数据进行预处理
原始文件train中没有将图片数据按狗的品种来分别建文件夹分类，本文件将按狗的品种建立多个文件夹，分别存放该种类狗的图片
keras的ImageGenerator需要将不同种类的图片放在不同的文件夹中
Coder: Wang Xi
time: 2018.3.14
'''

import os
import shutil
import pandas as pd
import numpy as np

from utils import train_path, test_path, label_path, sample_submission_path

def mk_breed_file():
    """
    在Data子目录下创建与类别相同的文件夹，以供后续ImageGenerator使用
    :return: None
    """
    label = pd.read_csv(label_path)
    category = label['breed'].unique()
    for file in category:
        os.makedirs(train_path + '\\' + file)
    print("Done")
    return None

