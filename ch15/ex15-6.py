from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D8
die_1 = Die(num_sides=8)
die_2 = Die(num_sides=8)

# Roll the dice multiple times and store the results in list
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analysis results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D8 dice 1,000,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')
