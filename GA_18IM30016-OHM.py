#!/usr/bin/env python
# coding: utf-8

# # Name: Priya Sinha
# # Roll No.: 18IM30016

# In[1]:


import numpy as np
import random
import math
N = 10 # Number of customer
population_size = 60 # Total chromosomes generated
D = 60  # financial institution’s deposit
k = 0.15  # required reserved ratio
insti_cost = 0.0025  # institutional cost
rD = 0.009  # weighted average of the deposit interest rates
L = [10,25,4,11,18,3,17,15,9,10]  # Loan size
rL = [0.021,0.022,0.021,0.027,0.025,0.026,0.023,0.021,0.028,0.022]  # Loan Interest rate       
loss = [0.0002,0.0058,0.0001,0.0003,0.0024,0.0002,0.0058,0.0002,0.001,0.001]  # Loss
loan_revenue = []  # for storing the value of loan revenue
loan_cost = []  # for storing the value for loans cost
total_transaction_cost = []  # for storing the value of total transcaction cost
cost_demand_deposit = []  # beta, cost of demand deposit
function = []  # Storing te value of objective function for every customer

for i in range(0, 10):
    a = rL[i]*L[i]-loss[i]
    loan_revenue.append(a)
    
    b = L[i]*insti_cost
    loan_cost.append(b)
    
    c = rL[i]*((1-k)*D - L[i])
    total_transaction_cost.append(c)
    
    d = rD*D
    cost_demand_deposit.append(d)
    
    function.append(a+c-d-loss[i])
    
function    


# In[2]:


# Generating initial solution
chromosomes =np.random.randint(2, size=(population_size,N))
chromo = chromosomes
chromosomes


# In[3]:


# calculating cummulative probability
cum_prob = [] # storing cummulative probability
fitness_val = []  # storing fitness value for every chromosomes
cum_fit = []  # storing cummulative fitness
A = []        # storing the objective function value for each customer
s = 0         # for getting the overall profit for chromosome
for i in range(0,population_size):
        for j in range(0,N):
            A.append(chromosomes[i][j]*function[j])
for i in range (0,population_size*N,N):
    for j in range(i,i+N):
        s = s + A[j]
    fitness_val.append(s)
    s = 0
for i in range(0,population_size):
    cum_fit.append(sum(fitness_val[0:i+1]))
for i in range(0,population_size):
    cum_prob.append(cum_fit[i]/cum_fit[population_size-1])
    
#cum_prob


# In[4]:


# roulette wheel selection
for i in range(0,population_size):
    r3 = random.random()
    #print(r3)
    for j in range(1,population_size):
        if (r3>=cum_prob[j-1]) & (r3<cum_prob[j]):
            chromosomes[i] = chromosomes[j]
    #print(chromosomes[i])
#chromosomes


# In[5]:


# sorting the chromosomes according to their fitness value
reproduction_ratio = round(0.194*population_size)
C = []  # storing idividual values
fit_val = []  # storing the fitness value for every chromosome
sum_ = 0
#appending the values for each customer
for i in range(0,population_size):
    for j in range(0,N):
        C.append(chromosomes[i][j]*function[j])
#finding the sum or fitness value
for i in range (0,population_size*N,N):
    for j in range(i,i+N):
        sum_ = sum_ + C[j]
    fit_val.append(sum_)
    sum_ = 0

for i in range(len(fit_val)):
    for j in range(0, len(fit_val)-i-1):
        if fit_val[j] > fit_val[j+1] :
            fit_val[j], fit_val[j+1] = fit_val[j+1], fit_val[j]
            temp = chromosomes[j]
            for k in range(len(chromosomes[j])):
                chromosomes[j][k], chromosomes[j+1][k] = chromosomes[j+1][k], chromosomes[j][k]
            
chromosomes


# In[6]:


# Crossover 
crossover_prob = 0.8
# we are using crossover on population_size - reproduction_ratio 
for i in range(0,population_size-reproduction_ratio,2):
    r4 = random.random()
    #print("r4",r4)
    if r4 <= crossover_prob:
        r1= random.randint(0,9) 
        #print("r1",r1)
        c1 = np.concatenate((chromosomes[i][0:r1],chromosomes[i+1][r1:]))
        c2 = np.concatenate((chromosomes[i+1][0:r1],chromosomes[i][r1:]))
    else:
        c1 = chromosomes[i]
        c2 = chromosomes[i+1]
    chromosomes[i] = c1
    chromosomes[i+1] = c2  
#chromosomes


# In[7]:


# mutation
mutation_prob = 0.006
for i in range(0,population_size-reproduction_ratio):
# we are using mutation on population_size - reproduction_ratio 
    for j in range(0,N):
        r5 = random.random()
        #print(r5)
        if r5<= mutation_prob:
            if chromosomes[i][j] == 1:
                chromosomes[i][j] = 0
            else:
                chromosomes[i][j] = 1
        else:
            chromosomes[i][j]=chromosomes[i][j]
    #print(chromosomes[i])
                


# In[8]:


#constraint
# Eliminating chromosomes which violates the constraint 

C = [] #for storing the loan size of individual gene
E = [] #for storing the fitness value for individual gene
loan_size = [] # for storing the loan size of chromosomes
fit = [] # for storing the fitness value for chromosomes
sum = 0
sum1 = 0
for i in range(0,population_size):
    for j in range(0,N):
        C.append(chromosomes[i][j]*L[j])
        E.append(chromosomes[i][j]*function[j])

for i in range (0,population_size*N,N):
    for j in range(i,i+N):
        sum = sum + C[j]
        sum1 = sum1 + E[j] 
    loan_size.append(sum)
    fit.append(sum1)
    sum = 0
    sum1 = 0
        
#loan_size    


# In[9]:


# As L<= (1-k)*D therefore, the value of (1-k)*D = 51

val = 51
for i in range(0,population_size):
    if loan_size[i] <= val:
        loan_size[i] = loan_size[i]
        fit[i] = fit[i]
    else:
        loan_size[i] = 0
        fit[i] = 0
    


# In[10]:


print('best solution',chromosomes[fit.index(max(fit))],"\n",'loan size',loan_size[fit.index(max(fit))],"\n",'fitness value',max(fit))


# In[ ]:





# In[ ]:




