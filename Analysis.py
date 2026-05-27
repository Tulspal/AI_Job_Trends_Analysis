# 1. Setup & Load Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# load the data
df = pd.read_csv('ai_job_trends_dataset.csv')
print("Dataset loaded Sucessfully")

# Data Profiling & Inspection
print("Data shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())
# First Look at the data
print(df.head())
# data types per column
print(df.dtypes)
# Unique values
print(df.nunique())

# Calculate average salary
avg_salary = df['Median Salary (USD)'].mean()

print(f"Average Salary: ${avg_salary:,.2f}")

# What's the salary by industry?
salary_by_industry = df.groupby('Industry')['Median Salary (USD)'].mean()
print(salary_by_industry)

# Which industry pays most?
highest = salary_by_industry.idxmax()
print(f"Highest paying: {highest}")

# Calculate industry statistics
industry_analysis = df.groupby('Industry').agg({
    'Automation Risk (%)': 'mean',
    'Median Salary (USD)': 'mean'
}).round(2)
industry_analysis.columns = ['Automation_Risk', 'Average_Salary']

print("\nINDUSTRY ANALYSIS")
print(industry_analysis)

# Most affected by automation risk
most_affected = industry_analysis['Automation_Risk'].idxmax()
most_affected_pct = industry_analysis.loc[most_affected, 'Automation_Risk']

# Highest paying industry
highest_paying = industry_analysis['Average_Salary'].idxmax()
highest_paying_amt = industry_analysis.loc[highest_paying, 'Average_Salary']

print(f"\nMOST AFFECTED: {most_affected} ({most_affected_pct:.1f}% automation risk)")
print(f"HIGHEST PAYING: {highest_paying} (${highest_paying_amt:,.0f})")

# Chart 1: Automation Risk
plt.figure(figsize=(10, 5))
industry_analysis['Automation_Risk'].sort_values(ascending=False).plot(kind='barh', color='Orange')
plt.title('Automation Risk by Industry')
plt.xlabel('Automation Risk (%)')
plt.savefig('chart1_automation_risk.png')
plt.show()

# Chart 2: Salary
plt.figure(figsize=(10, 5))
industry_analysis['Average_Salary'].sort_values(ascending=False).plot(kind='barh', color='green')
plt.title('Average Salary by Industry')
plt.xlabel('Salary (USD)')
plt.savefig('chart2_salary.png')
plt.show()

print("\nAnalysis Complete!")




