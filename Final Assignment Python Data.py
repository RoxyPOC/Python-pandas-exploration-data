import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

#Importing a CSV file
df = pd.read_csv('finance_liquor_sales.csv')

#Data Preparation: Extract, clean, and prepare the dataset for analysis
df.dropna()
df.drop_duplicates()

#TO-DO-1
# Group by zipcode and item, and sum the counts (if necessary)
grouped = df.groupby(['zip_code','item_number'], as_index=False)['item_number'].sum()

# Find the most popular item in each zipcode
most_popular = grouped.loc[grouped.groupby('zip_code')['item_number'].idxmax()]

print(most_popular)

#TO-DO-2
# Group by store and sum sales
sales_per_store = df.groupby('store_number')['sale_dollars'].sum().reset_index()

# Calculate total sales
total_sales = sales_per_store['sale_dollars'].sum()

#Compute percentage of sales per store
sales_per_store['sales_percentage'] = (sales_per_store['sale_dollars'] / total_sales) * 100

# Sort by percentage (optional, for better readability)
sales_per_store = sales_per_store.sort_values(by='sales_percentage', ascending=False)

print(sales_per_store)

# Bar chart for most popular items by ZIP code
fig = px.bar(
    most_popular,
    x='zip_code',        # Correct column for ZIP codes
    y='item_number',     # Correct column for the metric (items sold)
    title='Most Popular Items by ZIP Code (2016–2019)',
    labels={'item_number': 'Items Sold', 'zip_code': 'ZIP Code'},
)

fig.update_layout(xaxis=dict(type='category'), template='plotly', showlegend=False)
fig.show()


# Pie chart for Sales Percentage Per Store

fig = px.pie(
    sales_per_store,
    names='store_number',
    values='sales_percentage',
    title='Sales Percentage Per Store (2016–2019)',
    labels={'store_number': 'Store Number', 'sales_percentage': 'Sales Percentage'}
)

fig.update_traces(textinfo='percent+label')
fig.show()

