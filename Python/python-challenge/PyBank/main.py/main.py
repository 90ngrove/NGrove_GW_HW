# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""
# Import Dependencies
import pandas as pd

csv_path = "Resources/budget_data.csv"
budget_df = pd.read_csv(csv_path)
budget_df.head()

total_months = budget_df[["Date"]].count()
total_months.head()

net_amount = budget_df[["Profit/Losses"]].sum()
net_amount.head()

average_amount = budget_df[["Profit/Losses"]].mean()
average_amount.head() 


print(greatest_amountnew)greatest_amount = budget_df[["Date","Profit/Losses"]].max()
greatest_amountnew = greatest_amount.rename(columns={"Date": "Date",
                                                "Profit/Losses": "Greatest Increase"})
												
												lowest_amount = budget_df[["Date","Profit/Losses"]].min()
lowest_amountnew = lowest_amount.rename(columns={"Date": "Date",
                                                "Profit/Losses": "Lowest Increase"})
lowest_amountnew

print(f"Total months: {total_months}")
print("____________________________")
print(f"Net Amount: {net_amount}")
print("____________________________")
print(f"Average Amount: {average_amount}")
print("____________________________")
print(f"Lowest_Amount: {lowest_amountnew}")
print("____________________________")
print(f"Greatest_Amount: {greatest_amountnew}")























print(total_months)
print(net_amount)
print(average_amount)
print(lowest_amountnew)
print(greatest_amountnew)