# ai_job_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -------- Step 1: Load dataset --------
excel_file = 'ai_job_impact_dataset_100rows.xlsx'

if os.path.exists('ai_job_impact_dataset.pkl'):
    # Load from pickle if available (faster)
    df = pd.read_pickle('ai_job_impact_dataset.pkl')
    print("Loaded dataset from pickle file.")
else:
    # Load from Excel
    df = pd.read_excel(excel_file)
    print("Loaded dataset from Excel file.")
    # Save as pickle for next time
    df.to_pickle('ai_job_impact_dataset.pkl')
    print("Saved dataset as pickle for future use.")

# -------- Step 2: Basic Analysis --------
print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Top 5 Jobs by AI Impact ---")
top_impact = df.sort_values(by='AI Impact Score (0-1)', ascending=False).head(5)
print(top_impact)

print("\n--- Jobs Count per Sector ---")
print(df['Job Sector'].value_counts())

# -------- Step 3: Visualization --------
# 1. Distribution of AI Impact Scores
plt.figure(figsize=(10,6))
sns.histplot(df['AI Impact Score (0-1)'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of AI Impact Scores')
plt.xlabel('AI Impact Score')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('ai_impact_distribution.png')  # save plot
plt.show()

# 2. AI Impact Score by Job Sector
plt.figure(figsize=(12,6))
sns.boxplot(x='Job Sector', y='AI Impact Score (0-1)', data=df)
plt.xticks(rotation=45)
plt.title('AI Impact Score by Job Sector')
plt.tight_layout()
plt.savefig('ai_impact_by_sector.png')
plt.show()

# -------- Step 4: Save analysis results --------
top10 = df.sort_values(by='AI Impact Score (0-1)', ascending=False).head(10)
top10.to_excel('top10_ai_impact_jobs.xlsx', index=False)
print("\nTop 10 AI impact jobs saved as 'top10_ai_impact_jobs.xlsx'")