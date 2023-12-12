#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 05:17:31 2023

@author: arnobchowdhury

GOAL: 
    
    (1) analyze a total of 5 features – 4 listed below
and an additional one of your interests – and 
    
    (2) present the results of your
analysis and the plots for these 5 features.
"""



# %% Library imports
import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("task2_data.csv")
df.head()

# %%

# Feature 1: #entities
# Continous


# Count the number of relevant and non-relevant entities
relevant_counts = df[df['relevanceJudge'] == 1]['#entities'].count()
non_relevant_counts = df[df['relevanceJudge'] == 0]['#entities'].count()

# Plotting a bar plot
plt.bar(['Relevant', 'Non-Relevant'], [relevant_counts, non_relevant_counts], color=['blue', 'orange'])

# Set plot labels and title
plt.title("#Entities Distribution by Relevance")
plt.xlabel("Relevance")
plt.ylabel("Count")

# Show the plot
plt.show()


df["#entities"].plot(kind="hist")
plt.title("#Entities Distribution")
plt.xlabel("#Entities")
plt.ylabel("Frequency")
plt.show()



# %%
nr_entities_relevant = df[df['relevanceJudge']==1]['#entities']
nr_entities_non_relevant = df[df['relevanceJudge']==0]['#entities']
print("relevant: ", nr_entities_relevant.describe())
print("Non relevant: ", nr_entities_non_relevant.describe())

# %% Finding out stats
nr_entities_relevant = df[df['relevanceJudge']==1]['#entities']
nr_entities_non_relevant = df[df['relevanceJudge']==0]['#entities']
print("relevant: ", nr_entities_relevant.describe())
print("Non relevant: ", nr_entities_non_relevant.describe())

#%% Analysis

import numpy as np
from scipy.stats import mannwhitneyu
u, p_value = mannwhitneyu(
nr_entities_non_relevant, nr_entities_relevant
)

print(u, p_value)

# P value is very less than 0.05, hence reject the
# null hypothesis

# %%
# Feature 2: #entityTypes
# Count the number of relevant and non-relevant entities
relevant_counts = df[df['relevanceJudge'] == 1]['#entityTypes'].count()
non_relevant_counts = df[df['relevanceJudge'] == 0]['#entityTypes'].count()

# Plotting a bar plot
plt.bar(['Relevant', 'Non-Relevant'], [relevant_counts, non_relevant_counts], color=['blue', 'orange'])

# Set plot labels and title
plt.title("#entityTypes Distribution by Relevance")
plt.xlabel("Relevance")
plt.ylabel("Count")

# Show the plot
plt.show()

'''
plt.figure()
df["#entityTypes"].plot(kind="hist")
plt.title("#Entity Types Distribution")
plt.xlabel("#Entity Types")
plt.ylabel("Frequency")
plt.show()
'''


# %% Finding out stats
nr_entities_relevant = df[df['relevanceJudge']==1]['#entityTypes']
nr_entities_non_relevant = df[df['relevanceJudge']==0]['#entityTypes']
print("relevant: ", nr_entities_relevant.describe())
print("Non relevant: ", nr_entities_non_relevant.describe())


#%% Analysis

import numpy as np
from scipy.stats import mannwhitneyu
u, p_value = mannwhitneyu(
nr_entities_non_relevant, nr_entities_relevant
)

print(u, p_value)

# %%

# Feature 3: #tweetsPosted
relevant_counts = df[df['relevanceJudge'] == 1]['#tweetsPosted'].count()
non_relevant_counts = df[df['relevanceJudge'] == 0]['#tweetsPosted'].count()

print(df[df['relevanceJudge']==1])

# Plotting a bar plot
plt.bar(['Relevant', 'Non-Relevant'], [relevant_counts, non_relevant_counts], color=['blue', 'orange'])

# Set plot labels and title
plt.title("#tweetsPosted Distribution by Relevance")
plt.ylabel("Count")

# Show the plot
plt.show()
'''
plt.figure()
df["#tweetsPosted"].plot(kind="hist")
plt.title("#Tweets Posted Distribution")
plt.xlabel("#Tweets Posted")
plt.ylabel("Frequency")
plt.show()
'''

# %% Finding out stats
nr_entities_relevant = df[df['relevanceJudge']==1]['#tweetsPosted']
nr_entities_non_relevant = df[df['relevanceJudge']==0]['#tweetsPosted']
print("relevant: ", nr_entities_relevant.describe())
print("Non relevant: ", nr_entities_non_relevant.describe())

# %%
import numpy as np
from scipy.stats import mannwhitneyu
u, p_value = mannwhitneyu(
nr_entities_non_relevant, nr_entities_relevant
)

print(u, p_value)

# %%

# Feature 4: sentiment
plt.figure()
df["sentiment"].plot(kind="hist")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Frequency")
plt.show()

# %% Finding out stats
nr_entities_relevant = df[df['relevanceJudge']==1]['sentiment']
nr_entities_non_relevant = df[df['relevanceJudge']==0]['sentiment']
print("relevant: ", nr_entities_relevant.describe())
print("Non relevant: ", nr_entities_non_relevant.describe())

# %%
import numpy as np
from scipy.stats import mannwhitneyu
u, p_value = mannwhitneyu(
nr_entities_non_relevant, nr_entities_relevant
)

print(u, p_value)
#%%
# Additional Feature: Choose one more feature of interest, for example, #relevanceJudge
plt.figure()
custom_bins = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500,4500, 5500, 6500, 9000, 10000] 
df["nFollowers"].plot(kind="hist", bins=custom_bins)
plt.title("Followers distribution")
plt.xlabel("Followers")
plt.ylabel("Frequency")
plt.show()

# %% Finding out stats
nr_entities_relevant = df[df['relevanceJudge']==1]['nFollowers']
nr_entities_non_relevant = df[df['relevanceJudge']==0]['nFollowers']
print("relevant: ", nr_entities_relevant.describe())
print("Non relevant: ", nr_entities_non_relevant.describe())

#%%
import numpy as np
from scipy.stats import mannwhitneyu
u, p_value = mannwhitneyu(
nr_entities_non_relevant, nr_entities_relevant
)

print(u, p_value)


