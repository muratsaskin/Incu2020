#Exercise 2: Drop "Android Ver" and "Genres" column

# data analysis and wrangling
import pandas as pd
import numpy as np

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline


# Read the csv file and store it in dataframe
df_apps = pd.read_csv("../input/google-play-store-apps/googleplaystore.csv")

#We need to drop this sample as it's clearly corrupted.
df_apps = df_apps.drop(10472).reset_index().drop("index", axis=1)

#Let's drop "Android Ver" and "Genres" columns
df_apps.drop("Android Ver", axis=1, inplace=True)
df_apps.drop("Genres", axis=1, inplace=True)

# Check all the columns
df_apps.columns

