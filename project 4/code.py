import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_excel("retail_sales_dataset.xlsx")

print("="*60)
print("FIRST 5 RECORDS")
print(df.head())

print("\n" + "="*60)
print("DATASET INFO")
print(df.info())

print("\n" + "="*60)
print("STATISTICAL SUMMARY")
print(df.describe())

# =====================================
# DATA CLEANING
# =====================================

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATES")
print(df.duplicated().sum())

# =====================================
# TOTAL REVENUE
# =====================================

print("\nTOTAL REVENUE")
print(df["Revenue"].sum())

# =====================================
# TOP PRODUCTS BY REVENUE
# =====================================

product_revenue = df.groupby(
    "Product"
)["Revenue"].sum().sort_values(
    ascending=False
)

print(product_revenue)

plt.figure(figsize=(10,6))

sns.barplot(
    x=product_revenue.values,
    y=product_revenue.index
)

plt.title("Revenue by Product")
plt.xlabel("Revenue")
plt.ylabel("Product")

plt.show()

# =====================================
# CATEGORY REVENUE
# =====================================

category_revenue = df.groupby(
    "Category"
)["Revenue"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    category_revenue,
    labels=category_revenue.index,
    autopct="%1.1f%%"
)

plt.title("Revenue Share by Category")

plt.show()

# =====================================
# REGION ANALYSIS
# =====================================

region_revenue = df.groupby(
    "Region"
)["Revenue"].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    x=region_revenue.index,
    y=region_revenue.values
)

plt.title("Revenue by Region")

plt.show()

# =====================================
# MONTHLY SALES TREND
# =====================================

df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.month_name()

monthly_sales = df.groupby(
    "Month"
)["Revenue"].sum()

month_order = [
    "January","February","March","April",
    "May","June","July","August",
    "September","October","November","December"
]

monthly_sales = monthly_sales.reindex(month_order)

plt.figure(figsize=(12,6))

sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    marker="o"
)

plt.xticks(rotation=45)

plt.title("Monthly Revenue Trend")

plt.show()

# =====================================
# PRODUCT QUANTITY SOLD
# =====================================

qty = df.groupby(
    "Product"
)["Quantity"].sum()

plt.figure(figsize=(10,6))

sns.barplot(
    x=qty.index,
    y=qty.values
)

plt.title("Total Quantity Sold")

plt.show()

# =====================================
# CORRELATION HEATMAP
# =====================================

plt.figure(figsize=(8,6))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

# =====================================
# INSIGHTS
# =====================================

print("\nKEY BUSINESS INSIGHTS")

print("1. Products generate different revenue levels.")
print("2. Some regions outperform others.")
print("3. Monthly sales vary throughout the year.")
print("4. Revenue strongly depends on quantity and unit price.")
print("5. Product demand differs across categories.")

print("\nPROJECT COMPLETED SUCCESSFULLY")