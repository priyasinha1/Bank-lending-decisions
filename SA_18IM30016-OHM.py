#!/usr/bin/env python
# coding: utf-8

# # Name: Priya Sinha
# # Roll No.: 18IM30016

# In[1]:


# First we are finding the objective function value for each customer on the basis os their Loan size, Interest, Loss etc.


# In[2]:


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


# In[3]:


# Generating initial solution
chromosomes =np.random.randint(2, size=(population_size,N))
chromo = chromosomes
chromosomes


# In[4]:


# calculating cummulative probability
cum_prob = [] # storing cummulative probability
fitness = []  # storing fitness value for every chromosomes
cum_fit = []  # storing cummulative fitness
A = []        # storing the objective function value for each customer
s = 0         # for getting the overall profit for chromosome
for i in range(0,population_size):
        for j in range(0,N):
            A.append(chromosomes[i][j]*function[j])
for i in range (0,population_size*N,N):
    for j in range(i,i+N):
        s = s + A[j]
    fitness.append(s)
    s = 0
for i in range(0,population_size):
    cum_fit.append(sum(fitness[0:i+1]))
for i in range(0,population_size):
    cum_prob.append(cum_fit[i]/cum_fit[population_size-1])
    
#cum_prob


# In[5]:


# roulette wheel selection
for i in range(0,population_size):
    r3 = random.random()
    #print(r3)
    for j in range(1,population_size):
        if (r3>=cum_prob[j-1]) & (r3<cum_prob[j]):
            chromosomes[i] = chromosomes[j]
    #print(chromosomes[i])
#chromosomes


# In[6]:


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


# In[7]:


T0 = 300 #Initial Temperature  
Tf = 0  #final Temperature
n = -5  # temperature change after every iteration


# In[8]:


# Swapping
for i in range(0, population_size):
    r1= random.randint(0,9) # numbers for swappping
    #print('r1',r1)
    r2= random.randint(0,9)  # numbers for swappping
    #print('r2',r2)
    for j in range(0,10):
        temp = chromosomes[j][r1]
        chromosomes[i][r1] = chromosomes[i][r2]
        chromosomes[i][r2] = temp
#chromosomes


# In[9]:


#contraint
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


# In[10]:


# As L<= (1-k)*D therefore, the value of (1-k)*D = 51
val = 51
for i in range(0,population_size):
    if loan_size[i] <= val:
        loan_size[i] = loan_size[i]
        fit[i] = fit[i]
    else:
        loan_size[i] = 0
        fit[i] = 0


# In[11]:


fitness = []
chromo = []
LS = []
for i in range(0,population_size):
    if fit[i]!=0:
        fitness.append(fit[i])
        chromo.append(chromosomes[i])
        LS.append(loan_size[i])


# In[12]:


best_solution = fitness[0]
for i in range(1, len(fitness)):
    r3 = random.random()
    print('random number-',r3)
    if fitness[i]>= best_solution:
        best_solution = fitness[i]
    else:
        if math.exp((fit[i]-best_solution)/(T0+i*n)) > r3:
            print("Probablity",math.exp((fit[i]-best_solution)/(T0+i*n)))
            best_solution = fitness[i]
        else:
            best_solution = best_solution
    print(best_solution,"\n")


# In[13]:


print('best solution',chromo[fitness.index(best_solution)],"\n",'fitness value',best_solution,"\n",'loan_size',LS[fitness.index(best_solution)])


# In[ ]:





# In[ ]:





# In[ ]:




