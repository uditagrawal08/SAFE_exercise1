import pandas as pd
import matplotlib.pyplot as plt

# Reading data from the CSV file (replace 'path/to/your/file.csv' with your file path)
file_path = 'charts-excess-mortality (1).csv'
data = pd.read_csv(file_path, sep=';')  # Use sep=';' to specify the separator

# Plotting the graph
plt.figure(figsize=(10, 6))

# Assuming you want to plot each group separately
groups = data['group'].unique()
for group in groups:
    group_data = data[data['group'] == group]
    plt.plot(group_data['week'], group_data['value'], marker='o', label=group)

# Assuming you want to plot all groups in one graph
# plt.plot(data['week'], data['value'], marker='o')

plt.title('Excess death in europe')
plt.xlabel('Week')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
