import os
import csv

path = os.path.join("Resources","budget_data.csv")

with open(path, "r") as file:
    
    csv_reader = csv.DictReader(file)
    
    data = list(csv_reader)
    
    lines = len(list(data))
    
    total = 0
    
    profit_loss = 0
    
    sum_change = 0
    
    max_profit = 0
    
    max_loss = 0 
    
#     print(type(data))
#     print(type(lines))
#     print(type(total))
    
    for row in data:
        row = dict (row)
        profit_loss_previous = profit_loss
        profit_loss = int(row["Profit/Losses"])
        date = row["Date"]
        change = profit_loss - profit_loss_previous
        if profit_loss_previous != 0:
            sum_change = sum_change + change
        
        if change > max_profit:
            max_profit = change
            max_profit_date = date
            
        if change < max_loss:
            max_loss = change
            max_loss_date = date
        
    avg_change = sum_change/(lines - 1)
    

with open("./analysis/output.txt", "w+") as file:
    file.write("Financial Analysis\n")
    file.write("______________________________\n")
    file.write(f"Total Months: {lines}\n")
    file.write(f"Total: ${sum_change}\n")
    file.write(f"Average Change: ${round(avg_change,2)}\n")
    file.write(f"Greatest Increase in Profits: {max_profit_date} (${max_profit})\n")
    file.write(f"Greatest Decrease in Profits: {max_loss_date} (${max_loss})")

                              
print("Financial Analysis")
print("______________________________")
print(f"Total Months: {lines}")
print(f"Total: ${sum_change}")
print("Average Change: $", round(avg_change,2))
print(f"Greatest Increase in Profits: {max_profit_date} (${max_profit})")
print(f"Greatest Decrease in Profits: {max_loss_date} (${max_loss})")


       

        
    