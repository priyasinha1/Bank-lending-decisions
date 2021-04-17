# Bank-lending-decisions

Here we are using genetic algorithm and simulated annealing for optimizing the Bank lending decisions. A model that facilitates how banks would make an efficient decision while staying focus on the main objective of bank profit maximization.
![image](https://user-images.githubusercontent.com/64432440/115115742-af10ac80-9fb3-11eb-92b7-61976cc970c6.png)

  ![image](https://user-images.githubusercontent.com/64432440/115115783-ee3efd80-9fb3-11eb-8ac7-e7add98afe75.png)
  
Steps:
Step 1: Imported libraries numpy, random, math
Step 2: Declared values for N, population_size, D, k, insti_cost, rD
Step 3: Stored the values for loan size, loan interest rate, loss
Step 4: Created empty arrays to store the values of loan_revenue, loan_cost, total_transaction_cost, cost_demand_deposit, function
Step 5: Got profit value as output for every customer.
Step 6: Generating 60 chromosomes and storing them in 2d array
Step 7: Calculating the cumulative probability for each chromosome and storing them in array cum_fit
Step 8: Applying roulette wheel selection and updating the value of chromosomes in array.
Step 9: Sorting array according to their fitness value (from low to high) using bubble sort
Step 10: Applying crossover on the rest of chromosomes which do not undergo reproduction.
Step 11: After crossover applying mutation on those chromosomes
Step 12: Declaring T0, Tf, n
Step 13: Swapping the randomly chosen bits and updating array chromosome
Step 14: Eliminating chromosomes which violates the constraint (L <= (1-k) *D)
Step 15: Storing the rest of chromosomes in chromo and fitness value in fitness.
Step 16: declaring best_solution and applying simulated annealing and updating the value of best solution accordingly.
Step 17: Printing the value of best solution and respective chromosome.



