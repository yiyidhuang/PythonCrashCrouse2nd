import matplotlib.pyplot as plt

from random_walk import RandomWalk


# As long as the program is active, it constantly simulates random walking
while True:
    # Create a RandomWalk instance
    # rw = RandomWalk()
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Draw all points
    plt.style.use('classic')
    # fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    # ax.scatter(rw.x_values, rw.y_values, s=15)
    # ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # Highlight the start point and the end point
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    plt.show()

    # Hide axes
    ax.get_yaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
