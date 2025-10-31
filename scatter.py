import matplotlib.pyplot as plt
x=range(1,1001)
y=[i**2 for i in x]
plt.style.use('seaborn-v0_8-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x, y, c=y, cmap=plt.cm.Greens, s=10)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')
# Set size of tick labels.
ax.tick_params(labelsize=14)
plt.show()

