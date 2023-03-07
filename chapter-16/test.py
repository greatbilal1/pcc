import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4, 5, 5, 4, 3, 2, 11, 2, 3, 4, 5, 7])
ax.ticklabel_format(style="plain")
plt.show()
