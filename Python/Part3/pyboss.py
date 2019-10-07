# -*- coding: UTF-8 -*-
"""PyBoss Homework Solution."""
# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""
# Import Dependencies
import pandas as pd
import numpy as np
csv_path = "employee_data.csv"
employee_df = pd.read_csv(csv_path)
employee_df.head()


# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

employee_df['abbrev'] = employee_df['State'].map(us_state_abbrev)
employee_df = pd.DataFrame(employee_df)
del employee_df['State']
employee_df[['Fist Name','Last Name']] = employee_df["Name"].str.split(' ',expand=True)
del employee_df['Name']
employee_df['DOBN'] = pd.to_datetime(employee_df['DOB']).dt.strftime('%m/%d/%Y')
del employee_df['DOB']

employee_df["SSN"] = employee_df["SSN"].apply(lambda s: "*****" + s[5:])


employee_df.to_excel("pyboss.xlsx",index= False)