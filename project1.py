#Name: Anna Kerhoulas 
#Collaborators: Claire Fuller, Abbey Hallabis
#Emails: kerhoula@umich.edu, claireaf@umich.edu, ahalabis@umich.edu
#Used ChatGPT to aid with code structure, logic design, and file writing.
#Data set used: penguins.csv

import csv
import os
import unittest

#Reading CSV into a list of dicts
def load_penguins(filename):
    data = []
    dir_path = os.path.dirname(__file__)
    file_path = os.path.join(dir_path,filename)
    with open(file_path, mode = 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    #print (data)
    return data
