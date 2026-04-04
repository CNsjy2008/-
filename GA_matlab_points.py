import matplotlib.pyplot as plt
import GA
import numpy as np

x = np.linspace(0, 50, 1000)
y = [GA.fitness([_,0]) for _ in x]

plt.plot(x, y, linewidth=1)
plt.title("目标函数曲线")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.savefig("函数曲线.png", dpi=300)
plt.show()
plt.plot(x, y)
plt.scatter(GA.best_ind[0], GA.best_score, color='red', facecolors='none', s=80, label='最优点')
plt.legend()
plt.title("最优解位置")
plt.savefig("最优解.png", dpi=300)
plt.show()