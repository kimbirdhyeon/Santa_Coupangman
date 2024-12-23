import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
data = pd.read_csv('data.csv')
submission = pd.read_csv('sample_submission.csv')

# Filter data for x > 50 and x <= 50
x_fif = data[data['x'] > 50]  # Filter rows where x > 50
x_oth = data[data['x'] <= 50] # Filter rows where x <= 50

print(submission)
# Scatter plot for x > 50
plt.scatter(x_fif['x'], x_fif['y'], color='red', label='x > 50')

# Scatter plot for x <= 50
plt.scatter(x_oth['x'], x_oth['y'], color='blue', label='x <= 50')

# Labeling the axes
plt.xlabel('x')
plt.ylabel('y')

# Add legend to distinguish between the two plots
plt.legend()

# Show the plot
plt.show()

