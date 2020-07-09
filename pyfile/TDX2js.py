from pandas import DataFrame, concat, ExcelWriter, merge
from numpy import mean, max, array, unique, float, rint
import scipy.io as sio
import json
import os
import time

'''
Ifo是dataframe结构使用了values，to_dict(orient="list"),以保存数据类型
'''


'''
# 转存mat的字典结构
FKA = {
         'Ifo': Ifo.values,
         'QuasiSteady':
                {'PureSideSlip':
                    {'Data': SRData.values,'TestInfo': Test_Ifo_SR.values},
                 'PureLongSlip':
                    {'Data': SAData.values,'TestInfo': Test_Ifo_SA.values},
                 'CombinedSlip':
                    {'Data': XYData.values,'TestInfo': Test_Ifo_XY.values}
                 },
         'Steady':
             {
                 'PureSideSlip': {
                    'Data': W_SR.values,'TestInfo': W_SRInfo.values
                 },
                 'PureLongSlip': {
                     'Data': W_SA.values,'TestInfo': W_SAInfo.values
                 },
                 'CombinedSlip': {
                     'Data': W_XY.values,'TestInfo': W_XYInfo.values
                 },
                 'EffeR':ERR.values
            },
         'Static':
            {'VerStiff':
                 {'Data': VerData.values,'TestInfo': Test_Ifo_Ver.values},
             'LongStiff':
                 {'Data': LongData.values,'TestInfo': Test_Ifo_Lon.values},
             'LatStiff':
                 {'Data': LatData.values,'TestInfo': Test_Ifo_Lat.values}
            },
         'Transient':
             {'StepSlip':
                    {'Data': TSData.values,'TestInfo': Test_Ifo_TS.values}
              },
         'Dynamic': Dynamic.values,
         'Design': Design.values
    }
'''

# 转存json的字典结构
FKA = {
         'Ifo': Ifo.to_dict(orient="list"),
         'QuasiSteady':
                {'PureSideSlip':
                    {
                        'Data': SRData.to_dict(orient="list"),
                        'TestInfo': Test_Ifo_SR.to_dict(orient="list")
                    },
                 'PureLongSlip':
                    {
                        'Data': SAData.to_dict(orient="list"),
                        'TestInfo': Test_Ifo_SA.to_dict(orient="list")
                    },
                 'CombinedSlip':
                    {
                        'Data': XYData.to_dict(orient="list"),
                        'TestInfo': Test_Ifo_XY.to_dict(orient="list")
                    }
                 },
         'Steady':
             {
                 'PureSideSlip': {
                     'Data': W_SR.to_dict(orient="list"), 'TestInfo': W_SRInfo.to_dict(orient="list")
                 },
                 'PureLongSlip': {
                     'Data': W_SA.to_dict(orient="list"), 'TestInfo': W_SAInfo.to_dict(orient="list")
                 },
                 'CombinedSlip': {
                     'Data': W_XY.to_dict(orient="list"), 'TestInfo': W_XYInfo.to_dict(orient="list")
                 },
                 'EffeR': ERR.to_dict(orient="list")
         },
         'Static':
            {'VerStiff':
                 {'Data': VerData.to_dict(orient="list"),'TestInfo': Test_Ifo_Ver.to_dict(orient="list")},
             'LongStiff':
                 {'Data': LongData.to_dict(orient="list"),'TestInfo': Test_Ifo_Lon.to_dict(orient="list")},
             'LatStiff':
                 {'Data': LatData.to_dict(orient="list"),'TestInfo': Test_Ifo_Lat.to_dict(orient="list")}
            },
         'Transient':
             {'StepSlip':
                    {'Data': TSData.to_dict(orient="list"),'TestInfo': Test_Ifo_TS.to_dict(orient="list")}
              },
         'Dynamic': Dynamic.to_dict(orient="list") ,
         'Design': Design.to_dict(orient="list")
    }


# sio.savemat('FKA.mat', FKA)

js = json.dumps(FKA, sort_keys=True, separators=(',', ':'))
with open('FKA.json', 'w', encoding='utf-8') as f:
    f.write(js)



# dic = {'a': 1, 'b': 2, 'c': 3}