import pandas as pd
import os
import zipfile

def unzip_csv():
    '''
    将 zip 文件夹中的所有 zip 文件都解压到当前目录下
    并返回解压后的 csv 文件名列表
    '''
    zip_list = os.listdir('zip/')
    # 解压所有压缩包
    csv_list = []
    for file in zip_list:
        if file[-4:] == '.zip':
            with zipfile.ZipFile('zip/'+file, 'r') as myzip:
                csv_file = myzip.namelist()[0]
                csv_list.append(csv_file)
                myzip.extract(csv_file)
    return csv_list

def append_csv(csv_list):
    '''
    读取 csv_list 中的每一个 csv 文件，将所有的数据集追加到一起
    返回最终的 df
    '''
    # 将数据集合并到一起
    df = pd.DataFrame()
    df_shape = 0
    for c in csv_list:
        df_month = pd.read_csv(c)
        df_shape += df_month.shape[0]
        df = df.append(df_month)
    return df