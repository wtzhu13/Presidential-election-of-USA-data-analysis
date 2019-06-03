# _*_ coding:UTF-8 _*_
# path:/home/tarena/桌面/study_file/...

"""
作者：朱文涛
邮箱：wtzhu_13@163.com

时间：2019/05
描述：
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


def judge_num(month_data):
    """
        去掉数据中不能转化成整数的数，不能转换
        的统一记为0
    :param month_data:需要判断的数据
    :return:
    """
    try:
        return float(month_data)
    except:
        return 0


def get_sum(list_per_month_data):
    """
        对同一个月分的数据进行求和
        先将数组转化为列表，然后逐项
        进行float转化
    :param list_per_month_data:同一个月份的数据
    :return:
    """
    data_filter = [judge_num(i) for i in list_per_month_data.tolist()]
    return sum(data_filter)


def data_conformity(poll):
    """
        对相同月份的数据进行整理
    :param poll:待整理的数据
    :return:整理好，按月份排列的数据列表
    """
    ordinate = []
    for month in list_months:
        array_per_month_data = poll[array_month == month]
        per_month_total_data = get_sum(array_per_month_data)
        ordinate.append(per_month_total_data)
    return ordinate


def plot_data(list_clinton, list_trump):
    """
        利用好plot绘制图像
    :param list_clinton:克林顿的数据
    :param list_trump:特朗普的数据
    :return:
    """
    plt.plot(list_months, list_clinton, "r", list_months, list_trump, "g")
    plt.xlabel("date of month")
    plt.ylabel("data")


def bar_data(list_clinton, list_trump):
    """
        绘制条形图
    :param list_clinton:
    :param list_trump:
    :return:
    """
    x = list(range(len(list_months)))
    plt.bar(x=x, height=list_clinton, width=0.2, color="r", label="clinton")
    plt.bar(x=[i+0.2 for i in x], height=list_trump, width=0.2, color="g", label="trump")
    plt.xticks([index + 0.1 for index in x], list_months)
    plt.ylim(0, 170000)   # y轴取值范围
    plt.ylabel("data")     # 定义纵轴名
    plt.xlabel("time")     # 定义横轴名
    plt.legend()           # 设置题注


filename = "presidential_polls.csv"
# 读取表头，并删除换行符
with open(filename, "r") as f:
    str_col_name = f.readline()[:-1]
list_col_name = str_col_name.split(",")

# 需要用到的列的索引
list_use_name = ["enddate", "rawpoll_clinton", "rawpoll_trump",
                 "adjpoll_clinton", "adjpoll_trump"]
# 提取用到列的索引
list_use_name_index = [list_col_name.index(name) for name in list_use_name]

# 从表格中读取所需列的数据
data = np.loadtxt(filename, dtype=str, skiprows=1,
                  delimiter=",", usecols=list_use_name_index)
# 将日期单独列出来进行处理
list_enddate = data[:, 0].tolist()
# 将日期字符串转化为日期格式
list_datetime_enddate = [datetime.strptime(time, "%m/%d/%Y") for time in list_enddate]

# 整合月份，将一个月的数据整合到一齐
list_all_month = ["%d/%02d" % (datet.year, datet.month) for datet in list_datetime_enddate]
array_month = np.array(list_all_month)
list_months = np.unique(array_month).tolist()

# 获取克林顿的原始数据
array_rawpoll_clinton = data[:, 1]
# 获取克林顿的处理后的数据
array_adjpoll_clinton = data[:, 3]

# 获取特朗普的原始数据
array_rawpoll_trump = data[:, 2]
# 获取特朗普的处理后的数据
array_adjpoll_trump = data[:, 4]


# 整合后克林顿的数据
list_integration_clinton = data_conformity(array_rawpoll_clinton)
list_adjintegration_clinton = data_conformity(array_adjpoll_clinton)

# 整合后特朗普的数据
list_integration_trump = data_conformity(array_rawpoll_trump)
list_adjintegration_trump = data_conformity(array_adjpoll_trump)

# 使用连线图绘制图形
plt.figure(1)
plt.subplot(2, 1, 1)
plot_data(list_integration_clinton, list_integration_trump)
plt.subplot(2, 1, 2)
plot_data(list_adjintegration_clinton, list_adjintegration_trump)
plt.show()

# 使用条形图绘制数据
plt.figure(2)
plt.subplot(2, 1, 1)
bar_data(list_integration_clinton, list_integration_trump)
plt.subplot(2, 1, 2)
bar_data(list_adjintegration_clinton, list_adjintegration_trump)
plt.show()
