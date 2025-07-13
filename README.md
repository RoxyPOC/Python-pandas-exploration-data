# Python-pandas-exploration-data
The tasks at hand are, for the timeframe 2016-2019:      Discern the most popular item in each zipcode and     Compute the sales percentage per store (in dollars).

# 📊 Liquor Sales Data Analysis (2016–2019)
This project analyzes liquor sales data from Iowa (2016–2019) using Python, pandas, and Plotly. It reveals patterns in popular items sold by ZIP code and visualizes store sales distributions.

## 📁 Dataset

The dataset used is `finance_liquor_sales.csv`, which contains information such as:
- `zip_code`
- `item_number`
- `store_number`
- `sale_dollars`

## 🔧 Tech Stack

- **Python 3.x**
- **pandas** – for data wrangling and aggregation
- **Plotly Express & Graph Objects** – for interactive charts

---

## 🧼 Data Preparation

- Dropped `NaN` values (with `dropna`)
- Removed duplicate records (with `drop_duplicates`)

---

## 📈 Analysis Tasks

### ✅ TO-DO-1: Most Popular Items by ZIP Code

Grouped by `zip_code` and `item_number`, then selected the item with the highest sale count in each ZIP code.

```python
grouped = df.groupby(['zip_code','item_number'], as_index=False)['item_number'].sum()
most_popular = grouped.loc[grouped.groupby('zip_code')['item_number'].idxmax()]

✅ TO-DO-2: Sales Percentage Per Store

    Grouped by store_number

    Summed up sale_dollars

    Calculated each store’s share of total sales

sales_per_store = df.groupby('store_number')['sale_dollars'].sum().reset_index()
sales_per_store['sales_percentage'] = (sales_per_store['sale_dollars'] / total_sales) * 100



🚀 Getting Started

   - Clone the repo or download the script.

    - Make sure you have the required Python libraries:

pip install pandas plotly

Place the finance_liquor_sales.csv file in the same directory.

Run the script:

python liquor_analysis.py
