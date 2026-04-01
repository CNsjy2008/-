import  numpy as np
import random

def fitness(x):
    res = abs(x * np.sin(x) * np.cos(2 * x) - 2 * x * np.sin(3 * x) + 3 * x * np.cos(4 * x))
    return res

def create_individual(a, b):
    return random.uniform(a, b)

def create_population(size, a, b):
    return [create_individual(a, b) for _ in range(size)]

def select(pop, fits):
    total = sum(fits)
    r = random.uniform(0, total)
    s = 0
    for i in range(len(pop)):
        s += fits[i]
        if s >= r:
            return pop[i]
    return pop[-1]

def crossover(p1, p2):
    return (p1 + p2) / 2

def mutate(x, a, b, rate):
    if random.random() < rate:
        return random.uniform(a, b)
    return x

def ga(pop_size, a, b, gen, mut_rate):
    pop = create_population(pop_size, a, b)
    for _ in range(gen):
        fits = [fitness(x) for x in pop]
        new_pop = []
        for _ in range(pop_size):
            p1 = select(pop, fits)
            p2 = select(pop, fits)
            child = crossover(p1, p2)
            child = mutate(child, a, b, mut_rate)
            new_pop.append(child)
        pop = new_pop
    fits = [fitness(x) for x in pop]
    best = pop[fits.index(max(fits))]
    return best, fitness(best)

best_x, best_f = ga(50, 0, 50, 1000, 0.2)
print(best_x, best_f)




