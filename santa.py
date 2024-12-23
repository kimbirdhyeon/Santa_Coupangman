import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
data = pd.read_csv('data.csv')
submission = pd.read_csv('sample_submission.csv')



print(submission.iloc[3])

#draw the routes
data_for_draw = submission
data_for_draw['x'] = data_for_draw['point_id'].map(data['x'])
 

data = data.set_index('point_id')
data_for_draw['x'] = data_for_draw['point_id'].map(data['x'])
data_for_draw['y'] = data_for_draw['point_id'].map(data['y'])

plt.plot(data_for_draw['x'],data_for_draw['y'], marker = '.',color = 'c')

# Labeling the axes
plt.xlabel('x')
plt.ylabel('y')

# Add legend to distinguish between the two plots
plt.legend()

# Show the plot
plt.show()

