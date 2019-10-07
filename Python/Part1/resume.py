# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import string

# Counter is used later in the program
from collections import Counter

# Paths
resume_path = ("Resources/resume.md")

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r") as resume_file_handler:
        return resume_file_handler.read().lower().split()

# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()

# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation
print(resume)


# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
print("Intersection :", resume & REQUIRED_SKILLS)
print(REQUIRED_SKILLS)


# Calculate the Desired Skills Match using Set Intersection
print("DESIRED SKILLS")
print("Intersection :", resume & DESIRED_SKILLS)
print(DESIRED_SKILLS)


# Using collections.Counter
word_counter = Counter(word_list)
print(word_counter)

top_ten =first2pairs = {k: word_counter[k] for k in list(word_counter)[:2]}
print(top_ten)

