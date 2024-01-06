#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 19:14:22 2022

@author: bendr
"""
'''
Nidhi Bendre
DS2000
Homework 4
October 7, 2022
Question 1
this program reads a given file of rodent reports that includes neighborhood names, 
latitudes, and longitudes of the report. It reads the file and plots the coordinates
of all reports relative to Northeastern's location. The neighborhoods list is filtered
so that repeats are dropped and it is sorted alphabetically. The number of rodent
reports per neighborhod is then plotted as a bar graph. Total number of rodent
reports and average reports per neighborhood is calculated and printed
''' 
import matplotlib.pyplot as plt 

def main():
    
    # variable represents file name, which is interchangeable
    curr_file = 'rodents_311_2021.csv'
    
    # lists storing neighborhood names, latitudes, and longitudes of the rodent
    # reports are called
    neighborhoods = []
    latitude = []
    longitude = [] 
    
    # Northeastern coordinates are saved in a variable
    NU_latitude = 42.3398
    NU_longitude = -71.0892
    
    #desired file is opened and first line is read and saved in a variable 
    # so that it can be skipped
    rodents_file = open(curr_file,'r')
    lines_in_file = rodents_file.readline() 
    
    # the for loop reads every line in rodents_file, then breaks it based on the commas. 
    # If the first segment of the split isn't empty (if neighborhood isn't present), then 
    # the first segment is appended to the neighborhoods list, the second to
    # the latitude, and the last to the longitude
    for line in rodents_file:
        separate = line.split(",")
        if separate[0] != " ":
            neighborhoods.append(separate[0]) 
            latitude.append(float(separate[1])) 
            longitude.append(float(separate[2]))
    rodents_file.close()
    
    # Using the longitude and latitude lists, the rodent reports are plotted and labeled
    # the Northeastern coordinates are used to plot the it on the graph
    plt.scatter(longitude, latitude, marker = "o", color = "khaki", label = "rodent reports")
    plt.plot(NU_longitude, NU_latitude, marker = "*", color = "red", label = "Northeastern")
    plt.legend()
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("Map of Rodent Reports in 2021")
    plt.savefig("boston_rodents.pdf", bbox_inches="tight")
    plt.show()
    
    #In order to create the bar graph, two new lists are called
    unique_neighborhoods = []
    reports_per_neighborhood = []
    
    # the for loop appends neighborhoods from the original list to the unique list
    # if it already doesn' exist in the new list. The new list is sorted alphabetically.
    for neighborhood in neighborhoods:
        if neighborhood not in unique_neighborhoods:
            unique_neighborhoods.append(neighborhood)
        unique_neighborhoods.sort()
       
    # in this  loop, for every neighborhood in the new list, the number of
    # of times it appears in the original list is counted and appended to the
    # respective list     
    for neighborhood in unique_neighborhoods:
        x = neighborhoods.count(neighborhood)
        reports_per_neighborhood.append(x)
            
    # total rodent reports are printed by counting the length of the origninal
    # neighborhoods list
    print("Total rodent reports assigned to a valid neighborhood:", len(neighborhoods))
    
    # this loop prints the unique neighborhood on separate lines
    print ("Neighborhoods:")
    for neighborhood in unique_neighborhoods:
        print(neighborhood)
        
    # average number of rodent reports is printed by dividing number of all rodent reports
    # by the number of neighborhoods
    print("Average number of rodent reports:", len(neighborhoods) / len(unique_neighborhoods))
    
    # bar chart is created using the unique_neighborhoods list and reports_per_neighborhood
    plt.bar(unique_neighborhoods, reports_per_neighborhood, color = ["teal", "indigo"])
    plt.xticks(rotation = 90)
    plt.xlabel("Neighborhoods")
    plt.ylabel("Rodet Report Count")
    plt.title("Rodent Report Comparison for Neighborhoods")
    plt.savefig("neighborhoods.pdf", bbox_inches="tight")
    plt.show()
    
main()


                
              