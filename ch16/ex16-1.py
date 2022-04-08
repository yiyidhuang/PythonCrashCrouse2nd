import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, precips = [], []
    for row in reader:
        curren_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(curren_date)
        precip = float(row[3])
        precips.append(precip)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue')

plt.title("Daily Rainfall Amounts - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Rainfall (in)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
