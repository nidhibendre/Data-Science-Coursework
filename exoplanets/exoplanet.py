#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 18:32:40 2022

@author: bendr
"""
'''
Nidhi Bendre
DS2000
Homework 5
October 21, 2022
Question 1
This program, through a series of functions, determines the planet most simiar
to Earth by reading data of a planetary dataset, finding a planet with the least
euclidean distance from Earth, generating a readable report of all the attributes
of the most similar planet, and plots a scatter plot of mass vs semimajor axis
and a red x for the Earth point. 

Program output:
    Planet most like Earth is:
    planet name: TRAPPIST-1 d
    planet mass (Earth mass): 0.29690926
    planet radius (Earth radius): 0.7672418000000001
    planet orbital period (years): 0.011088039662448644
    planet semimajor axis (AU): 0.02228038
    planet surface temperature (K): 288.0
    The euclidean distance between Earth and TRAPPIST-1 d is 1.5755117881439684
    
''' 
import matplotlib.pyplot as plt
FILE = "exoplanets.csv"

def read_data(file):
    '''
    reads in the data from a given file and stores 6 attributes of a planet
    in a 2D list.
    Commas are used to separate column values in each row.
    
    Parameters
    ----------
    file : string
        name of the file to be read

    Returns
    -------
    all_planets : 2D list
        list of lists of strings and floats for all lines in the file
    '''
    # file is opened and all lines are read
    curr_file = open(file, "r") 
    all_data_lines = curr_file.readlines()
    all_planets = []
    # each line is split based on commas in order to separate the columns
    for line in all_data_lines:
        split = line.split(",") 
        planet = []
        # the lines with #'s are skipped
        if split[0][:1] != "#":
            # all unpresent values are replaced with 0.0
            for i in range(len(split)):
                if split[i] == '':
                    split[i] = 0.0
            # necessary columns are appended to a list with necessary calculations
            planet.append(split[0])
            earth_mass = 317.89 * float(split[2])
            planet.append(earth_mass)
            earth_radius = 10.97 * float(split[3])
            planet.append(earth_radius)
            years = float(split[4]) / 365.2422
            planet.append(years)
            planet.append(float(split[5]))
            planet.append(float(split[11]))
            # list with info about each planet is appended to a bigger list 
            all_planets.append(planet)
    return all_planets

        
def lookup_planet(planet, data):
    '''
    extracts the attributes of a specific planet from a given dataset
    
    Parameters
    ----------
    planet : string
        name of the planet
    data : 2D list
        dataset from which the planet data needs to be extracted

    Returns
    -------
    each_planet : list
        a list of attributes of the desired planet
    '''
    each_planet = []
    # checks to see if the first element in every list matches the parameter
    for ls in data:
        if ls[0] == planet:
            # if matching planet is found, each of its attributes is appended to a list
            for value in ls:
                each_planet.append(value)
    return each_planet


def euclidean_distance(planet1_data, planet2_data):
    '''
    uses planet attributes of two planets to calculate the euclidean distance 
    between the two.

    Parameters
    ----------
    planet1_data : list
        6 attributes of the first planet
    planet2_data : list
        6 attributes of the second planet

    Returns
    -------
    euclid : float
        the euclidean distance score between the two planets
    '''
    # all differences are calculated
    diff_mass = planet1_data[1] - planet2_data[1]
    diff_radius = planet1_data[2] - planet2_data[2]
    diff_period = planet1_data[3] - planet2_data[3]
    diff_axis = planet1_data[4] - planet2_data[4]
    diff_temp = planet1_data[5] - planet2_data[5]
    # euclidean distance is calculated based on differences
    euclid = ((diff_mass ** 2) + (diff_radius ** 2) + (diff_period ** 2) + 
              (diff_axis ** 2) + (diff_temp ** 2)) ** 0.5
    return euclid


def find_most_similar_planet(planet_name, dataset):
    '''
    finds the planet that is most similar (planet with the least euclidean distance)
    to a certain planet from a certain dataset.

    Parameters
    ----------
    planet_name : string
        name of planet of which the most similar planet is needed
    dataset : 2D list
        dataset that contains info about all planets

    Returns
    -------
    sim_planet : string
        name of the planet that is most similar to the planet in the parameter
    '''
    # data for the parameter planet is gathered
    our_planet = lookup_planet(planet_name, dataset)
    all_euclids = []
    smallest = 10000000
    sim_planet = dataset[0][0]
    # data for each planet in the dataset is gathered
    for ls in dataset:
            every_planet = lookup_planet(ls[0], dataset)
            # euclidean score is calcuated for the curr planet with the desired planet
            this_euclid = euclidean_distance(our_planet, every_planet)
            # each score is appended to a list
            all_euclids.append(this_euclid)
            # the eculidean distance between the asked planet and itself is skipped
            if this_euclid != 0:
                # for each euclidean score, if it is smaller than the one before
                # then the smallest is value is changed and the sim_planet is
                # changed to be the planet with the smallest euclidean
                if this_euclid < smallest:
                    smallest = this_euclid
                    sim_planet = every_planet[0]
    return sim_planet
    

def generate_planet_report(read_planet, from_data):
    '''
    prints a readable report of a desired planet from the given dataset

    Parameters
    ----------
    read_planet : string
        name of planet who's info is needed
    from_data : 2D list
        list of lists of planetary info

    Returns
    -------
    None.
    '''
    # planet who's attributes are needed is looked up and data is gathered
    planet_data = lookup_planet(read_planet, from_data)
    # each value is printed on a new line
    print("planet name:", planet_data[0])
    print("planet mass (Earth mass):", planet_data[1])
    print("planet radius (Earth radius):", planet_data[2])
    print("planet orbital period (years):", planet_data[3])
    print("planet semimajor axis (AU):", planet_data[4])
    print("planet surface temperature (K):", planet_data[5])


def extract_column (data, column_index):
    '''
    extracts a desired column from a dataset based on its index value

    Parameters
    ----------
    data : 2D list
        list of lists where each column has the same index value in each inner list.
    column_index : integer
        the index of the column that is needed.

    Returns
    -------
    column : list
        returns a list of all values at the index requested from all inner lists
    '''
    column = []
    # in each row, the value at desired index is appended to a list
    for row in data:
        column.append(row[column_index])
    return column

def visualize_exoplanets(x_axis, y_axis, our_data, x_label, y_label):
    '''
    generates a scatter plot based on lists for x and y axises.
    plots the point for earth using the 2D planetary dataset

    Parameters
    ----------
    x_axis : list
        list of values needed to be plot on the x axis
    y_axis : list
        list of values needed to be plot on the y axis
    our_data : 2D list
        list of lists from which Earth data is plotted
    x_label : string
        title of the x axis
    y_label : string
        title of the y axis

    Returns
    -------
    None.
    '''
    # Earth data is looked up and its mass and semimajor axis is plotted and labeled
    Earth_data = lookup_planet("Earth", our_data)
    plt.plot(Earth_data[1], Earth_data[4], marker = ("X"), ms = 10, color = "red")
    plt.text(Earth_data[1], Earth_data[4], "Earth")
    # a scatter plot of desired x and y axis values is created
    plt.scatter(x_axis, y_axis, marker = ".", color = "purple")
    # axises and title are labeled based on the label parameters
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xscale('log')
    plt.yscale('log')
    plt.title(x_label + " vs. " + y_label)
    plt.savefig("exoplanet.png", bbox_inches="tight")


def main():
    # exoplanets.csv is read
    exo_data = read_data(FILE)
    # planet like earth is found
    like_earth = find_most_similar_planet("Earth", exo_data)
    # a readable report of the planet like earth is printed
    print("Planet most like Earth is:")
    generate_planet_report(like_earth, exo_data)
    # the euclidean distance between the two is printed by looking up data of both
    # and calculating the score
    Earth_data = lookup_planet('Earth', exo_data)
    like_earth_data = lookup_planet(like_earth, exo_data)
    print("The euclidean distance between Earth and", like_earth, "is", euclidean_distance(Earth_data, like_earth_data))
    # scatter plot is created is created for mass vs. semimajor axis
    mass = extract_column(exo_data, 1)
    semimajor_axis = extract_column(exo_data, 4)
    visualize_exoplanets(mass, semimajor_axis, exo_data, "Mass (Earth Mass)", "Semimajor Axis (AU)")
    
main ()
