import plotly.express as px
import matplotlib.pyplot as plt

from die import Die

# Create a D6 and a D10.
die_1 = Die()
die_2 = Die(10)


# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for _ in range(50_000)]
print(results)


# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

frequencies = [results.count(_) for _ in poss_results]
print(frequencies)


# Visualize the results through plotly.
title = "Results of Rolling a D6 and a D10 Dice 50,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# fig.show()
fig.write_html("dice_visual_d6d10_15_08.html")


# Visualize the results through matplotlib.
plt.style.use("seaborn")

fig, ax = plt.subplots()
ax.plot(poss_results, frequencies, linewidth=4)
ax.set_title("15-10", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

ax.tick_params(labelsize=14)
plt.show()
plt.savefig("15_10.png", bbox_inches="tight")
