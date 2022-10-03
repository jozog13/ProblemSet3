#-------------------------------------------------------------
# ProblemSet3_Partl.py
#
# Description: Code for problem set 3
#
# Author: Jess Ozog (jo158@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------
#%% Task 1
#/*-PS3: Code Block 1--*/

mountain = "Denali"
nickname = 'Mt. McKinley'
elevation = 20322 

#print (mountain + ", formerly known as "" + nickname + ",)
#print ()"is " + elevation + '' above sea level.' )

print(f"{mountain}, formerly\nknown as \"{nickname}\" \nis {elevation} above sea level")

#%% Task 2

data_folder = "W:\859_data\\tri_state"
data_list = ["roads.shp", "road_types.dbf", "naip_imagery.tif"]
data_list = list(data_list)
user_item = "streams.shp"
data_list.append(user_item)

for item in data_list:
    print(f"{data_folder}\\{item}")

#%% Task 3

user_numbers=[]
user_int = int(input("Enter an integer: "))