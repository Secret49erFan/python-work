import plotly.express as px
import matplotlib.pyplot as plt

from die import Die

# Create a D6 and a D10.
die_a = Die()
die_b = Die()
# die_c = Die()

# Make some rolls, and store ruslts in a list.
num_of_rolls = 1_000_000

results_a = die_a.roll(num_of_rolls)
results_b = die_b.roll(num_of_rolls)
# results_c = die_c.roll(num_of_rolls)

die_sum = [results_a[i] + results_b[i] for i in range(num_of_rolls)]
# for roll_num in range(num_of_rolls):
#     die_sum.append(results_a[roll_num]+results_b[roll_num])

# Analyze the results.
max_result = die_a.sides + die_b.sides
frequencies = []
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = die_sum.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = 'Results of Rolling two D6 Dice 1,000,000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

# fig.show()

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(poss_results, frequencies)
ax.set_title('Results of Rolling two D6 Dice 1,000,000 Times', fontsize=24)
ax.set_xlabel('Results', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)
ax.set_xticks(list(poss_results))


plt.show()