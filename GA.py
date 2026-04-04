import numpy as np
from GAModdleFunction import *

# 这里必须改成 ind，然后取 ind[0] 才是真正的 x
def fitness(ind):
    x = ind[0]
    res = abs(x * np.sin(x) * np.cos(2 * x) - 2 * x * np.sin(3 * x) + 3 * x * np.cos(4 * x))
    return res

best_ind, best_score = genetic_algorithm(
    fitness_func=fitness,
    pop_size=50,
    gene_num=1,
    gene_min=0,
    gene_max=50,
    generations=1000,
    cross_rate=0.8,
    mut_rate=0.15
)

print("最优解 x =", best_ind[0])
print("最优适应度 =", best_score)


