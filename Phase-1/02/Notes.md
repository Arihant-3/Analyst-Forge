## Answers 

1. Across all years we see a significant changes in october to november month.

2. Yeah, April, july and October, november have unusually low and high sales compared to monthly average respectively.

3. In April and July, sales goes down significantly maybe cause of summer peaks or off season. Whereas in October and November the sales goes all day high.

- So we should focus on the products which is typically good in off season like more of a cold things, and focus on different sectors and thinking of ways to elevate more sales apart from dip month . And rest is going good.

---

### 🧠 Expected Key Insights:

* Spikes in Nov–Dec hint at festive seasons (Diwali, Christmas, New Year).

* Sharp dips in April & July likely correlate with off-season or post-festive drop-off.

* Business Strategy Insight: Increase inventory in Q4 (Oct–Dec), reduce marketing spend during Q2 (Apr–Jul) unless running promos.

---
---

# Cheat Sheet for this Question ---

## 🧾 Power BI & Python: Sales Trend & Anomaly Analysis Cheat Sheet

This cheat sheet summarizes my work with Python (via Jupyter Notebook) and Power BI to analyze sales trends, compute rolling averages, and detect anomalies using `retail_sales.csv`.

---

### 📦 Dataset Creation (Python)
- I simulated daily sales data from 2019 to 2021.
- Added anomalies by injecting artificial spikes in Nov–Dec and dips in Apr–Jul.
- Final DataFrame: `Date`, `Sales`

---

### 📊 Python Analysis Highlights

- **Monthly Aggregates**: Grouped data by `Month` to smooth daily noise.
- **Rolling Average**: Used 30-day rolling average to highlight long-term trends.
- **Visualization**: Created clear trend charts using `matplotlib` with grid and rotation for better x-axis legibility.

---

## 🔍 Power BI Analysis Guide

### ✔️ Load Data
- Imported the CSV from Python simulation.

### ✔️ Data Model Enhancements
- Created `MonthStart` (first day of each month) for smoother X-axis.
- Extracted `Year` to use in slicers.

### ✔️ Visual Setup
- Used **Line Chart** with:
  - **X-axis**: `MonthStart` (as continuous)
  - **Y-axis**: Sum or Avg of `Sales`
- Added a **Year Slicer** for filtering.

### ✔️ Rolling Average in Power BI
- Created a 3-month rolling average using DAX.
- Helped reduce seasonal noise and reveal overall trend.
📌 However, using a measure instead of a column gives more flexibility with slicers and filtering — useful if you want fully dynamic behavior.

### ✔️ Manual Anomaly Detection
- Calculated anomalies based on 2 standard deviations from the mean.
- Flagged "Anomaly" vs "Normal" using conditional formatting or markers.
Though it didn't go as I imagined.

---

## 📌 Key Concepts

- **Rolling Average**: Smooths short-term fluctuations to show longer-term trends.
- **Monthly Aggregates**: Converts daily data to monthly, reducing clutter and highlighting patterns.
- **Anomaly**: A data point that is noticeably different from the usual pattern — either too high or too low compared to the rest.

---

## ⚠️ Tips & Notes

- Power BI's **Anomaly Detection** only works with:
  - **Line Charts**
  - **Continuous Date** axis
- If anomalies are not showing:
  - Ensure your Date is typed correctly
  - Avoid using text-based time groupings (e.g., "Q1", "Jan")

