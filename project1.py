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

### Anna Kerhoulas's Calculation 1: Average Beak Size
### COLUMNS USED: species, bill_length_mm, bill_depth_mm
### Helper Function:
def get_penguin_beaksize(penguins, species): 
    sizes_list = []
    for p in penguins:
        if (p['species'] == species and p['bill_length_mm'] != 'NA' and p['bill_depth_mm'] != 'NA'):
            # Calculate overall beak size as the average of bill length and bill depth (in mm)
            beak_size = (float(p['bill_length_mm']) + float(p['bill_depth_mm'])) / 2
            sizes_list.append(beak_size)
    return sizes_list
### Primary Function: 
def average_beak_size(penguins):
    species_averages = {}
    species_list = list(set(p['species'] for p in penguins if p['species'] != ''))
    for species in species_list:
        sizes = get_penguin_beaksize(penguins, species)
        if sizes:
            species_averages[species] = sum(sizes) / len(sizes)
    # Print only the species that exist (to handle edge cases)
    for species in ['Adelie','Gentoo','Chinstrap']:
        if species in species_averages:
            print(f"Average beak size for {species}: {species_averages[species]:.3f}")
    return species_averages

### Anna Kerhoulas Calculation 2: Year that they collected most data on penguins.
### COLUMNS USED: year, island, species
### Primary Function:
def find_year_most_data(penguins):
    combo_counts = {}
    for p in penguins:
        year = p['year']
        island = p['island']
        species = p['species']
        combo = (year, island, species)
        combo_counts[combo] = combo_counts.get(combo, 0) + 1
    # Find which (year, island, species) combination has the most data entries
    top_combo = max(combo_counts, key=combo_counts.get)
    top_year, top_island, top_species = top_combo
    top_count = combo_counts[top_combo]
    print(f"The most penguin data was collected in {top_year} on {top_island} Island for {top_species} penguins ({top_count} entries).")
    return top_year, top_island, top_species

### Writing my results to a file.
def write_results_to_file(averages, top_year, top_island, top_species):
    with open("penguin_results.txt", "w") as f:
        f.write(" Penguin Data Analysis Results \n\n\n")
        # Anna Kerhoulas Calculation 1: Beak size results
        f.write(" Average Beak Sizes (mm):\n")
        f.write("(Beak size calculated as the average of bill length and bill depth.)\n\n")
        f.write(f"  Adelie: {averages['Adelie']:.3f} mm\n")
        f.write(f"  Gentoo: {averages['Gentoo']:.3f} mm\n")
        f.write(f"  Chinstrap: {averages['Chinstrap']:.3f} mm\n\n")
        # Anna Kerhoulas Calculation 2: Year/Island/Species with most data
        f.write(f" The most penguin data was collected in {top_year} on {top_island} Island for {top_species} penguins.\n\n")

    print(" Results written to penguin_results.txt")

def main():
    penguins = load_penguins("penguins.csv")
    averages = average_beak_size(penguins)
    top_year, top_island, top_species = find_year_most_data(penguins)
    write_results_to_file(averages, top_year, top_island, top_species)
 
main()
