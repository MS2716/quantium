import pandas as pd

data_0 = pd.read_csv('./data/daily_sales_data_0.csv')
data_1 = pd.read_csv('./data/daily_sales_data_1.csv')
data_2 = pd.read_csv('./data/daily_sales_data_2.csv')

data = pd.concat([data_0, data_1, data_2], ignore_index=True)

data['price'] = data['price'].replace('[\$,]', '', regex=True).astype(float)
# Filter data for sales 
filtered_data = data[data['product'] == 'pink morsel'].copy()

# Calculate sales
filtered_data['sales'] = filtered_data['price'] * filtered_data['quantity']

# Save final data
final_data = filtered_data.drop(columns=['price', 'quantity'])
final_data.to_csv('./data/daily_sales_data.csv', index=False)