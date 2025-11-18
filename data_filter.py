import os
import pandas as pd

DATA_DIR = "./data"
OUTPUT_DIR = "./data"

os.makedirs(OUTPUT_DIR, exist_ok=True)

all_data = []
files = os.listdir(DATA_DIR)
for file in files:
    if file.startswith("daily_sales_data_") and file.endswith(".csv"):
        data = pd.read_csv(os.path.join(DATA_DIR, file))
        all_data.append(data)

# Combine all data into a single DataFrame
combined_data = pd.concat(all_data, ignore_index=True)

# Process the combined data
combined_data['price'] = combined_data['price'].replace('[\$,]', '', regex=True).astype(float)
filtered_data = combined_data[combined_data['product'] == 'pink morsel'].copy()
filtered_data['sales'] = filtered_data['price'] * filtered_data['quantity']
final_data = filtered_data[['sales', 'date', 'region']]

# Save the final combined data to a single file
output_file = os.path.join(OUTPUT_DIR, "combined_daily_sales.csv")
final_data.to_csv(output_file, index=False)