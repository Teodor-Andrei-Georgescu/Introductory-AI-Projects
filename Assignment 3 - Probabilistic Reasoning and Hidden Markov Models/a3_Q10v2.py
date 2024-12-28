import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def plot_distributions(hypotheses, priors, title, filename):
    """Plot the probability distributions for each hypothesis."""
    x = np.linspace(0, 100, 1000)
    plt.figure(figsize=(12, 6))
    
    for i, (mean, std) in enumerate(hypotheses):
        y = norm.pdf(x, mean, std) * priors[i]
        plt.plot(x, y, label=f'H{i+1} (Prior: {priors[i]:.2f})')
    
    plt.title(title)
    plt.xlabel('Daily Steps (thousands)')
    plt.ylabel('Probability Density')
    plt.legend()
    plt.grid(True)
    plt.savefig(filename)
    plt.close()

def likelihood(x, mean, std):
    """Calculate likelihood of observation given hypothesis parameters."""
    return norm.pdf(x, mean, std)

def main():
    # Scenario: Fitness Tracker Data Analysis
    # We have 5 hypotheses about different user activity patterns
    # Each hypothesis represents a different type of user with their expected daily step count
    
    # Hypotheses: (mean_steps, standard_deviation)
    hypotheses = [
        (3000, 500),    # H1: Sedentary user
        (5000, 800),    # H2: Light activity user
        (7500, 1000),   # H3: Moderately active user
        (10000, 1200),  # H4: Active user
        (15000, 2000)   # H5: Highly active user
    ]
    
    # Initial prior probabilities (uniform)
    priors = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
    
    # Plot initial distributions
    plot_distributions(hypotheses, priors, 
                      'Initial Activity Pattern Hypotheses',
                      'initial_distributions.png')
    
    # Simulate some observations (daily step counts)
    observations = [9800, 10200, 9900, 10100, 9700]
    
    # Perform Bayesian updating
    posteriors = priors.copy()
    
    print("Bayesian Learning Process:")
    print("\nInitial priors:", priors)
    
    for i, obs in enumerate(observations, 1):
        # Calculate likelihoods for each hypothesis
        likelihoods = np.array([likelihood(obs, mean, std) 
                               for mean, std in hypotheses])
        
        # Calculate posterior using Bayes' rule
        posteriors = likelihoods * posteriors
        posteriors = posteriors / np.sum(posteriors)  # Normalize
        
        print(f"\nAfter observation {i} ({obs} steps):")
        print("Posteriors:", posteriors)
        
        # Plot updated distributions
        plot_distributions(hypotheses, posteriors,
                         f'Updated Distributions After Observation {i}',
                         f'distribution_after_obs_{i}.png')
    
    # Maximum Likelihood Estimation
    all_observations = np.array(observations)
    mle_means = []
    mle_stds = []
    
    print("\nMaximum Likelihood Estimates for each hypothesis:")
    for i, (mean, std) in enumerate(hypotheses):
        # Calculate total likelihood for all observations
        total_likelihood = np.sum([np.log(likelihood(obs, mean, std)) 
                                 for obs in observations])
        print(f"H{i+1}: Log Likelihood = {total_likelihood:.2f}")
        
        # MLE would be the sample mean and standard deviation
        mle_means.append(np.mean(all_observations))
        mle_stds.append(np.std(all_observations))
    
    # Maximum A Posteriori Estimation
    map_hypothesis = np.argmax(posteriors) + 1
    print(f"\nMAP Estimate: Hypothesis {map_hypothesis} is most probable")
    print(f"MAP probability: {posteriors[map_hypothesis-1]:.4f}")

if __name__ == "__main__":
    main()