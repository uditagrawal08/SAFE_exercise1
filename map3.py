import pandas as pd
import matplotlib.pyplot as plt

# Reading data from the CSV file
file_path = 'charts-z-scores-by-country.csv'  # Replace with your file path
data = pd.read_csv(file_path, sep=';')  # Use sep=';' to specify the separator

# Filter data for a specific country (e.g., Israel)
country_to_plot = 'Israel'
israel_data = data[data['country'] == country_to_plot]

# Find the group within Israel with the largest spike (highest z-score)
group_with_largest_spike = israel_data.loc[israel_data['zscore'].idxmax()]['group']

# Plotting z-scores for the group with the largest spike in Israel
plt.figure(figsize=(10, 6))

# Plot z-scores over weeks for the specific group in Israel
group_data_to_plot = israel_data[israel_data['group'] == group_with_largest_spike]
plt.plot(group_data_to_plot['week'], group_data_to_plot['zscore'], marker='o', label=f"{country_to_plot} - {group_with_largest_spike}")

plt.title(f'Z-scores over Weeks for {group_with_largest_spike} in {country_to_plot}')
plt.xlabel('Week')
plt.ylabel('Z-score')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
