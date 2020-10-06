import pandas as pd
import numpy as np

# categorization

def discretization(attr_list):

    sorted_list = sorted(attr_list)

    '''
    Our Discretization Method:

    Q 0            Q 1            Q 2            Q 3             Q 4
    0 % --------- 25 % --------- 50 % --------- 75 % --------- 100 % 
    
    score - 0             1               2              3

    '''

    attr_map = dict()
    multiple = len(attr_list) / 4
    next = multiple

    for index in range(4):
        attr_map[index] = sorted_list[int(next-1)] 
        next += multiple
    result = []

    for val in attr_list:
        for i in range(4):
            if val <= attr_map[i]:
                result.append(i)
                break
    
    return result


def categoric_encoder(attr_list, attr_map = {}):

    i = 0

    if len(attr_map) == 0:
        attr_set = set(attr_list)
        for a in attr_set:
            attr_map[a] = i
            i += 1
        
    result = []
    
    for a in attr_list:
        try:
            result.append(attr_map[a])
        except:
            print("'" + a + "'")
    
    return result