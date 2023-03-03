import matplotlib.pyplot as plt

from random_walk_refactored import RandomWalk

# Keep making new walks, as long as the program is active.

while True:
    # Make a random walk.
    rw = RandomWalk(5)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use("seaborn")
    # fig, ax = plt.subplots(figsize=(10, 9), dpi=128)
    fig, ax = plt.subplots()
    # point_numbers = range(rw.num_points)
    # ax.scatter(
    #     rw.x_values,
    #     rw.y_values,
    #     c=point_numbers,
    #     cmap=plt.cm.Blues,
    #     edgecolors="none",
    #     s=1,
    # )
    print(rw.x_values)
    print(rw.y_values)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    ax.set_title("15-05", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    # ax.set_aspect("equal")

    # Emphasize the first and last points.
    # ax.scatter(0, 0, c="green", edgecolors="none", s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Remove the axes.
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    # Set size of tick labels.
    ax.tick_params(labelsize=14)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
