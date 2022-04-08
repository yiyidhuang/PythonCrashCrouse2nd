import csv
from datetime import datetime

import matplotlib.pyplot as plt

# filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # highs = []
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

    plt.style.use('seaborn')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    fig, ax = plt.subplots()
    # ax.plot(highs, c='red')
    ax.plot(dates, highs, c='red')

    # ax.set_title("2018年7月每日最高温度", fontsize=24)
    ax.set_title("2018年每日最高温度", fontsize=4)
    ax.set_xlabel('', fontsize=16)
    fig.autofmt_xdate()
    ax.set_ylabel("温度（F）", fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

print(highs)
