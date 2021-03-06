from os import read
import random
from .Classes.Other.utilFunctions import sets

from .Classes.TrainingData import TrainingData
from .Classes.Other.utilFunctions import getCSVRef
from .Classes.Other.readWrite import readTrainingDataInstance

# Creating Datasets
##################################
def createDataSet(userID, divisionID, featureID, nullPercentage, numOfFiles, startingPoint=0, readPKL=True):
    instanceArray = []
    if numOfFiles <= len(sets[divisionID]):

        if readPKL: # Reading from the pre-recorded pkl object instances
            print(f"\nCreating a data set from {numOfFiles} PKL files...")
            for x in range(startingPoint, (numOfFiles + startingPoint)):
                instanceArray.append(readTrainingDataInstance(x, userID, divisionID))
        else: # Reading from the raw csv files
            print(f"\nCreating a data set from {numOfFiles} CSV files...")
            for x in range(startingPoint, (numOfFiles + startingPoint)):
                instanceArray.append(TrainingData(getCSVRef(x,userID,divisionID), divisionID, featureID, nullPercentage, readPKL))

    return instanceArray

randomNumbers = [] # placed outside the function so that if you run random for both training and testing
                   # you wont use the same csv's for both
def createRandomDataset(userID, divisionID, featureID, nullPercentage, numOfFiles, readPKL=True):
    instanceArray = []    
    if numOfFiles <= len(sets[divisionID]):
        x = 0
        if readPKL:
            print(f"\nCreating a data set from {numOfFiles} PKL files...")
        else: 
            print(f"\nCreating a data set from {numOfFiles} CSV files...")
            
        while x < numOfFiles:
            r = random.randint(0, len(sets[divisionID]) - 1)
            if r not in randomNumbers:
                x = x + 1
                randomNumbers.append(r)

                if readPKL: # Reading from the pre-recorded pkl object instances
                    instanceArray.append(readTrainingDataInstance(r, userID, divisionID))
                else: # Reading from the raw csv file
                    instanceArray.append(TrainingData(getCSVRef(r, userID, divisionID), divisionID, featureID, nullPercentage, readPKL))

    return instanceArray
##################################
            
def mergeInstanceData(instanceArray):
    final_x = []
    final_y = []

    # Filling final_x
    for instance in instanceArray:
        for row in instance.ml_X:
            final_x.append(row)

    # Filling final_y 
    for instance in instanceArray:
        for row in instance.ml_y:
            final_y.append(row)

    print("\nData has been merged!")
    print(f"Total Data Entries: {len(final_x)}")
    return final_x, final_y
