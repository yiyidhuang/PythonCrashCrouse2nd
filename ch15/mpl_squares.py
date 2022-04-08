import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(squares, linewidth=3)
ax.plot(input_values, squares, linewidth=3)

# Set the chart title and label the axis
ax.set_title("Square", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of label", fontsize=14)

# Sets the size of the tick mark
ax.tick_params(axis='both', labelsize=14)
# ax.plot(squares)

plt.show()
