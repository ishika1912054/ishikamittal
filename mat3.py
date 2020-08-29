from matplotlib import pyplot as plt
from matplotlib import style
#bar graph
plt.bar([1,3,5,7,9],[5,2,7,8,2],label='one')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='two')
plt.legend()
plt.title('bar graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()
