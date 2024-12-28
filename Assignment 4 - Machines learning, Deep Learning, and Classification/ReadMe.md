# Assignment 4: Machine Learning, Deep Learning, and Classification

This directory contains all files for **Assignment 4** of the CSC421 Fall 2024 course. The assignment focuses on **machine learning**, **deep learning**, and **classification tasks**. Below is an overview of the questions and file structure. For detailed explanations of the questions, please refer to the screenshots provided.

## Overview of Questions

### Questions 1, 2: Learning from Data
- Use the mushroom dataset (`mushroom.csv`) to train a Categorical Naive Bayes classifier.
- Create new training and testing sets by focusing only on specific features (e.g., `cap_shape`).
- Compare the classification accuracy when considering all features versus only selected features.
- Repeat the process for a decision tree classifier with a maximum depth of 2.

### Questions 3, 4: Classification of Handwritten Digits
- Work with the digits dataset, processing images into vectors.
- Train a Naive Bayes Gaussian classifier and an SVM classifier to calculate classification accuracy.
- Sort digits by their F1-scores, from hardest to easiest to classify.

### Question 5: Probabilistic Mushroom Classifier
- Calculate probabilities for a categorical Naive Bayes classifier focusing on the `cap_shape` attribute.
- Implement functions to compute prior and posterior probabilities for mushroom edibility based on the dataset.

### Question 6: Implementing Naive Bayes Classifier
- Develop a full Categorical Naive Bayes classifier from scratch (without using libraries like `sklearn`).
- Use the classifier to predict results for the mushroom dataset and generate a classification report.

### Question 7: Deep Learning with PyTorch
- Train a deep neural network using the CIFAR-10 dataset.
- Add random noise to the dataset and observe its impact on classification accuracy.
- Visualize noisy images and assess how adding noise affects test accuracy while keeping the training data intact.

## File Structure
- **`a4_q12.py`**: Solutions for Questions 1 and 2 (mushroom dataset classification).
- **`a4_q34.py`**: Solutions for Questions 3 and 4 (digits dataset classification).
- **`a4_q5.py`**: Solution for Question 5 (probabilistic mushroom classifier).
- **`a4_q6.py`**: Solution for Question 6 (manual Naive Bayes implementation).
- **`a4_q7.py`**: Solution for Question 7 (deep learning with PyTorch).
- **`mushroom.csv`**: Dataset used for mushroom classification tasks.
- **`Question Description screenshots`**: Contains screenshots of each question description.
