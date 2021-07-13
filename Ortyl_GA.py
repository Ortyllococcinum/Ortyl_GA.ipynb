#!/usr/bin/env python
# coding: utf-8

# # Dominik Ortyl 65797
# ## Assignment Genetic Algorithm

# In[19]:


import numpy as np
from numpy import random
from numpy.random import randint, rand

grades_v =   {0:1.5,
            1:0.5,
            2:0.5,
            3:1.5,
            4:1.5,
            5:0.5,
            6:0.5,
            7:1.5,
            8:1.5,
            9:0.5,
            10:0.5,
            11:1.5,
            12:1.5,
            13:0.5,
            14:0.5,
            15:1.5}


def selection(pop, scores, k=3):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
                # check if better (e.g. perform a tournament)
                if scores[ix] < scores[selection_ix]:
                        selection_ix = ix
                        return pop[selection_ix]
    

# crossover two parents to create two children
def crossover(p1, p2, r_cross):
    #children are copies of parents by default
    c1, c2 = np.copy(p1), np.copy(p2)
    c1 = c1.tolist()
    c2 = c2.tolist()
    #check for recombination
    if rand() < r_cross:
        #select crossover point that is not on the end of the string
        pt = randint(1, np.shape(p1)[0])
        #perform crossover
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
        return [c1, c2]
    else:
        return []

def mutation(bitstring, r_mut):
        for i in range(len(bitstring)):
                # check for a mutation
                if rand() < r_mut:
                        # flip the bit
                        bitstring[i] = 1 - bitstring[i]
                        
                        
                        
def objective(pop_i):
    grades = [grades_v[pop_i[0]],
              grades_v[pop_i[1]],
              grades_v[pop_i[2]],
              grades_v[pop_i[3]],
              grades_v[pop_i[4]],
              grades_v[pop_i[5]],
              grades_v[pop_i[6]],
              grades_v[pop_i[7]],
              grades_v[pop_i[8]],
              grades_v[pop_i[9]],
              grades_v[pop_i[10]],
              grades_v[pop_i[11]],
              grades_v[pop_i[12]],
              grades_v[pop_i[13]],
              grades_v[pop_i[14]],
              grades_v[pop_i[15]]]
    grade_period1=(grades_v[pop_i.index(0)]+grades_v[pop_i.index(1)]+grades_v[pop_i.index(2)]+grades_v[pop_i.index(3)])
    grade_period2=(grades_v[pop_i.index(4)]+grades_v[pop_i.index(5)]+grades_v[pop_i.index(6)]+grades_v[pop_i.index(7)])
    grade_period3=(grades_v[pop_i.index(8)]+grades_v[pop_i.index(9)]+grades_v[pop_i.index(10)]+grades_v[pop_i.index(11)])
    grade_period4=(grades_v[pop_i.index(12)]+grades_v[pop_i.index(13)]+grades_v[pop_i.index(14)]+grades_v[pop_i.index(15)])
        
    penalty=(grade_period1-1.0)*(grade_period1-1.0)*10+(grade_period2-1.0)*(grade_period2-1.0)*10+(grade_period3-1.0)*(grade_period3-1.0)*10+(grade_period4-1.0)*(grade_period4-1.0)*10
        
    for block in range(4,15):
        if pop_i.index(block) < pop_i.index(block-4):
            penalty = penalty+1700
            
    print(penalty)
    return penalty


# In[ ]:





# In[20]:



# genetic algorithm
def genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut):
        # initial population of random bitstring
        pop = [np.random.permutation(n_bits).tolist() for _ in range(n_pop)]
        # keep track of best solution
        best = 0
        best_eval = objective(pop[0])
        # enumerate generations
        for gen in range(n_iter):
                # evaluate all candidates in the population
                scores = [objective(c) for c in pop]
                # check for new best solution
                for i in range(n_pop):
                        if scores[i] < best_eval:
                                best, best_eval = pop[i], scores[i]
                # select parents
                selected = [selection(pop, scores) for _ in range(n_pop)]
                # create the next generation
                children = list()
                for i in range(0, n_pop, 2):
                        # get selected parents in pairs
                        p1, p2 = selected[i], selected[i+1]
                        # crossover and mutation
                        for c in crossover(p1, p2, r_cross):
                            # mutation
                                mutation(c, r_mut)
                                # store for next generation
                                children.append(c)
                # replace population
                pop = children
        return [best, best_eval]


# In[21]:


n_bits = 16
n_pop = 10
n_iter = 15
r_cross= 0.5
r_mut= 1.0 / float(n_bits)

genetic_algorithm(objective, n_bits, n_iter, n_pop, r_cross, r_mut)


# In[ ]:





# In[ ]:




