# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""
# Import Dependencies
import pandas as pd

csv_path = "Resources/budget_data.csv"
budget_df = pd.read_csv(csv_path)
budget_df.head()

total_months = budget_df[["Date"]].count()
total_months.head()
total_months_df = pd.DataFrame(total_months)

net_amount = budget_df[["Profit/Losses"]].sum()
net_amount.head()
net_amount_df = pd.DataFrame(net_amount)
net_amount_df.head()

average_amount = budget_df[["Profit/Losses"]].mean()
average_amount.head() 
average_amount_df = pd.DataFrame(average_amount)
average_amount_df


greatest_amount = budget_df[["Date","Profit/Losses"]].max()
greatest_amount_df = pd.DataFrame(greatest_amount)
greatest_amount_df

lowest_amount = budget_df[["Date","Profit/Losses"]].min()
lowest_amount_df = pd.DataFrame(lowest_amount)
lowest_amount_df



print(f"Total months: {total_months_df}")
print("____________________________")
print(f"Net Amount: {net_amount_df}")
print("____________________________")
print(f"Average Amount: {average_amount_df}")
print("____________________________")
print(f"Lowest Amount: {lowest_amount_df}")
print("____________________________")
print(f"Greatest Amount: {greatest_amount_df}")