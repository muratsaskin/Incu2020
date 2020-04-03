# data analysis and wrangling
import pandas as pd
import numpy as np

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline


# Read the csv file and store it in dataframe
df_apps = pd.read_csv("../input/google-play-store-apps/googleplaystore.csv")

# We need to drop this sample as it's clearly corrupted.
df_apps = df_apps.drop(10472).reset_index().drop("index", axis=1)

# Print unique values in each column, we use alternative way to print them in a "for" loop
for i in df_apps.columns:
    print ("# of Unique Values in Column", i, "is", df_apps[i].nunique())

