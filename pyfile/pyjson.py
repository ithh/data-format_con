import json
import xlrd
import time

def read_json(name):
    data = xlrd.open_workbook(name, 'rd')
    l={}
    for i in data.sheet_names():
        table = data.sheet_by_name(f'{i}')
        table_ncols = table.ncols  # 工作表的列数
        table_nrows = table.nrows  # 工作表的行数
        if i == 'ERR':  # 针对文件最后一个文档
            pass
        else:
            if table_ncols == 1:  # 针对文件第一个文档
                t = table.col_values(0)
                m={}
                for k in t:
                    h = k.split(':', 1)
                    m.setdefault(f'{h[0]}', f'{h[1].lstrip()}')
                # l.append(m)
                l.setdefault(f'{i}',m)
            elif table_ncols == 0:  # 针对空文档
                pass
            else:
                for j in range(table_ncols):
                    o = {}
                    if j == table_ncols - 1:
                        t = table.col_values(j)
                        for k in t[:12]:
                            h = k.split(':', 1)
                            o.setdefault(f'{h[0]}', f'{h[1].lstrip()}')
                        l.setdefault(f'{i}', o)
                    else:
                        pass
    return l
