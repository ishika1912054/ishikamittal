from matplotlib import pyplot as plt
from matplotlib import style
# scatter plot
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]
plt.scatter(x, y, label='scatplot', color='k', s=25, marker='o')
plt.legend()
plt.title('scatter plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

