import numpy as np
import matplotlib.pyplot as plt
map_size = 10
goal_num = 10
goals_x = []
goals_y = []
goals_x_p = []
goals_y_p = []

goals_x.append(0)
goals_y.append(0)
goals_x.append(0.6)
goals_y.append(0)

for i in range(goal_num-2):
    goals_x.append((np.random.rand(1)[0]*(map_size-0.5))-((map_size+1)/2))
    goals_y.append((np.random.rand(1)[0]*(map_size-0.5))-((map_size+1)/2))

print(goals_x)
print(goals_y)
np.savetxt('goals.txt', np.array([goals_x, goals_y]).T, fmt="%.2f")
plt.xlim((-(map_size/2),map_size/2))
plt.ylim((-(map_size/2),map_size/2))
plt.plot(goals_x,goals_y,'r*',[0],[0],'b^')
plt.grid(True)
plt.show()