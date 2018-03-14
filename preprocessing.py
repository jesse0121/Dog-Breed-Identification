"""
对狗狗分类数据进行预处理
原始文件train中没有将图片数据按狗的品种来分别建文件夹分类，本文件将按狗的品种建立多个文件夹，分别存放该种类狗的图片
keras的ImageGenerator需要将不同种类的图片放在不同的文件夹中
Coder: Wang Xi
time: 2018.3.14
"""

import os
import shutil
import pandas as pd
from utils import *


def make_breed_file():
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


def move_train_data():
    """
    将训练集中的图片按其类别移动到相对应的文件夹，要求对应的文件夹存在
    :return: None
    """
    labels = pd.read_csv(label_path)
    labels = labels.set_index('id')
    label_dict = labels.to_dict('index')
    train_list = os.listdir(train_path + '\\train')
    for file in train_list:
        move_file(train_path + '\\train\\' + file,
                  train_path + '\\' + label_dict[file[:-4]]['breed'])
    print('Done')
    return None


def move_file(srcfile, dst):
    """

    :param srcfile: string 源文件路径
    :param dst: string 目标路径
    :return: None
    """
    if os.path.isfile(srcfile) is False:
        print("%s not exist" % srcfile)
    else:
        fpath, fname = os.path.split(srcfile)
        if os.path.exists(dst) is False:  # 判断dstpath是否为一个存在的路径或文件
            os.makedirs(dst)
        shutil.move(srcfile, dst)  # 移动文件
        print("move %s from %s -> %s" % (fname, fpath, dst))
    return None


def copy_file(srcfile, dst):
    """

    :param srcfile: string 源文件路径
    :param dst: string 目标路径
    :return: None
    """
    if os.path.isfile(srcfile) is False:
        print("%s not exist" % srcfile)
    else:
        fpath, fname = os.path.split(srcfile)
        if os.path.exists(dst) is False:  # 判断dstpath是否为一个存在的路径或文件
            os.makedirs(dst)
        shutil.copy(srcfile, dst)  # 移动文件
        print("copy %s from %s -> %s" % (fname, fpath, dst))
    return None


if __name__ == '__main__':
    pass
    # make_breed_file() # 在train中创建狗的不同品种文件夹
    # move_train_data() # 将原始数据的图片按照label.csv中的breed移动到不同的文件夹中
