import numpy as np
import matplotlib.pyplot as plt
x = np.random.normal(0, 1, 1000)
y = np.random.normal(0, 1, 1000)
plt.scatter(x, y, alpha=0.5)
plt.title("Scatter Plot of Normal Distribution")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()
