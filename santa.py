import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV
data = pd.read_csv('data.csv')
submission = pd.read_csv('sample_submission.csv')




#draw the routes
data_for_draw = submission
data = data.set_index('point_id')
data_for_draw['x'] = data_for_draw['point_id'].map(data['x'])
data_for_draw['y'] = data_for_draw['point_id'].map(data['y'])

plt.plot(data_for_draw['x'],data_for_draw['y'], marker = '.',color = 'c')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

