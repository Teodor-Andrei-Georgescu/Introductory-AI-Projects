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

# Load the dataset
columns = [
    "class", "cap-shape", "cap-surface", "cap-color", "bruises", "odor",
    "gill-attachment", "gill-spacing", "gill-size", "gill-color", "stalk-shape",
    "stalk-root", "stalk-surface-above-ring", "stalk-surface-below-ring",
    "stalk-color-above-ring", "stalk-color-below-ring", "veil-type", "veil-color",
    "ring-number", "ring-type", "spore-print-color", "population", "habitat"
]

data = pd.read_csv("mushroom.csv", header=None, names=columns, skiprows=1)

# Encode categorical features and labels using LabelEncoder -- copied from q12
encoder = LabelEncoder()
for col in data.columns:
    data[col] = encoder.fit_transform(data[col])
    
# Separate features (X) and target (y)
X = data.drop("class", axis=1)  # Features
y = data["class"]              # Target

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Implementing my own Categorical Naive Bayes Classifier
class CategoricalNaiveBayes:
    #Init the necessary values
    def __init__(self, smoothing=1):
        self.smoothing = smoothing
        self.priors = {}
        self.likelihoods = {}
        self.classes = []
        self.features = []

    #Fit method
    def fit(self, X, y):
        #classes are all the unique values
        self.classes = np.unique(y)
        #features are all the x columns
        self.features = X.columns.tolist()

        #For each class its prior probability is number of samples in y that are in class c over total samples in y.
        for c in self.classes:
            #This check all y values and sees if they are equal to c or not
            #If equal to c it gets set to True otherwise False
            #The .mean() treats True as 1 and computes (# of Trues)/(# of values in y) 
            self.priors[c] = (y == c).mean()

        #Calculate likelihoods with smoothing
        #We want likelihoods of all features and for each class
        for feature in self.features:
            self.likelihoods[feature] = {}
            for c in self.classes:
                #Only storing Y value rows that are for the current class
                class_data = X[y == c]
                #Basically make each feature a key in a dictionary and count how many times each feature appears 
                value_counts = class_data[feature].value_counts().to_dict()

                #Get total number length of class data plus smoothing for all feautures assuming they happened "smoothing" amount of times
                #Basically just ensure each feauture doesn't have a 0 value
                total_count = len(class_data) + self.smoothing * len(X[feature].unique())
                
                #Now calculate likelihood for class for each feature
                self.likelihoods[feature][c] = {}
                for value in X[feature].unique():
                    # Get the count for the current value of a feature or default to 0
                    count = value_counts.get(value, 0)
                    
                    #Apply smoothing and calculate the likelihoodS
                    likelihood = (count + self.smoothing) / total_count
                    
                    # Store the likelihood for the current value
                    self.likelihoods[feature][c][value] = likelihood

    #Predict values based on Naive Bayes classification rule
    def predict(self, X):
        predictions = []
        
        #For each row in X we want to look more at the samples - AKA the feature values for that row/sample
        for _, sample in X.iterrows():
            
            #Will hold the probability of each class for the current sample
            posteriors = {}
            
            #Now looping through each unique class
            for c in self.classes:
                #Take log of the current class's prior probability
                posterior = np.log(self.priors[c])
                
                #Now go through all features
                for feature in self.features:
                    #Get probability of being in a class given its current feature
                    feature_value = sample[feature]
                    likelihood = self.likelihoods[feature][c].get(feature_value, 1e-10)
                    posterior += np.log(likelihood) 
                
                #Now store posterior probability of a class based on the classes probablity alone plus probabilty of each feature value resutling in the same class
                posteriors[c] = posterior
            
            #Now after going through all classes and getting all posterior probabilites our prediction is the one with the highest value
            predictions.append(max(posteriors, key=posteriors.get))
        return predictions

# Train the Categorical Naive Bayes Classifier
nb_clf = CategoricalNaiveBayes()
nb_clf.fit(X_train, y_train)

# Predict the test set
y_pred = nb_clf.predict(X_test)

# Evaluate the predictions
print(classification_report(y_test, y_pred, output_dict=True))  # Numeric report
