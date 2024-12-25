import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Define hypotheses: each hypothesis is a different calibration setting
# Each setting is represented by a Normal distribution with a specific mean and variance
hypotheses = {
    "Setting 1": {"mean": 20, "std_dev": 1},
    "Setting 2": {"mean": 22, "std_dev": 1.5},
    "Setting 3": {"mean": 24, "std_dev": 2},
    "Setting 4": {"mean": 26, "std_dev": 1},
    "Setting 5": {"mean": 28, "std_dev": 1.5}
}

# Generate synthetic data samples (observations)
np.random.seed(42)
true_hypothesis = "Setting 3"
observed_samples = np.random.normal(hypotheses[true_hypothesis]["mean"], hypotheses[true_hypothesis]["std_dev"], 50)

# Prior probabilities for each hypothesis (assumed equal here)
prior_probs = {key: 1/len(hypotheses) for key in hypotheses.keys()}

# Maximum Likelihood Estimation (MLE)
def mle(observed_samples, hypotheses):
    likelihoods = {}
    for setting, params in hypotheses.items():
        likelihood = np.prod(norm.pdf(observed_samples, params["mean"], params["std_dev"]))
        likelihoods[setting] = likelihood
    best_setting = max(likelihoods, key=likelihoods.get)
    return best_setting, likelihoods

mle_estimate, mle_likelihoods = mle(observed_samples, hypotheses)
print("Maximum Likelihood Estimate:", mle_estimate)

# Maximum a Posteriori (MAP) Estimation
def map_estimate(observed_samples, hypotheses, prior_probs):
    posterior_probs = {}
    for setting, params in hypotheses.items():
        likelihood = np.prod(norm.pdf(observed_samples, params["mean"], params["std_dev"]))
        posterior = likelihood * prior_probs[setting]
        posterior_probs[setting] = posterior
    best_setting = max(posterior_probs, key=posterior_probs.get)
    return best_setting, posterior_probs

map_estimate_result, map_posterior_probs = map_estimate(observed_samples, hypotheses, prior_probs)
print("MAP Estimate:", map_estimate_result)

# Bayesian Learning with successive samples
def bayesian_learning(observed_samples, hypotheses, prior_probs):
    posterior_probs = prior_probs.copy()
    posteriors_over_time = []
    for sample in observed_samples:
        for setting, params in hypotheses.items():
            likelihood = norm.pdf(sample, params["mean"], params["std_dev"])
            posterior_probs[setting] *= likelihood
        # Normalize to make it a probability distribution
        normalization_constant = sum(posterior_probs.values())
        for setting in posterior_probs:
            posterior_probs[setting] /= normalization_constant
        posteriors_over_time.append(posterior_probs.copy())
    return posteriors_over_time

posterior_progression = bayesian_learning(observed_samples, hypotheses, prior_probs)

# Plot the posterior progression over time
plt.figure(figsize=(12, 6))
for setting in hypotheses.keys():
    plt.plot([p[setting] for p in posterior_progression], label=f"{setting}")
plt.xlabel("Sample number")
plt.ylabel("Posterior Probability")
plt.title("Bayesian Learning: Posterior Probability Progression")
plt.legend()
plt.show()

# Save the plots as required
plt.savefig("posterior_progression.png")

# Additional test cases and output display can be added here for verification
