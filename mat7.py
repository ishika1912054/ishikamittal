from matplotlib import pyplot as plt
from matplotlib import style
# pie plot
slices=[7,2,2,13]
activities=['sleeping','eating','working','playing']
cols=['m','c','r','b']
plt.pie(slices,labels=activities,
        colors=cols,
        shadow=True,
        startangle=90,
        explode=(0,0.1,0,0),
        autopct='%1.1f%%')
plt.title('pie plot')
plt.show()
