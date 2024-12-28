# Assignment 3: Probabilistic Reasoning and Hidden Markov Models

This directory contains all files for **Assignment 3** of the CSC421 Fall 2024 course. The assignment focuses on **probabilistic reasoning**, **Bayesian networks**, **random variables**, and **Hidden Markov Models (HMMs)**. Below is an overview of the questions and file structure. For detailed explanations of the questions, please refer to the screenshots provided.

## Overview of Questions

### Question 1 (Basic): Non-Transitive Dice
- Explore random variables by simulating a dice war game with non-transitive dice.
- Use the provided `dice_war` function to demonstrate counter-intuitive results, where:
  - The Red die beats the Green die.
  - The Green die beats the Blue die.
  - The Blue die beats the Red die.

### Question 2 (Basic): Bayesian Networks
![Asia Network](./Asia%20Network.PNG)
- Use the conventions for Bayesian Networks defined in the AIMA repository.
- Encode the provided "Asia" problem as a Bayesian network.
- Answer queries using exact inference (enumeration) and approximate inference (rejection sampling and likelihood weighting).

### Question 3 (Expected): Bayesian Inference
- Evaluate the likelihood of a patient having specific conditions based on symptoms.
- Implement exact inference using enumeration and approximate inference using rejection sampling.

### Question 4 (Expected): Modeling a Coin and Dice Game
- Model a board game involving a coin toss and dice rolls using random variables.
- Calculate probabilities for the random variable `CD` (Coin x Dice outcome).
- Use exact and approximate inference methods to evaluate `CD`.

### Question 5 (Advanced): Random Variables in Games
- Extend Question 4 to compute exact and approximate values for the coin-dice outcome.
- Use a `RandomVariable` class to define variables and calculate distributions.

### Questions 6, 7, 8, 9: Hidden Markov Models (HMMs)
- Model DNA sequences using HMMs with states for CG-dense and CG-sparse regions.
- Use the transition probabilities and observation probabilities provided to analyze DNA sequences.
- Generate visualizations of posterior distributions and observe how beliefs update with new observations.

## File Structure
- **`a3_q1.py`**: Solution for Question 1 (Non-Transitive Dice).
- **`a3_q23.py`**: Solutions for Questions 2 and 3 (Bayesian Networks and Inference).
- **`a3_q45.py`**: Solutions for Questions 4 and 5 (Random Variables and Board Game Modeling).
- **`a3_q6789.py`**: Solutions for Questions 6 through 9 (HMMs for DNA sequences).
- **`Question Description screenshots`**: Contains screenshots of each question description.
