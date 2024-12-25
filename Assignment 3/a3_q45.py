# Modify this code as needed 

import numpy as np
from scipy import stats
from collections import defaultdict, Counter


rng = np.random.default_rng(10)


class Random_Variable: 
    
    def __init__(self, name, values, probability_distribution): 
        self.name = name 
        self.values = values 
        self.probability_distribution = probability_distribution
        if all(issubclass(type(item), np.integer) for item in values):
            self.type = 'numeric'
            self.rv = stats.rv_discrete(name = name, values = (values, probability_distribution), seed=rng)
        elif all(type(item) is str for item in values): 
            self.type = 'symbolic'
            self.rv = stats.rv_discrete(name = name, values = (np.arange(len(values)), probability_distribution), seed=rng)
            self.symbolic_values = values 
        else: 
            self.type = 'undefined'

    def __str__(self):
        sres = "values: " + str(self.values) + "\n" + "probs :"  + str(self.probability_distribution)
        return sres
    
    def sample(self,size): 
        if (self.type =='numeric'):
            return self.rv.rvs(size=size)
        elif (self.type == 'symbolic'): 
            numeric_samples = self.rv.rvs(size=size)
            mapped_samples = [self.values[x] for x in numeric_samples]
            return mapped_samples

    def get_name(self):
        return self.name

    def get_values(self):
        return self.values

    def get_probability_distribution(self):
        return self.probability_distribution  


vals_coin = np.array([1,2])
probs_coin  = np.array([0.5, 0.5])
coin = Random_Variable("coin", vals_coin, probs_coin)
vals_die = np.array([1,2,3,4,5,6])
probs_die = np.array([1/6., 1/6., 1/6., 1/6., 1/6., 1/6.])
die1 = Random_Variable("die1", vals_die, probs_die)
die2 = Random_Variable("die2", vals_die, probs_die)


# APPROXIMATE INFERENCE
# Calculate using approximate inference the values and associated probabilities
# for the random variable CD = C * (D1 + D2) where C is a coin random variable
# and D1 and D2 are die random variables. Do so by generating 10000 samples
# of each random variable calculating the corresponding 10000 values of CD
# and then using frequency counting to estimate the values and probabilities
# of the coin-dice random variable.

num_samples=10000
coin_samples = coin.sample(num_samples)
die1_samples = die1.sample(num_samples)
die2_samples = die2.sample(num_samples)

cd_samples = []
for i in range(num_samples):
    c = coin_samples[i]
    d1 = die1_samples[i]
    d2 = die2_samples[i]
    cd_samples.append(c * (d1 + d2))

cd_freqs = {}
for value in cd_samples:
    if value in cd_freqs:
        cd_freqs[value] += 1
    else:
        cd_freqs[value] = 1

approximate_vals_coin_dice = []
approximate_probs_coin_dice = []

for value, count in cd_freqs.items():
    approximate_vals_coin_dice.append(value)
    approximate_probs_coin_dice.append(count / num_samples)

approximate_vals_coin_dice = np.array(approximate_vals_coin_dice)
approximate_probs_coin_dice = np.array(approximate_probs_coin_dice)

sorted_indices = np.argsort(approximate_vals_coin_dice)
approximate_vals_coin_dice = approximate_vals_coin_dice[sorted_indices]
approximate_probs_coin_dice = approximate_probs_coin_dice[sorted_indices]

# Uncomment the following lines once you have approximate inference working
# The approximate_vals_coin_dice and approximate_probs_coin_dice variables
# should be np.arrays

approximate_coin_dice = Random_Variable("approximate_coin_dice", approximate_vals_coin_dice,
                                       approximate_probs_coin_dice)

print("APPROXIMATE INFERENCE")
print(approximate_vals_coin_dice)
print(approximate_probs_coin_dice) 
print(approximate_coin_dice)
print(approximate_coin_dice.sample(20))

# EXACT INFERENCE 
# Calculate using exact inference the values and probabilities of CD.
# You will need to calculate all the possible combinations of values
# and look up the associated probability distributions.
# Write a function rv_op that takes as argument two random variables
# and returns a new random variable that is the result of applying the
# operator f to their values (you will need a sum and prod version)
# There are different ways of implementing this function. I suggest
# you use a default dictionary with keys the values of the resulting
# random variable and as dictionary value the associated probaibities.  

# YOUR CODE GOES HERE 
def rv_op(rv1, rv2, f):
    results = {}
    
    rv1_values = rv1.get_values()
    rv1_probs = rv1.get_probability_distribution()
    rv2_values = rv2.get_values()
    rv2_probs = rv2.get_probability_distribution()
    
    for i in range(len(rv1_values)):
        v1 = rv1_values[i]
        p1 = rv1_probs[i]
        for j in range(len(rv2_values)):
            v2 = rv2_values[j]
            p2 = rv2_probs[j]
            
            result_value = f(v1,v2)
            if result_value in results:
                results[result_value] += p1*p2
            else:
                results[result_value] = p1*p2\
                    
    result_values = np.array(list(results.keys()))
    result_probs = np.array(list(results.values()))

    sorted_indices = np.argsort(result_values)
    result_values = result_values[sorted_indices]
    result_probs = result_probs[sorted_indices]
    
    return Random_Variable("res", result_values, result_probs)

# Uncomment these lines once you have a functionining rv_op 
dice = rv_op(die1, die2, lambda a,b:a+b)
coin_dice = rv_op(coin, dice, lambda a,b:a*b)

print("EXACT INFERENCE")

vals_coin_dice = coin_dice.get_values()
probs_coin_dice = coin_dice.get_probability_distribution()
print(vals_coin_dice)
print(probs_coin_dice)
print(coin_dice)
print(coin_dice.sample(20))


