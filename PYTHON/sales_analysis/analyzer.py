import pandas as pd
import json
import os

# Check if we're in the right place
print("Current directory:", os.getcwd())
print("Directories: ", os.listdir())
# Check if our data file exists
data_path = "PYTHON/sales_analysis/data/sales.csv"
if os.path.exists(data_path):
    print(f"✅ Found {data_path}")
else:
    print(f"❌ Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")


print("")
print("-----------------------------------------------------------------")
print("")

# Read the CSV file
df = pd.read_csv(data_path)
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df["total"] = df["quantity"] * df["price"]
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs("PYTHON/sales_analysis/output", exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json("PYTHON/sales_analysis/output/sales_data.json", orient="records", indent=2)

# 2. Excel format (good for sharing)
df.to_excel("PYTHON/sales_analysis/output/sales_data.xlsx", index=False)

# 3. Updated CSV (with our new total column)
df.to_csv("PYTHON/sales_analysis/output/sales_with_totals.csv", index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx")
print("- output/sales_with_totals.csv")
