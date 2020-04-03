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

# Plot using only "df_apps" and limit the boundries
ax1 = df_apps[['Category','Rating']].groupby('Category').mean().sort_values("Rating").plot(kind='bar', figsize=(20,10))
ax1.set_ylim(3.5,5)

