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
            
percent_kahn = round((Khan/lines) * 100 , 3)
percent_correy = round((Correy/lines) * 100, 3)
percent_li = round((Li/lines) * 100, 3)
percent_otooley = round((OTooley/lines) * 100, 3)

# def Winner   
#     if Khan == max(Khan, Correy, Li, OTooley):
#         return("Winner: Khan")
#     elif Correy == max(Khan, Correy, Li, OTooley):
#         return("Winner: Correy")
#     elif Li == max(Khan, Correy, Li, OTooley):
#         return("Winner: Li")
#     elif OTooley == max(Khan, Correy, Li, OTooley):
#         return("Winner: O'Tooley")

print("Election Results")               
print("_____________________________")    
print(f"Total Votes: {lines}")
print("_____________________________")
print(f"Khan: {percent_kahn}% ({Khan})")
print(f"Correy: {percent_correy}% ({Correy})")
print(f"Li: {percent_li}% ({Li})")    
print(f"O'Tooley: {percent_otooley}% ({OTooley})")
print("_____________________________")

if Khan == max(Khan, Correy, Li, OTooley):
    print("Winner: Khan")
elif Correy == max(Khan, Correy, Li, OTooley):
    print("Winner: Correy")
elif Li == max(Khan, Correy, Li, OTooley):
    print("Winner: Li")
elif OTooley == max(Khan, Correy, Li, OTooley):
    print("Winner: O'Tooley")

# if Khan == max(Khan, Correy, Li, OTooley):
#     print("Winner: Khan")
# elif Correy == max(Khan, Correy, Li, OTooley):
#     print("Winner: Correy")
# elif Li == max(Khan, Correy, Li, OTooley):
#     print("Winner: Li")
# elif OTooley == max(Khan, Correy, Li, OTooley):
#     print("Winner: O'Tooley")
    
# with open("./analysis/output.txt", "w+") as file:
#     file.write("Election Results\n")               
#     file.write("______________________________\n")    
#     file.write(f"Total Votes: {lines}\n")
#     file.write("______________________________\n")
#     file.write("Khan:",round((Khan/lines) * 100 , 3),"% (",Khan,")\n")
#     file.write("Correy:",round((Correy/lines) * 100, 3),"% (",Correy,")\n")
#     file.write("Li:",round((Li/lines) * 100, 3),"% (",Li,")\n")
#     file.write("O'Tooley:",round((OTooley/lines) * 100, 3),"% (",OTooley,")\n")
#     file.write("______________________________\n")
