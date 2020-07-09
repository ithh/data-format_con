import os
import json
import scipy.io as spio
import pandas as pd


def loadmat(filename):
    data = spio.loadmat(filename, struct_as_record=False, squeeze_me=True)
    return _check_keys(data)


def _check_keys(dict):
    '''
    检查字典中的条目是否是关联对象。如果是调用todict将其更改为嵌套字典
    '''
    for key in dict:
        if isinstance(dict[key], spio.matlab.mio5_params.mat_struct):
            dict[key] = _todict(dict[key])
    return dict


def _todict(matobj):
    '''
    一个由matobjects嵌套字典构造的递归函数
    '''
    dict = {}
    for strg in matobj._fieldnames:
        elem = matobj.__dict__[strg]
        if isinstance(elem, spio.matlab.mio5_params.mat_struct):
            dict[strg] = _todict(elem)
        else:
            dict[strg] = elem
    return dict


def mat2json(mat_path=None, filepath=None):
    """
    mat_path: Str
        path/filename .mat存放路径
    filepath: Str
        如果需要保存成json, 添加这一路径. 否则不保存
    Returns
        返回转化的字典
    """

    matlabFile = loadmat(mat_path)

    # print(type(matlabFile))
    # print(matlabFile)
    # 弹出所有不允许jsonize文件的哑字段
    matlabFile.pop('__header__')
    matlabFile.pop('__version__')
    matlabFile.pop('__globals__')
    # jsonize文件定向为“索引”
    matlabFile = pd.Series(matlabFile).to_json()

    # print(matlabFile)
    # pandas 会对数据中的'/'做转义处理，为保证格式，做字符串转换
    matlabFile = matlabFile.replace(r'\/', r'/')
    if filepath:
        json_path = os.path.splitext(os.path.split(mat_path)[1])[0] + '.json'
        json_path = filepath + json_path
        with open(json_path, 'w') as f:
            f.write(matlabFile)
    return matlabFile

matfile = 'a.mat'
jsonfile = r"C:\Users\Admin\Desktop\ "
mat2json(matfile, jsonfile)

