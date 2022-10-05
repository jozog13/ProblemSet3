#-------------------------------------------------------------
# ProblemSet3_Part2.py
#
# Description: Code for Problem Set 3 - Part 2 (tasks 4-5)
#
# Author: Jess Ozog (jo158@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#%% Task 4.1

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='transshipment_vessels_20180723.csv', mode='r')

#Read the entire contents into a list object
lineList = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = lineList[0]

#Print the contents of the headerLine
print(headerLineString)

#%% Task 4.2

#Split the headerLineString into a list of header items
headerItems = headerLineString.split(',')

#List the index of the mmsi, shipname, and fleet_name values
mmsi_idx = headerItems.index("mmsi")
name_idx = headerItems.index("shipname")
fleet_idx = headerItems.index("fleet_name")

#Print the values
print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3

#Create an empty dictionary
vesselDict = {}

#Iterate through all lines (except the header) in the data file:
for lineString in lineList[1:]:
   
    #Split the data into values
    lineData = lineString.split(',')

    #Extract the mmsi value from the list using the mmsi_idx value
    mmsi = lineData[mmsi_idx]

    #Extract the fleet value
    fleet = lineData[fleet_idx]

    #Adds info to the vesselDict dictionary, with key as mmsi and value as fleet
    vesselDict[mmsi] = fleet

#%% Task 4.4

# assign value for vessel ID
vesselID = '258799000'

# get associated fleet name from vesselDict
fleetName = vesselDict[vesselID]

print(f'Vessel # {vesselID} flies the flag of {fleetName}')

#%% Task 5

#Create a Python file object, i.e., a link to the file's contents
fileObj = open(file='loitering_events_20180723.csv', mode='r')

#Read the entire contents into a list object
lineList2 = fileObj.readlines()

#Release the link to the file objects (now that we have all its contents)
fileObj.close() #Close the file

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString2 = lineList2[0]

#Print the contents of the headerLine
print(headerLineString2)

#Split the headerLineString2 into a list of header items
headerItems2 = headerLineString2.split(',')

#List the index of the transshipmet_mmsi, starting and ending latitude, and starting longitude
mmsi_idx = headerItems2.index("transshipment_mmsi")
s_lat_idx = headerItems2.index("starting_latitude")
e_lat_idx = headerItems2.index("ending_latitude")
s_long_idx = headerItems2.index("starting_longitude")

# print index values for variables
print(mmsi_idx, s_lat_idx, e_lat_idx, s_long_idx)

#Iterate through all lines (except the header) in the data file:
for lineString in lineList2[1:]:
   
    #Split the data into values
    lineData2 = lineString.split(',')

    #Extract the mmsi, start and end latitudes, and start longitude
    mmsi = lineData2[mmsi_idx]
    s_lat = lineData2[s_lat_idx]
    e_lat = lineData2[e_lat_idx]
    s_long = lineData2[s_long_idx]

    # examine if vessel crosses the equator from S to N (s_lat and e_lat)
    # vessel crosses equator if s_lat is negative and e_lat is positive 
    
    


