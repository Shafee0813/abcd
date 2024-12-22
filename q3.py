import pandas as pd

# Import the existing CSV file
csv_path = "dummy_dataset.csv"  # Replace with the actual path of your CSV
df = pd.read_csv(csv_path)

# Rename columns
renamed_df = df.rename(columns={"Age": "Age (Years)", "Income": "Annual Income"})

print("Renamed DataFrame:\n", renamed_df)
