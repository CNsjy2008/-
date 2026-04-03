import random

"""
=========================================================================================
通用遗传算法核心库
功能：用于求解连续函数的最大值优化问题
特点：
    1. 不绑定任何题目，可直接套用任意适应度函数
    2. 实数编码（浮点数基因），适合绝大多数数值优化场景
    3. 包含：初始化、选择、交叉、变异、进化完整流程
    
使用方法：
    # 运行遗传算法
best_ind, best_score = genetic_algorithm(
    fitness_func=my_fitness,
    pop_size=50,     # 种群大小
    gene_num=,      # 变量个数（x一个变量）
    gene_min=,    # 变量下限,即区间起始
    gene_max=,     # 变量上限，即区间终点
    generations=100, # 迭代次数
    cross_rate=0.8,  # 交叉率
    mut_rate=0.05    # 变异率，取0.01~0.2
)

print("最优解 x =", best_ind[0])
print("最优适应度 =", best_score)
=========================================================================================
"""
def fit(ind:list):
    """
    在这里编写适应函数
    :param ind: 输入的是一个indvisual个体，需要用x,y,z接受ind的各值
    :return: 函数表达式
    """
    pass



def initialize_population(pop_size, gene_num, gene_min, gene_max):
    """
    初始化种群
    :param pop_size: 种群大小（个体数量）
    :param gene_num: 每个个体的基因数量（变量个数）
    :param gene_min: 基因最小值
    :param gene_max: 基因最大值
    :return: 初始化完成的种群（二维列表：个体数 × 基因数）
    """
    pop = []
    # 循环创建指定数量的个体
    for _ in range(pop_size):
        # 每个个体由 gene_num 个 [gene_min, gene_max] 之间的随机浮点数组成
        individual = [random.uniform(gene_min, gene_max) for _ in range(gene_num)]
        pop.append(individual)
    return pop


def select(pop, fitness):
    """
    选择操作：轮盘赌选择法
    核心思想：适应度越高的个体，被选中的概率越大
    :param pop: 当前种群
    :param fitness: 种群中每个个体对应的适应度值
    :return: 选择后的新种群
    """
    new_pop = []
    total_fit = sum(fitness)  # 总适应度（用于计算选择概率）

    # 循环选择，保持种群大小不变
    for _ in range(len(pop)):
        r = random.uniform(0, total_fit)  # 生成随机指针
        current_sum = 0

        # 遍历个体，找到指针落在哪个个体区间
        for i in range(len(pop)):
            current_sum += fitness[i]
            if current_sum >= r:
                new_pop.append(pop[i].copy())  # 选中该个体
                break

    return new_pop


def crossover(p1, p2, cross_rate):
    """
    交叉操作：单点交叉
    作用：产生新个体，保留父代优良基因
    :param p1: 父代个体1
    :param p2: 父代个体2
    :param cross_rate: 交叉概率（一般0.6~0.9）
    :return: 交叉后的子代个体
    """
    # 按概率判断是否进行交叉
    if random.random() > cross_rate:
        return p1.copy()  # 不交叉，直接返回父代1副本

    # 随机选择交叉点（不首尾交叉，保证有效）
    cross_point = random.randint(1, len(p1) - 1)

    # 前半段来自p1，后半段来自p2
    child = p1[:cross_point] + p2[cross_point:]
    return child


def mutate(ind, mut_rate, gene_min, gene_max):
    """
    变异操作：随机重置基因值
    作用：保持种群多样性，避免早熟收敛
    :param ind: 待变异个体
    :param mut_rate: 变异概率（一般0.001~0.1）
    :param gene_min: 基因最小值
    :param gene_max: 基因最大值
    :return: 变异后的个体
    """
    # 遍历个体的每一个基因位
    for i in range(len(ind)):
        if random.random() < mut_rate:
            # 满足概率则随机重置为区间内新值
            ind[i] = random.uniform(gene_min, gene_max)
    return ind


def evolve(pop, fitness, cross_rate, mut_rate, gene_min, gene_max):
    """
    一代完整进化流程：选择 → 交叉 → 变异
    :return: 进化后的新一代种群
    """
    # 第一步：选择优秀个体
    pop = select(pop, fitness)
    new_pop = []

    # 两两配对进行交叉变异
    for i in range(0, len(pop), 2):
        parent1 = pop[i]
        parent2 = pop[i + 1] if i + 1 < len(pop) else parent1  # 防止越界

        # 交叉产生两个子代
        child1 = crossover(parent1, parent2, cross_rate)
        child2 = crossover(parent2, parent1, cross_rate)

        # 变异
        child1 = mutate(child1, mut_rate, gene_min, gene_max)
        child2 = mutate(child2, mut_rate, gene_min, gene_max)

        new_pop.append(child1)
        new_pop.append(child2)

    # 保持种群大小不变
    return new_pop[:len(pop)]


def genetic_algorithm(fitness_func, pop_size, gene_num, gene_min, gene_max, generations, cross_rate, mut_rate):
    """
    遗传算法主函数（总入口）
    :param fitness_func: 外部传入的适应度函数（必须自己定义）
    其余参数：种群大小、基因数、基因范围、迭代次数、交叉率、变异率
    :return: 最优个体 + 最优适应度
    """
    # 初始化种群
    pop = initialize_population(pop_size, gene_num, gene_min, gene_max)

    # 开始迭代进化
    for gen in range(generations):
        # 计算所有个体的适应度
        fitness = [fitness_func(ind) for ind in pop]
        # 进化一代
        pop = evolve(pop, fitness, cross_rate, mut_rate, gene_min, gene_max)

    # 找出最终最优个体
    final_fitness = [fitness_func(ind) for ind in pop]
    best_index = final_fitness.index(max(final_fitness))

    return pop[best_index], final_fitness[best_index]