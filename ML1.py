import pandas as pd
import json

def Menu():
    
        print("for CSV file enter 1")
        print("for JSON file enter 2")
        print("for TXT file enter 3")
        print("for XLS file enter 4")

        return( int(input("Enter a number according to th provided menu: ")))
    
def LoadFiles():
        file = Menu()
        path = input("Enter the path of file you want to upload: ")

        if file == 1:
                DataFrame = pd.read_csv(path)
    
        elif file == 2:
                with open(path, 'r') as JasonFile:
                        DataFrame = json.load(JasonFile)

        elif file == 3:
                DataFrame = pd.read_csv(path)
                
        elif file == 4:
                DataFrame = pd.read_excel(path)
            
        else:
                print("Invalid Input")

        return DataFrame

Data = LoadFiles()
print(Data)