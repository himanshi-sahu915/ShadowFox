import matplotlib.pyplot as plt
import seaborn as sns

# Example data
data = [10, 20, 15, 30, 25]

# Plot using Matplotlib
plt.plot(data)
plt.title("Matplotlib Example")
plt.show()

# Plot using Seaborn
sns.set(style="darkgrid")
sns.histplot(data, kde=True)
plt.title("Seaborn Example")
plt.show()
