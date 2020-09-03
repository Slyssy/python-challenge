import os
import csv
 

path = os.path.join("Resources","election_data.csv")

with open(path, "r") as file:
    
    csv_reader = csv.DictReader(file)
    
    data = list(csv_reader)
    
    lines = len(list(data))
    
    candidate_name = set()
    
    Correy = 0
    Li = 0
    OTooley = 0
    Khan = 0

    for row in data:
        row = dict (row)
        name = row["Candidate"]
        if name not in candidate_name:
            candidate_name.add(name)
        if name == "Correy":
            Correy = Correy + 1
        if name == "Li":
            Li = Li + 1
        if name == "O'Tooley":
            OTooley = OTooley + 1
        if name == "Khan":
            Khan = Khan + 1 
               
    
print(f"Total Votes: {lines}")      
print(candidate_name)
print("Khan:",round((Khan/lines) * 100 , 3), "% (",Khan,")")
print("Correy:",round((Correy/lines) * 100, 3), "% (",Correy,")")
print("Li:",round((Li/lines) * 100, 3), "% (",Li,")")
print("O'Tooley:",round((OTooley/lines) * 100, 3), "% (",OTooley,")")

if Khan == max(Khan, Correy, Li, OTooley):
    print("Winner: Khan")
elif Correy == max(Khan, Correy, Li, OTooley):
    print("Winner: Correy")
elif Li == max(Khan, Correy, Li, OTooley):
    print("Winner: Li")
elif OTooley == max(Khan, Correy, Li, OTooley):
    print("Winner: O'Tooley")
    
        