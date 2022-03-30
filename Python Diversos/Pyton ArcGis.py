#import modules
import os

#user inputs
baseFolder = "C:\\Temp\\"
projectName = "RiverProject"

#define folder paths
asciiFolder = baseFolder + "\\" + projectName + "\\"+ "ascii_output"
rasterFolder = baseFolder + "\\" + projectName + "\\"+ "raster_output"
graphFolder = baseFolder + "\\" + projectName + "\\"+ "graph_output"
tableFolder = baseFolder + "\\" + projectName + "\\"+ "table_output"

#create list of folder paths
folders = [asciiFolder, rasterFolder, graphFolder, tableFolder]

#check if project folder exists
if not os.path.exists(baseFolder + projectName):
    #Create folder if it does not exist
    for folder in folders:
        os.makedirs(folder)
        print("Created: " + folder)
else:
    #if project folder exists, print error message
    print (projectName + " exists. Please provide a new project name.")