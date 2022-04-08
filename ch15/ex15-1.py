from matplotlib import pyplot as plt


# Define the data
x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Create the plot
plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.scatter(x_values, cubes, edgecolor='none', s=40)

# Set chart name and axis name
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set label scale size
ax.tick_params(axis='both', labelsize=14)

# Display
plt.show()
