import pandas as pd
import matplotlib.pyplot as plt

# Reading data from the CSV file
file_path = 'AH_Excess_Deaths_by_Sex__Age__and_Race_and_Hispanic_Origin_20231230 (1).csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Filter data for a specific Age Group (e.g., '0-14 Years') and All Race/Ethnicity Groups
filtered_data = data[(data['AgeGroup'] == '0-14 Years') & (data['RaceEthnicity'] == 'All Race/Ethnicity Groups')]

# Grouping data by MMWRyear and calculating the sum of 'Deaths (unweighted)' for each year
grouped_data = filtered_data.groupby('MMWRyear')['Deaths (unweighted)'].sum().reset_index()

# Plotting the graph
plt.figure(figsize=(8, 6))
plt.bar(grouped_data['MMWRyear'], grouped_data['Deaths (unweighted)'], color='skyblue')

plt.title('Total Unweighted Deaths in 0-14 Age Group across Years')
plt.xlabel('Year')
plt.ylabel('Total Unweighted Deaths')
plt.grid(axis='y')

plt.tight_layout()
plt.show()
