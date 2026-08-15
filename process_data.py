import pandas as pd
import glob

# Find all CSV files in the data folder
csv_files = glob.glob("data/*.csv")

# Read and combine all CSV files into one DataFrame
all_data = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)

# Keep only rows where product is "pink morsel"
pink_morsels = all_data[all_data["product"] == "pink morsel"].copy()

# Clean the price column (remove "$" sign) and convert to float
pink_morsels["price"] = pink_morsels["price"].replace(r"[$]", "", regex=True).astype(float)

# Create the "Sales" column = quantity * price
pink_morsels["Sales"] = pink_morsels["quantity"] * pink_morsels["price"]

# Rename columns to match required output
pink_morsels = pink_morsels.rename(columns={"date": "Date", "region": "Region"})

# Keep only the required columns
output = pink_morsels[["Sales", "Date", "Region"]]

# Save to a new CSV file
output.to_csv("data/formatted_sales_data.csv", index=False)

print("Done! Output saved to data/formatted_sales_data.csv")
print(output.head())