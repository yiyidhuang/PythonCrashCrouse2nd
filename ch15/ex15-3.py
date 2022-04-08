import matplotlib.pyplot as plt


from random_walk import RandomWalk

# As long as the program is active, it constantly simulates random walking
while True:
    # Create a instance for RandomWalk
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Draw all the points contained in the instance
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # Highlight the start point and the end point
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Hide axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
