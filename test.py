import gdspy
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path

# Load the GDS file
gds_path = "MM-wg2.gds"  # Replace with your GDS file path
layout = gdspy.GdsLibrary().read_gds(gds_path)

# Extract the top-level cell
top_cell = layout.top_level()[0]

# Define grid resolution for rasterization
x_min, y_min, x_max, y_max = top_cell.get_bounding_box().flatten()
resolution = 2000  # High resolution for accuracy
x_grid = np.linspace(x_min, x_max, resolution)
y_grid = np.linspace(y_min, y_max, resolution)
grid_x, grid_y = np.meshgrid(x_grid, y_grid)

bitmap = np.zeros_like(grid_x, dtype=np.uint8)
for vertices in top_cell.get_polygons():
    path = Path(vertices)
    points = np.vstack((grid_x.ravel(), grid_y.ravel())).T
    mask = path.contains_points(points).reshape(grid_x.shape)
    bitmap[mask] = 255

# Check bitmap statistics
print("Non-zero bitmap pixels:", np.count_nonzero(bitmap))


# Visualize with imshow
plt.figure(figsize=(10, 8))
plt.imshow(bitmap, extent=[x_min, x_max, y_min,
           y_max], cmap="gray", origin="lower")
plt.colorbar(label="GDS Layout Intensity")
plt.xlabel("X (microns)")
plt.ylabel("Y (microns)")
plt.title("GDS Layout Visualization")
plt.show()
