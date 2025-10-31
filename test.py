import matplotlib.pyplot as plt
squares=[1,4,9,16,25]
inputvalues=[1,2,3,4,5]
plt.style.use('seaborn-v0_8-darkgrid')
fig,ax=plt.subplots()
ax.plot(inputvalues,squares, linewidth=3)
# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(labelsize=14)
plt.show()