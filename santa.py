import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from functions import *

# Read data from CSV
data = pd.read_csv('data.csv')
submission = pd.read_csv('sample_submission.csv')

# Draw the routes
data_for_draw = submission
data = data.set_index('point_id')
data_for_draw['x'] = data_for_draw['point_id'].map(data['x'])
data_for_draw['y'] = data_for_draw['point_id'].map(data['y'])

distance = distance_calculator(data_for_draw['x'].values, data_for_draw['y'].values)
print(f"총 거리: {distance}")

plt.plot(data_for_draw['x'], data_for_draw['y'], marker='.', color='c')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()