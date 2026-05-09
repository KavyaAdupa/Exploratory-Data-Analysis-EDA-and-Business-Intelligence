pandas
numpy# ==========================================
# EXPLORATORY DATA ANALYSIS (EDA)
# & BUSINESS INTELLIGENCE PROJECT
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# STEP 1: LOAD DATASET
# ==========================================

# Read CSV File
data = pd.read_csv("sales_data.csv")

# Display Dataset
print("Original Dataset:\n")
print(data)

# ==========================================
# STEP 2: DATA IMMERSION
# ==========================================

print("\nFirst 5 Rows:\n")
print(data.head())

print("\nDataset Information:\n")
print(data.info())

print("\nStatistical Summary:\n")
print(data.describe())

print("\nMissing Values:\n")
print(data.isnull().sum())

# ==========================================
# STEP 3: DATA CLEANING
# ==========================================

# Remove duplicate rows
data = data.drop_duplicates()

# Fill missing values with mean
data['Sales'] = data['Sales'].fillna(data['Sales'].mean())

print("\nCleaned Dataset:\n")
print(data)

# ==========================================
# STEP 4: EXPLORATORY DATA ANALYSIS
# ==========================================

# Total Sales
total_sales = data['Sales'].sum()
print("\nTotal Sales =", total_sales)

# Average Sales
average_sales = data['Sales'].mean()
print("Average Sales =", average_sales)

# Maximum Sales
max_sales = data['Sales'].max()
print("Maximum Sales =", max_sales)

# Minimum Sales
min_sales = data['Sales'].min()
print("Minimum Sales =", min_sales)

# ==========================================
# STEP 5: BUSINESS INTELLIGENCE
# ==========================================

# Sales by Product
product_sales = data.groupby('Product')['Sales'].sum()

print("\nSales by Product:\n")
print(product_sales)

# Best Selling Product
best_product = product_sales.idxmax()
print("\nBest Selling Product =", best_product)

# ==========================================
# STEP 6: DATA VISUALIZATION
# ==========================================

# Bar Chart
product_sales.plot(kind='bar')

plt.title("Sales by Product")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.show()

# ==========================================
# STEP 7: FINAL INSIGHTS
# ==========================================

print("\n----- BUSINESS INSIGHTS -----")

print("1. Total Revenue Generated =", total_sales)

print("2. Best Selling Product =", best_product)

print("3. Average Sales Value =", average_sales)

print("4. Highest Sales Recorded =", max_sales)

print("5. Lowest Sales Recorded =", min_sales)

print("\nEDA and Business Intelligence Completed Successfully!")