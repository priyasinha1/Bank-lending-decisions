# Bank-lending-decisions

Here we are using genetic algorithm and simulated annealing for optimizing the Bank lending decisions. A model that facilitates how banks would make an efficient decision while staying focus on the main objective of bank profit maximization.
![image](https://user-images.githubusercontent.com/64432440/115115742-af10ac80-9fb3-11eb-92b7-61976cc970c6.png)

  ![image](https://user-images.githubusercontent.com/64432440/115115783-ee3efd80-9fb3-11eb-8ac7-e7add98afe75.png)
  
Steps:<br/>
Step 1: Imported libraries numpy, random, math<br/>
Step 2: Declared values for N, population_size, D, k, insti_cost, rD<br/>
Step 3: Stored the values for loan size, loan interest rate, loss<br/>
Step 4: Created empty arrays to store the values of loan_revenue, loan_cost, total_transaction_cost, cost_demand_deposit, function<br/>
Step 5: Got profit value as output for every customer.<br/>
Step 6: Generating 60 chromosomes and storing them in 2d array<br/>
Step 7: Calculating the cumulative probability for each chromosome and storing them in array cum_fit<br/>
Step 8: Applying roulette wheel selection and updating the value of chromosomes in array.<br/>
Step 9: Sorting array according to their fitness value (from low to high) using bubble sort<br/>
Step 10: Applying crossover on the rest of chromosomes which do not undergo reproduction.<br/>
Step 11: After crossover applying mutation on those chromosomes<br/>
Step 12: Declaring T0, Tf, n<br/>
Step 13: Swapping the randomly chosen bits and updating array chromosome<br/>
Step 14: Eliminating chromosomes which violates the constraint (L <= (1-k) *D)<br/>
Step 15: Storing the rest of chromosomes in chromo and fitness value in fitness.<br/>
Step 16: declaring best_solution and applying simulated annealing and updating the value of best solution accordingly.<br/>
Step 17: Printing the value of best solution and respective chromosome.<br/>

Result:

![image](https://user-images.githubusercontent.com/64432440/115115932-aa002d00-9fb4-11eb-8ca1-1cfd97b55b6d.png)
Best solution obtained so far:
Chromosomes: [1 0 1 1 0 1 0 0 1 1]
Fitness: 4.1494


