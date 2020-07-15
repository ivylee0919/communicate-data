import pandas as pd
import os
import requests
import zipfile
import io


def unzip_csv(urls):
    '''
    将 urls 中的 zip 数据下载并解压到 data 文件夹中
    返回解压后的 csv 文件名列表
    '''
    if not os.path.exists('data'):
        os.makedirs('data')

    data_list = os.listdir('data/')
    csv_list = []

    for url in urls:
        r = requests.get(url)
        file_name = url.split('/')[-1][:-4]
        csv_list.append(file_name)
        if file_name not in data_list:
            z = zipfile.ZipFile(io.BytesIO(r.content))
            z.extractall('data')
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
        csv_path = 'data/' + c
        df_month = pd.read_csv(csv_path)
        df_shape += df_month.shape[0]
        df = df.append(df_month)
    return df
