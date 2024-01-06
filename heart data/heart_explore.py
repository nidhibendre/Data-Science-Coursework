#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:18:29 2022

@author: bendr
"""
'''
Nidhi Bendre
DS2000
Homework 6
October 28, 2022
Question 1
This program uses functions to read a dataset about patients and answer questions
relating to the patients' characteristics such as age and blood pressure and 
highlights differences between heart disease and non-heart disease patients. It
also generates a scatter plot that visualizes this difference. 

Program output:
    Number of patients: 918
    Number of patients with heart disease: 508
    Average age: 53.5109
    Average age of patients with heart disease: 55.8996
    Average resting blood pressure: 132.3965
    Average resting blood pressure of patients with heart disease: 134.185
''' 
# imports are made and constants are named
import matplotlib.pyplot as plt
FILE = 'heart.csv'

def read_data(file):
    '''
    reads in data from a given file by skipping the header and appending all 
    the values in one row in a list and combining the lists to create a 2D list.

    Parameters
    ----------
    file : string
        name of file

    Returns
    -------
    all_patients : 2D list 
        list of all patients' attributes

    '''
    # file is opened and first line is read in order to skip it
    heart_file = open(file,'r')
    skip_line = heart_file.readline() 
    all_patients = []
    # every row is split by the comma
    for line in heart_file:
        separate = line.split(",")
        each_patient = []
        # all indexes except 1 and 2 (sex and chest pain type) are stored as ints
        for i in range(len(separate)):
            if i == 0 or i in range(3,7):
                each_patient.append(int(separate[i]))
            # index 1 and 2 is stored as strings
            else:
                each_patient.append(separate[i])
        # list of each patient's attributes is appended to a bigger list and returned
        all_patients.append(each_patient)
    return all_patients


def heart_disease_patients_count(data):
    '''
    heart disease patients are separated from the bigger 2D list of all patients

    Parameters
    ----------
    data : 2D list
        list of charcteristics of all patients

    Returns
    -------
    HD_patients : 2D list
        list of characterstics of heart disease patients

    '''
    HD_patients = []
    # if the heart disease column indicates yes (1), then the patient list is 
    # appended to the list of HD_patients
    for patient in data:
        if patient[6] == 1:
            HD_patients.append(patient)
    return HD_patients


def extract_column (dataset, column_index):
    '''
    extracts a desired column from a dataset based on its index value

    Parameters
    ----------
    dataset : 2D list
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
    for row in dataset:
        column.append(row[column_index])
    return column


def average_attributes(column_list):
    '''
    finds the average of any given list of numbers

    Parameters
    ----------
    column_list : list 
        list of numerical values

    Returns
    -------
    average : integer or float
        the average of the numerical list

    '''
    # for the given list, its sum is divided by the number of items
    average = sum(column_list) / len(column_list)
    return round(average,4)
    

def visualize_patients(our_data, x_axis, y_axis, x_label, y_label):
    '''
    creates a scatter plot from lists for x and y axises.
    separates heart disease and non-heart disease patients by color.

    Parameters
    ----------
    our_data : 2D list
        list of lists of all patients data
    x_axis : list
        list of values to be plotted on the x axis
    y_axis : list
        list of values to be plotted on the y axis
    x_label : string
        label for the x axis
    y_label : string
        label for the y axis
        
    Returns
    -------
    None.

    '''
    colors = []
    # patients are given separate colors based on 1 or 0 value in the last column 
    for row in our_data:
        if row[6] == 0:
            colors.append('b')
        if row[6] == 1:
            colors.append('r')
    # the input lists are plotted and colors list is used to assign color
    plt.scatter(x_axis, y_axis, marker = '.', color = colors)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(x_label + " vs. " + y_label)
    plt.savefig("heart.png", bbox_inches="tight")
    
def main():
    # patients file is read
    patients_data = read_data(FILE)
    # number of patients is calculated by counting the number of lists in the 2D list
    print("Number of patients:", len(patients_data))
    # heart disease patients are separated and the length of this list is calculated
    patients_with_HD = heart_disease_patients_count(patients_data)
    print("Number of patients with heart disease:", len(patients_with_HD))
    # age column is extracted and the average of the column is calculated
    avg_age = average_attributes(extract_column(patients_data, 0))
    print("Average age:", avg_age)
    # age column is extracted from HD patients and the average is calculated
    avg_age_HD = average_attributes(extract_column(patients_with_HD, 0))
    print ("Average age of patients with heart disease:", avg_age_HD)
    # # blood pressure column is extracted and the average of the column is calculated
    avg_BP = average_attributes(extract_column(patients_data, 3))
    print("Average resting blood pressure:", avg_BP)
    # blood pressure column is extracted from HD patients and the average is calculated
    avg_BP_HD = average_attributes(extract_column(patients_with_HD, 3))
    print("Average resting blood pressure of patients with heart disease:", avg_BP_HD)
    # max heart rate and cholesterol columns are extracted and are used to create a scatter plot
    max_HR = extract_column(patients_data, 5)
    cholesterol = extract_column(patients_data, 4)
    visualize_patients(patients_data, max_HR, cholesterol, "Maximum Heart Rate", "Cholesterol")
   

if __name__ == "__main__":
    main()
    