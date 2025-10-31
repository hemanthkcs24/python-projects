import matplotlib.pyplot as plt
from RandomWalk import randoom_walk 
rw=randoom_walk(50000)
rw.fill_walk()
fig,ax=plt.subplots(figsize=(10, 6), dpi=128)
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Greens,edgecolors='none', s=10)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
plt.show()