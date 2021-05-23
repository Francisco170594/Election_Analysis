#The data we need to retrieve.
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of the election based on popular vote


#Assign a varaible fot the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#Opening the election results and read the file
with open(file_to_load, encoding='UTF-8') as election_data:

    #To do: perform analysis.
    print(election_data)


#Close the file.
election_data.close()

import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources','election_results.csv')
#Open the election results and read the file
with open(file_to_load,encoding='UTF-8') as election_data:

   # To do: read and analyze the data here.
   
   # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    
    

# Create a filename variable to a direct or indirect path to the file.
file_to_save = 'analysis/election_analysis.txt'
# Using the with statement open the file as text file
with open (file_to_save, 'w') as txt_file:

   # Write some data to the file
    txt_file.write ("Counties in the Election\n\nAraphoe\nDenver\nJefferson")
    
# Close the file
txt_file.close()









