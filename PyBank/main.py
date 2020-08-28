import os
import csv

OUT_PATH = "augmented_budget_data.csv"

path = os.path.join("Resources","budget_data.csv")

with open(path, "r") as file:
    
    csv_reader = csv.DictReader(file)
    
    data = list(csv_reader)
    
    lines = len(list(data))
    
    total = 0
    
    for row in data:
        row = dict (row)
        total = row["Profit/Losses"]
        
print(f"Total Months: {lines}")
print(f"Total: ${total}")
      
    
# with open(OUT_PATH, "w+") as file:
    
#     csv_writer = csv.DictWriter(file, 
#                                 [
#                                     "Date",
#                                     "Profit/Losses"
                                    
#                                 ])
    