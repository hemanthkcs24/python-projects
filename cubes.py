import matplotlib.pyplot as plt
x=range(-5000,5000)
y=[i**3 for i in x]
ax=plt.subplot()
ax.scatter(x,y,c=y,cmap=plt.cm.Blues,s=10)
ax.set_title('cubes',fontsize=24)
ax.set_xlabel('numbers',fontsize=20)
ax.set_ylabel('values',fontsize=20)
plt.show()