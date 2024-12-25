
# Modify this code as needed

import numpy as np
from scipy import stats


class Random_Variable:

    def __init__(self, name, values, probability_distribution):
        self.name = name
        self.values = values
        self.probability_distribution = probability_distribution
        if all(issubclass(type(item), np.integer) for item in values):
            self.type = 'numeric'
            self.rv = stats.rv_discrete(name = name, values = (values, probability_distribution))
        elif all(type(item) is str for item in values):
            self.type = 'symbolic'
            self.rv = stats.rv_discrete(name = name, values = (np.arange(len(values)), probability_distribution))
            self.symbolic_values = values
        else:
            self.type = 'undefined'

    def sample(self,size):
        if (self.type =='numeric'):
            return self.rv.rvs(size=size)
        elif (self.type == 'symbolic'):
            self.rv = stats.rv_discrete(name = name, values = (np.arange(len(values)), probability_distribution))
            self.symbolic_values = values
        else:
            self.type = 'undefined'

    def sample(self,size):
        if (self.type =='numeric'):
            return self.rv.rvs(size=size)
        elif (self.type == 'symbolic'):
            numeric_samples = self.rv.rvs(size=size)
            mapped_samples = [self.values[x] for x in numeric_samples]
            return mapped_samples

    def get_name(self):
        return self.name

values = np.array([1,2,3,4,5,6])
probabilities_A = np.array([1/6., 1/6., 1/6., 1/6., 1/6., 1/6.])
probabilities_B = np.array([0.0, 0.0, 0/6., 3/6., 3/6., 0/6.])

dieA = Random_Variable('DieA', values, probabilities_A)
dieB = Random_Variable('DieB', values, probabilities_B)

def dice_war(A,B, num_samples = 1000, output=True):
    # your code goes here and calculates appropriately prob
    prob = 0
    
    A_values = A.values
    A_probability = A.probability_distribution
    B_values = B.values
    B_probability = B.probability_distribution
    
    A_wins = 0
    for _ in range(num_samples):
        roll_A = np.random.choice(A_values, p=A_probability)
        roll_B = np.random.choice(B_values, p=B_probability)
        
        if roll_A > roll_B:
            A_wins += 1
    if A_wins:
        prob = A_wins / num_samples
    res = prob > 0.5

    if output:
        if res:
            print('{} beats {} with probability {}'.format(A.get_name(),
                                                           B.get_name(),
                                                           prob))
        else:
            print('{} beats {} with probability {:.2f}'.format(B.get_name(),
                                                               A.get_name(),
                                                               1.0-prob))
    return (res, prob)



dice_war(dieA, dieB, 1000)

# Define red, green, and blue appropriately
red_values = [2, 2, 4, 4, 9, 9]
blue_values = [1, 1, 6, 6, 8, 8]
green_values = [3, 3, 5, 5, 7, 7]
uniform_probablity = np.array([1/6,1/6,1/6,1/6,1/6,1/6])

red = Random_Variable('red', red_values, uniform_probablity)
blue = Random_Variable('blue', blue_values, uniform_probablity)
green = Random_Variable('green', green_values, uniform_probablity)
# Uncomment the code below when the random variables for the red, green, and blue die
# have been defined

dice_war(red, green, 1000)
dice_war(green, blue, 1000)
dice_war(blue, red, 1000)





