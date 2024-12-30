import matplotlib.pyplot as plt
import numpy as np

# Create an array of x values from 0 to 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Calculate the corresponding y values as the sine of x
y = np.sin(x)

# Create a plot
plt.plot(x, y, label="Sine Wave", color='b')  # 'b' stands for blue color

# Add a title and labels
plt.title("Sine Wave")
plt.xlabel("X values (radians)")
plt.ylabel("Y values (sin(x))")

# Show a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
