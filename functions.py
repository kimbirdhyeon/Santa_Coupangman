def distance_calculator(x_coords, y_coords):
    total_distance = 0
    for i in range(1, len(x_coords)):
        total_distance += np.sqrt((x_coords[i] - x_coords[i-1])**2 + (y_coords[i] - y_coords[i-1])**2)
        
    return total_distance
