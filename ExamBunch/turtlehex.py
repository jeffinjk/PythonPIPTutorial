import matplotlib.pyplot as plt
import numpy as np
import random

# Create a figure
fig = plt.figure(figsize=(10, 6))

# Create subplots (2 rows, 2 columns, subplot 1)
ax1 = fig.add_subplot(2, 2, 1)
ax1.plot(np.random.randn(50).cumsum())
ax1.set_title("Plot 1")

# Subplot 2
ax2 = fig.add_subplot(2, 2, 2)
ax2.plot(np.random.randn(50).cumsum(), color='orange')
ax2.set_title("Plot 2")

# Subplot 3
ax3 = fig.add_subplot(2, 2, 3)
ax3.plot(np.random.randn(50).cumsum(), color='green')
ax3.set_title("Plot 3")

# Show all plots
plt.tight_layout()
plt.show()
