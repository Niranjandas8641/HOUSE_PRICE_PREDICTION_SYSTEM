import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("data/housing.csv")


print("\n========== DATASET INFORMATION ==========")

print("\nShape:")
print(data.shape)


print("\nColumns:")
print(data.columns.tolist())


print("\nMissing Values:")
print(data.isnull().sum())


print("\nStatistics:")
print(data.describe())


print("\nAverage House Price:")
print(data["price"].mean())


print("\nMinimum House Price:")
print(data["price"].min())


print("\nMaximum House Price:")
print(data["price"].max())


# Price distribution

plt.figure(figsize=(10, 6))

plt.hist(data["price"], bins=10)

plt.title("House Price Distribution")

plt.xlabel("Price")

plt.ylabel("Number of Houses")

plt.tight_layout()

plt.savefig("price_distribution.png")

plt.show()


# Living area vs price

plt.figure(figsize=(10, 6))

plt.scatter(
    data["sqft_living"],
    data["price"]
)

plt.title("Living Area vs House Price")

plt.xlabel("Living Area (sqft)")

plt.ylabel("Price")

plt.tight_layout()

plt.savefig("living_area_vs_price.png")

plt.show()