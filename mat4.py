from matplotlib import pyplot as plt
from matplotlib import style
#histogram graph
population=[10,11,22,33,44,55,66,77,88,99,21,66,33,88,56,89,53,96,23,99,11,33,66,44,77,77,77,23,67]
bin=[10,20,30,40,50,60,70,80,90,100,110]
plt.hist(population,bin,histtype='bar',rwidth=0.8)
plt.legend()
plt.title('histogram graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()

