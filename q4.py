import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dummy_dataset.csv")

# Create a scatter plot
plt.scatter(df["Age"], df["Income"])
plt.title("Age vs Income")
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()

# Suggested dimension reduction technique
print("Suggested Technique: Principal Component Analysis (PCA)")
