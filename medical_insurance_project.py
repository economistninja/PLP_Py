# -*- coding: utf-8 -*-

import pandas as pd

# This command reads the CSV file into a DataFrame
df = pd.read_csv('insurance.csv')

# Use these commands to perform the basic exploration
print(df.head())
print(df.info())
print(df.shape)

# Create a new DataFrame with the encoded categorical columns
df_encoded = pd.get_dummies(df, columns=['sex', 'smoker', 'region'], drop_first=True)

# Display the first few rows of the new, encoded DataFrame
print(df_encoded.head())

# Check the new data types and structure
print(df_encoded.info())

# Task 1: Analyze the impact of smoking on charges
avg_smoker_charges = df_encoded.groupby('smoker_yes')['charges'].mean()
print("Average charges for smokers (1) vs. non-smokers (0):")
print(avg_smoker_charges)
print("\n")

# Task 2: Analyze charges by region
avg_charges_by_region = df.groupby('region')['charges'].mean()
print("Average charges by region:")
print(avg_charges_by_region)
print("\n")

# Task 3: Find the correlation between numerical variables
print("Correlation matrix:")
print(df_encoded[['age', 'bmi', 'children', 'charges']].corr())

import matplotlib.pyplot as plt
import seaborn as sns

# Set a style for the plots
sns.set_style('whitegrid')

# Task 1: Plot the distribution of charges
plt.figure(figsize=(10, 6))
sns.histplot(df['charges'], kde=True, bins=30)
plt.title('Distribution of Charges')
plt.xlabel('Charges')
plt.ylabel('Frequency')
plt.show()

# Task 2: Create a scatter plot of BMI vs. Charges, colored by smoker status
plt.figure(figsize=(10, 6))
sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df)
plt.title('BMI vs. Charges (by Smoker Status)')
plt.xlabel('BMI')
plt.ylabel('Charges')
plt.show()

# Task 3: Create a bar chart of average charges by region
avg_charges_region = df.groupby('region')['charges'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_charges_region.index, y=avg_charges_region.values, palette='viridis')
plt.title('Average Charges by Region')
plt.xlabel('Region')
plt.ylabel('Average Charges')
plt.show()

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# 
# # Set a style for the plots
# sns.set_style('whitegrid')
# 
# # Load the data
# df = pd.read_csv('insurance.csv')
# 
# # --- STREAMLIT APP LAYOUT ---
# 
# st.title("Insurance Charges Analysis 📊")
# st.markdown("A simple data analysis and visualization app using the insurance dataset.")
# 
# # Display a sample of the data
# st.subheader("Raw Data Sample")
# st.dataframe(df.head())
# 
# # --- VISUALIZATIONS ---
# 
# st.subheader("Distribution of Charges")
# fig, ax = plt.subplots()
# sns.histplot(df['charges'], kde=True, bins=30, ax=ax)
# ax.set_title('Distribution of Charges')
# ax.set_xlabel('Charges')
# ax.set_ylabel('Frequency')
# st.pyplot(fig)
# 
# st.subheader("BMI vs. Charges (by Smoker Status)")
# fig, ax = plt.subplots()
# sns.scatterplot(x='bmi', y='charges', hue='smoker', data=df, ax=ax)
# ax.set_title('BMI vs. Charges (by Smoker Status)')
# ax.set_xlabel('BMI')
# ax.set_ylabel('Charges')
# st.pyplot(fig)
# 
# st.subheader("Average Charges by Region")
# avg_charges_region = df.groupby('region')['charges'].mean().sort_values(ascending=False)
# fig, ax = plt.subplots()
# sns.barplot(x=avg_charges_region.index, y=avg_charges_region.values, palette='viridis', ax=ax)
# ax.set_title('Average Charges by Region')
# ax.set_xlabel('Region')
# ax.set_ylabel('Average Charges')
# st.pyplot(fig)

!streamlit run app.py & npx localtunnel --port 8501

# Commented out IPython magic to ensure Python compatibility.
# %pip install streamlit -q

!streamlit run app.py & npx localtunnel --port 8501

!npm install -g localtunnel

!streamlit run app.py & npx localtunnel --port 8501 --public

!npx localtunnel --port 8501
