"""PyBank Homework Solution."""
# Import Dependencies
import pandas as pd
import numpy as np
csv_path = "Resources/election_data.csv"
poll_df = pd.read_csv(csv_path)
poll_df.head()

poll_df.count()

votercount = poll_df[["Voter ID"]].count()
votercount
votercount_df = pd.DataFrame(votercount)
votercount_df.head()

candidates_df = poll_df.groupby(['Candidate'])
votesbycandidate =candidates_df[["Voter ID"]].count().head(10)
votesbycandidate

votepercentage = poll_df.groupby('Candidate')['Voter ID'].count().reset_index()
votepercentage['Percentage'] = 100 * P['Voter ID']  / P['Voter ID'].sum()
votepercentage

votesbycandidatesorted = votesbycandidate.sort_values("Voter ID")
winner =votesbycandidatesorted.tail(1)
winner
winner_df = pd.DataFrame(winner)
winner_df
