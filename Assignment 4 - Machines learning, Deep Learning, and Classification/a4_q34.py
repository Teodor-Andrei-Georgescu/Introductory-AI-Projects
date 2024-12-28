
import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn import datasets, svm
from sklearn import tree
from sklearn.naive_bayes import CategoricalNB
from sklearn.datasets import load_digits
from sklearn.naive_bayes import GaussianNB


# Question 4.3 

digits = load_digits()
print("Digits shape: ", digits.data.shape)

# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Split data into 50% train and 50% test subsets
Xd_train, Xd_test, yd_train, yd_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)


# Train a GaussianNB classifier and store
# the predictions over Xd_test in yd_predict 

gaussian_clf = GaussianNB()
gaussian_clf.fit(Xd_train, yd_train) 
yd_predict = gaussian_clf.predict(Xd_test) 
clf = classification_report(yd_test, yd_predict, output_dict=True)

print(
    f"Classification report for classifier {clf}:\n"
    f"{classification_report(yd_test, yd_predict)}\n"
)
gaussian_digits_report = classification_report(yd_test, yd_predict,output_dict=True)
# Find the gaussian_accuracy rounding to two digits 
gaussian_accuracy = np.round(gaussian_digits_report["accuracy"],2)


# Based on the classification report calculate a list of digits sorted by f1-score 
# Each item should be an integer

digits = []
sorted_digits = []

for k, v in gaussian_digits_report.items():
    if k.isdigit():
        digits.append((int(k), v["f1-score"]))

digits.sort(key=lambda x: x[1])

for digit_score in digits:
    sorted_digits.append(digit_score[0])

# Repeat the process for a SVM classifier

svm_clf = svm.SVC() 
svm_clf.fit(Xd_train, yd_train) 
yd_predict_svm = svm_clf.predict(Xd_test)  
svm_digits_report = classification_report(yd_test, yd_predict_svm, output_dict=True)
svm_accuracy = np.round(svm_digits_report["accuracy"], 2)

print(sorted_digits) 
print("Digits - Gaussian Accuracy", gaussian_accuracy)
print("Digits - SVM Accuracy", svm_accuracy)

