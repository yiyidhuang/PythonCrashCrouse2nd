from matplotlib import pyplot as plt

# Define data
x_values = list(range(5001))
cubes = [x**3 for x in x_values]

# Create plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, s=10)

# Set chart name and axis name
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set the size of the scale label and the value range of each coordinate axis
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])

# Display
plt.show()
