# Import Dependencies
import pandas as pd

# Store filepath in a variable
file_one = "web_starter.csv"



# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
file_one_df = pd.read_csv(file_one, encoding="UTF-8",names =["ID", "Title", "Website", "Open","Price","Subscriber Count","Number of Reviews","Course Length 2","Levels","Course Length","Start Date"])

# Show just the header
file_one_df.head(5)

file_one_columns_df = file_one_df[["Title", "Price", "Subscriber Count", "Number of Reviews", "Course Length"]]
# Only keep: "isbn", "original_publication_year", "original_title", "authors",
# "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5"
file_one_columns_df.head(10)


file_one_columns_df.loc[:, "Subscriber Count"] = file_one_columns_df["Subscriber Count"].astype("int")
file_one_columns_df.loc[:, "Number of Reviews"] = file_one_columns_df["Number of Reviews"].astype("int")

file_one_columns_df['Perc_Good'] = (file_one_columns_df.loc[ ,'Number of Reviews'] /file_one_columns_df.loc[ ,'Subscriber Count'])*100

file_one_columns_df['Percentage'] = (file_one_columns_df['Number of Reviews']  / file_one_columns_df['Subscriber Count'])*100
# Push the remade DataFrame to a new CSV file
file_one_columns_df.to_csv("new_web_starter.csv", index=False, header=True)