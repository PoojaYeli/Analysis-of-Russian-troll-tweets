from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
fig = plt.figure()
ax = fig.add_subplot(111)
langs = ['#maga', '#local', '#tcot', '#news', '#sports', '#politics', '#topnews', '#world']
students = [15536, 26088, 15458, 131030, 48846, 39858, 15149, 27622]
ax.bar(langs,students)
ax.set_xlabel('Trending hashtags', fontsize=20, labelpad=15)
ax.set_ylabel('Number of hashtags', fontsize=20, labelpad=15)
plt.title('Trending hashtags', fontsize=20, y=1.08)
plt.show()