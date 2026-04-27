# 📊 Marketing Funnel & Conversion Analysis

## 🔍 Project Overview

This project focuses on analyzing user behavior in an e-commerce dataset to understand how users move through the funnel:

View → Cart → Purchase

The goal is to identify:

* Where users drop off
* How conversion behaves across stages
* Which product categories perform better

## 🎯 Objectives

* Analyze user journey across funnel stages
* Calculate conversion rates
* Identify drop-off points
* Find top-performing product categories
* Present insights using a dashboard

## 📁 Dataset

* E-commerce user interaction dataset
* Link : https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store
* Size: ~1.6 GB (sampled for analysis)
* Key columns used:

  * event_type (view, cart, purchase)
  * user_id
  * product_id
  * category_code
  * price
  * user_session

## 🛠️ Tools Used

* Python (Pandas) → Data cleaning & analysis
* Power BI → Dashboard & visualization

## ⚙️ Data Processing Steps

### 1. Data Loading

* Loaded only required columns
* Used a subset of data (300,000 rows) for efficiency

### 2. Handling Missing Values

* Created two datasets:

  * df_main → for funnel analysis
  * df_category → for category analysis (removed missing category values)

### 3. Funnel Creation

* Identified unique users for each stage:

  * View
  * Cart
  * Purchase

* Ensured proper flow:

  * Cart users ⊆ View users
  * Purchase users ⊆ Cart users

### 4. Metrics Calculated

* Total Views
* Total Carts
* Total Purchases
* Conversion Rate

Conversion Rate = Purchases / Views

### 5. Drop-off Analysis

* View → Cart drop
* Cart → Purchase drop

### 6. Category Analysis

* Grouped data by category_code
* Calculated:

  * Unique viewers
  * Unique purchasers
  * Conversion rate per category

## 📤 Generated Datasets (Used in Dashboard)

The following datasets were created and exported from Python for visualization in Power BI:

* funnel.csv
  Contains funnel stages (View, Cart, Purchase) and corresponding user counts

* dropoff.csv
  Contains number of users dropping off between stages

* category_analysis.csv
  Contains category-wise:

  * views
  * purchases
  * conversion rates

These datasets form the base for all dashboard visuals.

## Dashboard Preview 👁️
![Dashboard](Task3_Dashboard.png)

## 📊 Dashboard Overview

### 🔹 KPI Cards

* Total Views
* Total Carts
* Total Purchases
* Conversion Rate

### 🔹 Funnel Chart

* Visual representation of:
  View → Cart → Purchase

### 🔹 Drop-off Chart

* Shows where users are leaving the funnel

### 🔹 Category Analysis

* Top converting product categories
* Sorted by conversion rate

### 🔹 Filters

* Category-based filtering for dynamic analysis

## 📈 Key Insights

* Significant drop observed from View → Cart stage
* Strong conversion from Cart → Purchase stage
* Certain product categories show higher purchase intent
* Indicates opportunity to improve early-stage engagement

## 🚀 Conclusion

This analysis demonstrates how user behavior data can be used to:

* Identify bottlenecks in conversion
* Improve product and marketing strategies
* Support data-driven decision making

## 📌 Future Improvements

* Use full dataset (not sample)
* Improve category-level accuracy
* Add time-based funnel trends
* Include session-level analysis


