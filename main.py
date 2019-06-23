import itertools
import pandas as pd
from pprint import pprint
commandList = []
stateVariableList = []
#identifier = 0

# Get all the commands
while True:
    command = input("Please enter all the commands, enter -1 to quit\n")
    if command == "-1":
        print("Exiting From Command Collection\n")
        break
    commandList.append(command.strip()) #strip() removes whitespaces from the beginning and end of the input

#Get all the state variables
while True:
    stateVariable = input("Please enter all state variables, enter -1 to quit\n")
    if stateVariable == "-1":
        print("Exiting From State Variable Collection\n")
        break
    stateVariableList.append(stateVariable.strip())

#Get possible values of the state variables
#Create a dictionary with state variables as key and make empty list for values
stateVariableWithValue = dict()
for i in stateVariableList:
    stateVariableWithValue[i] = []

#For every key(state variable), get the possible values and append to the list of values
for i in stateVariableWithValue.keys():
    while True:
        print("Enter the values of ", i, " enter -1 to quit")
        value = input()
        if value == "-1":
            break
        stateVariableWithValue[i].append(value)

#Create the input data with command list and all the value list
inputData = []
inputData.append(commandList)
for i in stateVariableWithValue.keys():
    inputData.append(stateVariableWithValue[i])

#Make the all possible combination of commands and the values of state variables
combinationOfCommandAndSV = list(itertools.product(*inputData))

command = ["command"]
column = command + stateVariableList

df = pd.DataFrame(combinationOfCommandAndSV, columns = column)
df["Hazard? if provided?"] = ""
df["Hazard? if not provided"] = ""

df.to_csv("contextTable.csv", index=False)

print("commandList: ", commandList)
print("stateVariableList: ", stateVariableList)
print("stateVariableWithValue: ",stateVariableWithValue)
print("inputData: ", inputData)
pprint(combinationOfCommandAndSV)
print(df)
