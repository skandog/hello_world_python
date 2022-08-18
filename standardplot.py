import matplotlib.pyplot as plt
import numpy as np

# Create a list of evenly-spaced numbers over the range
x = np.linspace(0, 45, 500)
plt.plot(x, np.sin(x))  # Plot the sine of each x point
plt.show()  # Display the plot
