import pandas as pd
import numpy as np

'''
P(A & B) = P(A | B) X P(B)  OR  P(B | A) X P(A)

Hence
    P(Class) P(Attributes | Class) = P(Class | Attributes) * P(Attributes)

    Therefore,
    
    P(Class) = [ P(Class | Attributes) * P(Attributes) ] / P(Attributes | Class)

    P(C) = [ P(C | A1, A2, ..,An) * P(A1, A2, ..,An)] / P(A1, A2, ..,An | C)

    P(C) = P(C | A1) * P(C | A2) * ... * P(C | An) * P(A1) * P(A2) * ... * P(An)
            __________________________________________________________________
                      
                      P(A1 | C) * P(A2 | C) * ... * P(An | C)

'''

class NaiveBayesAlgorithm:

    def __init__(self):
        self.count = {}
        self.P = {}
        self.classes = None

    def initialize_count(self, X, Y):

        for x, y in zip(X, Y):
            '''
            x = [a1, a2, ..., an] Y = [C]
            '''
            for i, a in enumerate(x):

                self.count['C' + str(y) + '|' + 'A' + str(i) + str(a)] = self.count.get('C' + str(y) + '|' + 'A' + str(i) + str(a), 0) + 1

                self.count['A' + str(i) + str(a) + '|' + 'C' + str(y)] = self.count.get('A' + str(i) + str(a) + '|' + 'C' + str(y), 0) + 1
                
                self.count['A' + str(i) + str(a) + '_'] = self.count.get('A' + str(i) + str(a) + '_', 0) + 1

            self.count['C' + str(y) + '_'] = self.count.get('C' + str(y) + '_', 0) + 1

        return

    def initialize_probability(self, n):

        for k in self.count.keys():
            
            if k[-1] != '_':
                self.P[k] = self.count[k] / self.count[k[k.find('|') + 1:] + '_']
            
            else:
                self.P[k] = self.count[k] / n
        
        return

            

    def fit(self, X, Y):

        self.classes = sorted( list( set( list( Y.flatten() ))))
        
        self.initialize_count(X, Y)

        self.initialize_probability(X.shape[0])

        return
    
    
    def numerator(self, c, x):

        result = 1

        for i, a in enumerate(x):
            result *= self.P['A' + str(i) + str(a) + '_']
            result *= self.P['C' + str(c) + '|' + 'A' + str(i) + str(a)]
        
        return result
        
    
    def denominator(self, c, x):

        result = 1

        for i, a in enumerate(x):
            result *= self.P['A' + str(i) + str(a) + '|' + 'C' + str(c)]
        
        return result
        

    def predict(self, x):

        best_class = self.classes[0]
        best_score = 0

        for c in self.classes:

            n = self.numerator(c, x)
            d = self.denominator(c, x)
            score = n/d

            if (score > best_score):
                best_class = c
                best_score = score
        
        return best_class, best_score
        

    def evaluate(self, X, Y):
        correct = 0
        total = X.shape[0]

        for x, y in zip(X, Y):

            c, _ = self.predict(x)

            if(c == y):
                correct += 1
        
        accuracy = correct / total
        return accuracy