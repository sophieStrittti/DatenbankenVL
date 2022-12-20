import csv
import pandas as pd
 
# tsv_file = "C:/Users/sosos/OneDrive/Documents/DHBW/Semester 5/Datenbanken/dataset_ imdbws/name_basics.tsv"
# csv_table = pd.read_table(tsv_file,sep='\t')
# csv_table.to_csv('C:/Users/sosos/OneDrive/Documents/DHBW/Semester 5/Datenbanken/dataset_ imdbws/name_basics.csv',index=False)

new_data = []
with open("C:/Users/sosos/OneDrive/Documents/DHBW/Semester 5/Datenbanken/dataset_ imdbws/title_principals.tsv", errors='replace') as file:
    tsv_file = csv.reader(file, delimiter="\t")     
    
    for line in tsv_file:   
        print(line)
        if '\\N' not in line:
            
            new_data.append(line)
            
print(new_data[1])
with open("C:/Users/sosos/OneDrive/Documents/DHBW/Semester 5/Datenbanken/dataset_ imdbws/name_basics.csv", 'r+', errors='replace') as file:
    for line in new_data:
        writer = csv.writer(file)
        writer.writerow(line)
        print("written")    
        
            
            
        