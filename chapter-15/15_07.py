import plotly.express as px

from die import Die

# Create Three D6 Dice
die_1 = Die()
die_2 = Die()
die_3 = Die()


# Make some rolls, and store results in a list.
results = []
for roll_num in range(100_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

print(results)


# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Visualize the results.
title = "Results of Rolling Three D6 Dice 100,000 Times"
labels = {"x": "Result", "y": "Frequency of Result"}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# fig.show()
fig.write_html("dice_visual_three_d6.html")
