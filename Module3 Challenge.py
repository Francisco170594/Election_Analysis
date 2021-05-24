 #-*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = 'Resources/election_results.csv'

# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0


# Candidate Options and candidate votes.


# 1: Create a county list and county votes dictionary.
counties = []
counties_votes ={}



# Track the winning candidate, vote count and percentage


# 1a.Track winning turnout, county and percentage

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_turnout = 0
largest_percentage = 0




# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1
        

        # Get the candidate name from each row.
        

        # 3: Extract the county name from each row.
        county_name = row [1]
        


        # If the candidate does not match any existing candidate add it to
        # the candidate list
                
        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in counties:
        

            # 4b: Add the existing county to the list of counties.
            counties.append(county_name)


            # 4c: Begin tracking the county's vote count.
            counties_votes[county_name] = 0


        # 5: Add a vote to that county's vote count.
        counties_votes[county_name] += 1



# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in counties_votes:

        # 6b: Retrieve the county vote count.
        turnout = counties_votes.get(county_name)

        # 6c: Calculate the percentage of votes for the county.
        turnout_percentage = float(turnout) / float(total_votes) * 100
        county_result = (
            f"{county_name}: {turnout_percentage:.1f}% ({turnout})\n")
        

         # 6d: Print the county results to the terminal.
        print(county_result)


         # 6e: Save the county votes to a text file.
        


         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (turnout > largest_turnout) and (turnout_percentage > largest_percentage):
             largest_turnout = turnout
             largest_county = county_name
             largest_percentage = turnout_percentage




    # 7: Print the county with the largest turnout to the terminal.
    turnout_summary = (
        f"Largest County Turnout: {largest_county}")       




    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(turnout_summary)


    # Save the final candidate vote count to the text file.
    
