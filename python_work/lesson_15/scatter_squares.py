import matplotlib.pyplot as plt

x_values = []
y_values = []
for i in range(1, 5001):
    x_values.append(i)
    y_values.append(i**3)

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, s=10)

# Set chart title and label axes.
ax.set_title('Cube Numbers', fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0,5000,0,120_100_000_000])
ax.ticklabel_format(style='plain')

plt.show()