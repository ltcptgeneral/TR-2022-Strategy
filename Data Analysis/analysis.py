#this should be imported as a python module using 'import analysis'

import statistics
import math
import csv
import random
import functools

class objectives:
    
    c_names = []
    c_ids = []
    c_pos = []
    c_effects = []

    def debug(self):
        print("objectives has atributes names, ids, positions, and effects. __init__ takes self, 1d array of names, 1d array of ids, 2d array of position, 1d array of effects.")
        return [c_names, c_ids, c_pos, c_effects]
    
    def __init__ (self, names, ids, pos, effects):
        c_names = names
        c_ids = ids
        c_pos = pos
        c_effects = effects
        return None
    
    def append(self, n_name, n_id, n_pos, n_effect):
        c_names.append(n_name)
        c_ids.append(n_id)
        c_pos.append(n_pos)
        c_effects(n_effect)
        return None
    
    def edit(self, search_id, n_name, n_id, n_pos, n_effect):
        position = 0
        for i in c_ids:
            if c_ids[i] == search:
                position = i
        c_name[position] = n_name

        if n_id != "null":
            c_id[position] = n_id

        c_pos[position] = n_pos
        c_effect[position] = n_effect
        return None
    
    def search(self, search):
        position = 0
        for i in c_ids:
            if c_ids[i] == search:
                position = i

        return [c_names[position], c_ids[position], c_pos[position], c_effects[position]]

def load_csv(filepath):
    with open(filepath, newline = '') as csvfile:
        file_array = list(csv.reader(csvfile))
    return file_array

def basic_stats(data, mode, arg): # data=array, mode = [0:1_basic_stats, 1:c_basic_stats, 2:r_basic_stats], arg for mode 1 or mode 2 for column or row

    if mode == 'debug':
        out = "basic_stats requires 3 args: data, mode, arg; where data is data to be analyzed, mode is an int from 0 - 2 depending on type of analysis (by column or by row) and is only applicable to 2d arrays (for 1d arrays use mode 1), and arg is row/column number for mode 1 or mode 2; function returns: [mean, median, mode, stdev, variance]"
        return out

    if mode == 0:
    
        mean = statistics.mean(data)
        median = statistics.median(data)
        try:
            mode = statistics.mode(data)
        except:
            mode = None
        stdev = statistics.stdev(data)
        variance = statistics.variance(data)
        
        out = [mean, median, mode, stdev, variance]

        return out
    
    elif mode == 1:

        c_data = []
        c_data_sorted = []
        
        for i in data:
            c_data.append(float(i[arg]))
            
        mean = statistics.mean(c_data)
        median = statistics.median(c_data)
        try:
            mode = statistics.mode(c_data)
        except:
            mode = None
        stdev = statistics.stdev(c_data)
        variance = statistics.variance(c_data)
        
        out = [mean, median, mode, stdev, variance]

        return out

    elif mode == 2:

        r_data = []

        for i in range(len(data[arg])):
            r_data.append(float(data[arg][i]))
        
        mean = statistics.mean(r_data)
        median = statistics.median(r_data)
        try:
            mode = statistics.mode(r_data)
        except:
            mode = None
        stdev = statistics.stdev(r_data)
        variance = statistics.variance(r_data)
        
        out = [mean, median, mode, stdev, variance]

        return out
    else:
        return ["mode_error", "mode_error"]
    
def z_score(point, mean, stdev):
    score = (point - mean)/stdev
    return score

def histo_analysis(hist_data):

    if hist_data == 'debug':
        return['lower estimate (5%)', 'lower middle estimate (25%)', 'middle estimate (50%)', 'higher middle estimate (75%)', 'high estimate (95%)', 'standard deviation']
    
    derivative = []
    for i in range(0, len(hist_data) - 1, 1):
        derivative.append(float(hist_data[i+1]) - float(hist_data[i]))
        
    derivative_sorted = sorted(derivative, key=int)
    mean_derivative = basic_stats(derivative_sorted, 0, 0)[0]
    stdev_derivative = basic_stats(derivative_sorted, 0, 0)[3]

    low_bound = mean_derivative + -1.645 * stdev_derivative
    lm_bound = mean_derivative + -0.674 * stdev_derivative
    mid_bound = mean_derivative * 0 * stdev_derivative
    hm_bound = mean_derivative + 0.674 * stdev_derivative
    high_bound = mean_derivative + 1.645 * stdev_derivative

    low_est = float(hist_data[-1:][0]) + low_bound
    lm_est = float(hist_data[-1:][0]) + lm_bound
    mid_est = float(hist_data[-1:][0]) + mid_bound
    hm_est = float(hist_data[-1:][0]) + hm_bound
    high_est = float(hist_data[-1:][0]) + high_bound

    return [low_est, lm_est, mid_est, hm_est, high_est, stdev_derivative]
