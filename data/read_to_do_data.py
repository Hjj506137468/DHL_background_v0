import xlrd
import json
from config import BASE_DIR


def handler_excel(filename=BASE_DIR + "./data/background_to_do_data.xls"):  # 文件夹位置
    # 打开文件
    workbook = xlrd.open_workbook(filename)
    """打开文件"""
    sheet1 = workbook.sheet_names()[0]
    """获取sheet1"""
    table = workbook.sheet_by_name(sheet1)
    """通过sheet1获取表格"""

    nrows = table.nrows
    """表格中的行"""
    data_list = list()  # 空列表
    data_list1 = list()  # 空列表1
    data_list2 = list()  # 空列表2
    for i in range(1, nrows):  # 从第1行到第n行循环
        # print(table.row_values(i))#获取table中每行所有值
        # print(table.row_values(i)[2])#获取table中每行 中 特定列的值
        n = json.loads(table.row_values(i)[2])  # 将字符串转化成json（列表）
        data_list.append(n)
        """n 追加到列表里面"""
        # print(list(n))
        # print(data_list)
        for e in data_list:  # 循环这个列表获得username，password、expect....
            data_list1 = list()  # 空列表1
            # print(e['username'])
            # print(e['password'])
            # print((e['code']))
            # print((e['expect']))
            data_list1.append(e['username'])
            data_list1.append(e['password'])
            data_list1.append(e['expect'])
            # print(data_list1)
        data_list2.append(data_list1)
    print(data_list2)
    return data_list2


if __name__ == '__main__':
    handler_excel()
