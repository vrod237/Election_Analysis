import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file from a path
file_to_save = '/Users/vrod4/dataAustin2020/Analysis/Resources/election_analysis.txt'

# 1. Initialize a total vote counter
total_votes = 0

# Candidate options
candidate_options = []
# Delcare the empty dictionary
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

county_options = []
county_votes = {}
winning_county = ""

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
        # Beging tracking vote count per county
        county_name = row[1]

        # If the county name does not match any existing county
        if county_name not in county_options:
            # Add it to the list of counties
            county_options.append(county_name)
            # Begin tracking that county's vote count
            county_votes[county_name] = 0
        # Add vote to that county's count
        county_votes[county_name] += 1

    # Save the results to out text file
    with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)     

        county_results = (
            f"\nCounty Votes:\n")
        print(county_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(county_results)    

        # Finding percentage of votes per county
        for county in county_votes:
        
            votes = county_votes[county]
        
            vote_percentage = int(votes) / int(total_votes) * 100
            county_results = (
                f"{county}: {vote_percentage:4.2f}% ({votes:,})\n")
            print(county_results)
            #Save the county votes to the text file
            txt_file.write(county_results)

            # Finding county with largest turnout
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes ###
                winning_county = county
      
        winning_county_summary = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
        print(winning_county_summary)
        # Save the county with largest turnout's name to the text file
        txt_file.write(winning_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts
    # Iterate through the candidate list
        for candidate in candidate_votes:
            #Retrieve vote count of a candidate
            votes = candidate_votes[candidate]
            # Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
        
            candidate_results = (f"{candidate}: {vote_percentage:4.2f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)

            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)

        # To do: print out each candidate's name, vote count and percentage of votes
        
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count
            #if (votes > winning_count) and (vote_percentage > winning_percentage):
            if (vote_percentage > winning_percentage):
                # If true then set winning_count = votes and winning_percent =  vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # And set the winning candidate equal to the candidate's name
                winning_candidate = candidate
                # To do: print out each candidate's name, vote count and percentage of votes
      
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)