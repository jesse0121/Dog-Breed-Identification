import os
import shutil
import pandas as pd


train_path = 'D:\\Competition\\Dog-Breed-Identification\\Data\\train'
test_path = 'D:\\Competition\\Dog-Breed-Identification\\Data\\test'
sample_submission_path = 'D:\\Competition\\Dog-Breed-Identification\\Data\\sample_submission.csv'
label_path = 'D:\\Competition\\Dog-Breed-Identification\\Data\\labels.csv'


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
    if os.path.isfile(srcfile) is False:
        print("%s not exist" % srcfile)
    else:
        fpath, fname = os.path.split(srcfile)
        if os.path.exists(dst) is False:  # 判断dstpath是否为一个存在的路径或文件
            os.makedirs(dst)
        shutil.copy(srcfile, dst)  # 移动文件
        print("copy %s from %s -> %s" % (fname, fpath, dst))
    return None