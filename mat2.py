from matplotlib import pyplot as plt
from matplotlib import style
#line graph
style.use("ggplot")
x1=[5,8,9]
y1=[12,16,6]
x2=[6,9,11]
y2=[6,15,7]
plt.plot(x1,y1,'g',label='line one',linewidth=5)
plt.plot(x2,y2,'c',label='line two',linewidth=5)
plt.title('line graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
