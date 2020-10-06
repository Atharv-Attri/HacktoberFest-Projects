import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import math


class Node:

    def __init__(self, attribute = None):
        self.attribute = attribute
        self.children = {}
        self.group = None


class DecisionTreeClassifier:

    def __init__(self):
        self.attr_set = []
        self.class_set = {}
        self.root = None
        self.num = 0

    def set_metadata(self, X, Y):

        for i in range(self.num): 
            # accessing the attribute columns one at a time

            x = X[:, i].flatten()
            y = Y.flatten()

            # preparing details of ith attribute column
            attr_details = {}

            # dictionary for different values of categorical attribute column
            for a in set(x):
                attr_details[a] = set()

            for i, a in enumerate(x):
                attr_details[a].add(i)
            
            self.attr_set.append(attr_details)
        
        # preparing details of objective class
        for c in set(y):
            self.class_set[c] = set()
        
        for i, c in enumerate(y):
            self.class_set[c].add(i)

        return


    def entropy(self, p):

        '''
        Entropy = - P X Log(P)
        '''
        if p == 0:
            return  0
            
        return (-1 * p * math.log2(p))


    def get_base_entropy(self, remainder_indices):

        result = 0
        if (len(remainder_indices) == 0): return result

        for c in self.class_set.keys():
            p = len(self.class_set[c].intersection(remainder_indices)) / len(remainder_indices)
            result += self.entropy(p)
        
        return result


    def get_group(self, remainder_indices):
        
        best_class = None
        best_score = 0

        for c in self.class_set.keys():

            score = len( self.class_set[c].intersection(remainder_indices) )

            if (score > best_score):
                best_class = c
                best_score = score
            
            return best_class
    

    def find_best_attribute(self, attributes, indices, base):

        best_attribute = None
        best_gain = 0

        for a in list(attributes): # attribute
            score = 0
            for c in self.attr_set[a].keys(): # subclasses in every attribute

                new_indices = self.attr_set[a][c].intersection(indices)
                
                p = len(new_indices) / len(indices)

                entropy = self.get_base_entropy(new_indices)

                score += p * entropy
            
            gain = base - score

            if (gain > best_gain):
                best_gain = gain
                best_attribute = a
        
        return best_attribute


    def make_tree(self, remainder_indices, remainder_attributes, depth):
        
        if len(remainder_indices) == 0:

            root = Node()
            root.group = list(self.class_set.keys())[0]
            return root

        base_entropy = self.get_base_entropy(remainder_indices)

        if depth == 0 or len(remainder_attributes) == 0 or base_entropy == 0:

            root = Node()

            root.group = self.get_group(remainder_indices)

            return root

        best_attribute = self.find_best_attribute(remainder_attributes, remainder_indices, base_entropy)
        
        remainder_attributes.remove(best_attribute)
        
        root = Node(best_attribute)

        for c in self.attr_set[best_attribute].keys(): 

            new_indices = self.attr_set[best_attribute][c].intersection(remainder_indices)
            
            root.children[c] = self.make_tree(new_indices, remainder_attributes, depth-1)

        return root


    def fit(self, X, Y, depth):
        
        self.num = X.shape[1]
        self.set_metadata(X, Y)

        remainder_indices = set([i for i in range(Y.shape[0])])
        remainder_attributes = set([i for i in range(self.num)])

        self.root = self.make_tree(remainder_indices, remainder_attributes, depth)

        return


    def predict(self, x):

        temp = self.root
        while(temp.attribute != None):

            c = x[temp.attribute]
            temp = temp.children[c]

        return temp.group


    def evaluate(self, X, Y):

        score = 0
        total = X.shape[0]

        for i, x in enumerate(X):

            c = self.predict(x)

            if (c == Y[i]):
                score += 1
        
        return (score/total)