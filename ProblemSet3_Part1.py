#-------------------------------------------------------------
# ProblemSet3_Partl.py
#
# Description: Code for Problem Set 3 - Part 1 (tasks 1-3)
#
# Author: Jess Ozog (jo158@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#%% Task 1
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

print (mountain + ", formerly\nknown as \"" + nickname + "\"")
print ("is " + str(elevation) + '\' above sea level.' )

# more edited versions
#print(f"{mountain}, formerly\nknown as \"{nickname}\" \nis {elevation} above sea level")
#print(mountain + ", formerly\nknown as \"" + nickname + "\"\nis " + str(elevation) + "\' above sea level.")

#%% Task 2

data_folder = r"U:\859_data\tri_state"
data_list = ["roads.shp", "road_types.dbf", "naip_imagery.tif"]
#data_list = list(data_list)
user_item = "streams.shp"
data_list.append(user_item)

for item in data_list:
    print(f"{data_folder}\\{item}")

#%% Task 3

user_numbers=[]

for i in range(1,4):
    user_int = int(input("Enter an integer: "))
    user_numbers.append(user_int)
    i += i
user_numbers.sort()
print(user_numbers[2])

#%% Task 3 - Challenge 

user_numbers.sort(reverse=True)
print(user_numbers)
