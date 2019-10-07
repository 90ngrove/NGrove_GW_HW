# Import Dependencies
import pandas as pd

# Store filepath in a variable
file_one = ("Resources/employees.csv")



# Read our Data file with the pandas library
# Not every CSV requires an encoding, but be aware this can come up
file_one_df = pd.read_csv(file_one, encoding="UTF-8")

# Show just the header

file_one_df["Email"] = file_one_df["first_name"] + file_one_df["last_name"]+"@example.com"
file_one_df.head(5)

# Push the remade DataFrame to a new CSV file
file_one_df.to_csv("employees_email.csv", index=False, header=True)
