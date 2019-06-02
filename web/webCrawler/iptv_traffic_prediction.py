import csv
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdates
from sklearn import linear_model
import numpy as np
from itertools import islice


"""
IPTV 分解点流量趋势及预测

读取历史数据
计算增长趋势
可视化展现

hints: 历史数据天数可以不连续
"""


filename = 'cdn_rate_zte.csv'
output = 'cdn_rate_zte_prediction.csv'
used_days = 28          # 用来计算的历史数据天数
prediction_days = 14    # 预测未来数据的天数
# 总容量：2265Gbps
nodes_bandwidth = {
    '区域中心1': 96,
    '区域中心2': 96,
    '节点1': 240,
    '节点2': 240,
    '节点3': 132,
    '节点4': 102,
    '节点5': 120,
    'cm': 60,
    'bs': 160,
    'jd': 210,
    'sj': 150,
    'fx': 120,
    'js': 99,
    'qz': 255,
    'qp': 105,
    'nh': 80
}   # 各个节点带宽
font = FontProperties(fname=r"../../src/simsun.ttc", size=10)   # 給Plt的图标里使用的中文字体


if __name__ == '__main__':
    # Input
    f = open(filename, 'r')
    reader = csv.reader(f)

    # Output 没用到，算法简单，低运算成本
    g = open(output, 'w')
    writer = csv.writer(g)

    # 画布准备
    plt.figure(figsize=(30, 20))    # 创建画布
    plt.suptitle('IPTV日峰值流量预测', fontproperties=font)
    plt.subplots_adjust(top=0.94, bottom=0.09, left=0.06, right=0.98, hspace=0.2, wspace=0.2)

    # 数据预处理
    raw_data = list()   # 从csv中提取数据。
    for item in islice(reader, 1, None):    # 从第二行开始读
        raw_data.append(item)
    earliest_recorded_day = datetime.datetime.strptime(raw_data[-used_days][0], '%Y-%m-%d')

    print('可用历史数据天数:', len(raw_data))
    print('使用数据天数:', used_days)
    print('预测天数:', prediction_days)
    print('当前节点数:', len(nodes_bandwidth.keys()))

    x_date = list()     # [0, 1, 2, ...] 供sklearn计算使用。实现非连续日期计算，便于剔除数据。
    x_show = list()     # x轴展示的日期，datetime格式
    for i in range(used_days, 0, -1):
        current_day = datetime.datetime.strptime(raw_data[-i][0], '%Y-%m-%d')
        delta = (current_day - earliest_recorded_day).days
        x_date.append([delta])
        x_show.append(current_day)

    x_predict = list()  # x轴展示的日期，预测时段
    now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    now = now - delta
    for i in range(prediction_days):
        x_predict.append(now)
        now = now + delta


    for n, node in enumerate(nodes_bandwidth.keys()):
        print()
        print(node, ':')
        tmp_data_rate = list()
        for i in range(used_days, 0, -1):
            tmp_data_rate.append([float(raw_data[-i][n+1])])
        # print('x_date:', x_date)
        # print('y_data:', tmp_data_rate)
        model = linear_model.LinearRegression()     # sklearn线性回归模型
        model.fit(x_date, tmp_data_rate)            # 计算
        print(model.coef_, model.intercept_)  # 线性模型的系数, 截距
        # print('损耗: ', model.residues_)  # 残差系数 方差和

        # x = np.linspace(0, used_days-1, used_days)
        x = np.array(x_date)    # 转换成ndarray类型
        plt.subplot(4, 4, n+1)  # 选定子视图
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%y.%m.%d'))   # 设置横坐标格式
        # plt.gca().xaxis.set_major_locator(mdates.DayLocator())

        plt.plot(x_show, (x * float(model.coef_)) + float(model.intercept_), 'b-', label=node)  # 预测直线（历史部分）
        plt.plot(x_predict, (np.array([i for i in range(used_days, used_days + prediction_days)]) * float(model.coef_))
                 + float(model.intercept_), 'g-')  # 预测直线（未来部分）
        plt.plot(x_show + x_predict, ([nodes_bandwidth[node]] * (used_days+prediction_days)), 'r-')         # 节点100%带宽预警
        plt.plot(x_show + x_predict, ([nodes_bandwidth[node] * 0.8] * (used_days+prediction_days)), 'c-')   # 节点80%带宽预警
        plt.plot(x_show, tmp_data_rate, 'k.')       # 历史数据打点
        plt.gcf().autofmt_xdate()                   # 自动调整横坐标显示格式
        plt.legend(prop=font)                       # 添加图例

    plt.show()







