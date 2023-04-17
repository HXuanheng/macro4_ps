import itertools
import numpy as np

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[9, 10], [11, 12]]

matrices = [A, B, C]

for rows in itertools.product(*matrices):
    print(rows)
    for prod in itertools.product(*rows):
        print(prod)
        print(np.prod(prod))




%matplotlib inline

def f(x, y):
    return np.exp(x) * np.exp(y)

# Define the grid
num_points = 100
x_min, x_max = 0, 1
y_min, y_max = -1, 0
x_grid, y_grid = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

# Evaluate the function on the grid
z_grid = f(x_grid, y_grid)

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_grid, y_grid, z_grid)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
plt.show()
plt.close()


