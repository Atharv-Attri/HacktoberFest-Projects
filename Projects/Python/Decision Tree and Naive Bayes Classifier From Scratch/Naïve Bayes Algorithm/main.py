import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import NBClassifier as NB
import Categorization as C

# getting raw csv data
raw_dataset = pd.read_csv("data/toy_dataset.csv")

# dropping N/A 
raw_dataset.dropna(inplace=True)

print('Dataset Description')
print(raw_dataset.describe())

'''
Index(['City', 'Gender', 'Age', 'Income', 'Illness'], dtype='object')
We need to discretize age & income as they are continuous attribute 
encode rest of the categorical attributes
'''
dataset = raw_dataset.copy()

dataset['City'] = C.categoric_encoder(dataset['City'])
dataset['Gender'] = C.categoric_encoder(dataset['Gender'], {'Female': 0, 'Male': 1})
dataset['Age'] = C.discretization(dataset['Age'])
dataset['Income'] = C.discretization(dataset['Income'])
dataset['Illness'] = C.categoric_encoder(dataset['Illness'], {'Yes': 1, 'No': 0})

print('Description of Preprocessed Raw dataset:')
print(dataset.describe())

# Splitting of data for training and testing
data = dataset.to_numpy()
X = data[:, :-1]
Y = data[:,  -1]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# initializing the Classifier Tree Object
model = NB.NaiveBayesAlgorithm()

# Fitting Model on Training Data
model.fit(X_train, Y_train)

print('Evaluating on the data it is trained:')
print(model.evaluate(X_train, Y_train))
# 0.9185 (results that model achieved)

print('Evaluating on testing data')
print(model.evaluate(X_test, Y_test))
# 0.92076 (results that model achieved)





