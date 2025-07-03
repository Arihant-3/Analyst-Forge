### Answer

1. Done

2. Done

3. Done 

4. Done

5.  - Holt's model fit better, both in-sample and for forecasting.
    - Make strategies, plan inventory, campaigns, budgeting, etc.

---

- **Is seasonality strong?**  
Seasonality is present but moderate, the upward trends dominates especially in 2023.

- **Which model better captures fluctuations?**  
Holt's model

- **How can forecasts improve staffing or inventory?**  
    1. Order inventory in time
    2. Avoids stocks overstocking
    3. Schedule staffs and hiring new temporary hiring according to expected peak months

---
---

# 📘 Time Series Forecasting Notes 

---

## 🔹 1. What is Time Series?

**Definition:**  
A sequence of observations collected at regular time intervals (e.g., hourly, daily, monthly).

**Key Components:**
- **Trend:** Long-term increase or decrease
- **Seasonality:** Periodic patterns that repeat (e.g., monthly, weekly)
- **Cyclic:** Irregular long-term fluctuations (e.g., economic cycles)
- **Noise:** Random variation (unexplained)

**Used For:**  
Sales forecasting, weather prediction, financial modeling, web traffic analysis, etc.

---

## 🔹 2. Choosing a Forecasting Model

| Data Pattern | Model | Comments |
|--------------|-------|----------|
| No trend, no seasonality | **SMA**, **SES** | Basic smoothing |
| Trend only | **Holt’s Linear Trend** | Captures level + trend |
| Seasonality only | **Seasonal Moving Average**, **Holt-Winters (seasonal)** | Good for recurring cycles |
| Trend + seasonality | **Holt-Winters**, **SARIMA**, **Prophet** | Handles complex patterns |
| Irregular cycles | **ARIMA**, **LSTM** | Use if patterns are hard to capture statistically |

---

## 🔹 3. Core Models Summary

### ✅ Simple Moving Average (SMA)
- **Definition:** Rolling average over `n` past periods
- **Best For:** Smooth data without trend/seasonality
- **Limitation:** Lags in capturing turning points

---

### ✅ Single Exponential Smoothing (SES)
- **Definition:** Weighted average with recent values given more weight
- **Formula:**  
  `S_t = α * Y_t + (1 - α) * S_(t-1)`
- **Best For:** Flat data (no trend or seasonality)

---

### ✅ Holt’s Linear Trend Method
- **Definition:** Extends SES to include a trend component
- **Best For:** Data with linear trend
- **Limitation:** Does not handle seasonality

---

### ✅ Holt-Winters (Triple Exponential Smoothing)
- **Definition:** Adds **seasonality** to Holt’s method
- **Types:**
  - **Additive**: For constant seasonal variation
  - **Multiplicative**: For increasing seasonal variation
- **Best For:** Data with **trend + seasonality**

---

### ✅ ARIMA (AutoRegressive Integrated Moving Average)
- **Definition:** Combines AR (past values), MA (past errors), and differencing
- **Best For:** Non-seasonal, stationary series (use SARIMA for seasonality)
- **Steps:** Ensure stationarity → Identify p, d, q → Fit

---

### ✅ SARIMA (Seasonal ARIMA)
- **Definition:** ARIMA + seasonal terms
- **Best For:** Data with trend and seasonality (monthly, quarterly)

---

### ✅ Prophet (by Meta)
- **Definition:** Additive model with trend + seasonality + holiday effects
- **Advantages:** Handles missing data, outliers, and holiday events
- **Best For:** Business applications, flexible to custom cycles

---

## 🔹 4. Seasonal or Not? How to Decide

- **Visual inspection** (line plot)
- **Decomposition** (`statsmodels.tsa.seasonal_decompose`)
- **Autocorrelation (ACF) plots** — seasonal lags show repeating peaks
- **Fourier transforms / periodograms**

---

## 🔹 5. When to Use Which Model

| Feature | SMA | SES | Holt | Holt-Winters | ARIMA | Prophet |
|--------|-----|-----|------|---------------|-------|---------|
| Trend  | ❌  | ❌  | ✅   | ✅            | ✅    | ✅      |
| Seasonality | ❌  | ❌  | ❌   | ✅            | ✅ (SARIMA) | ✅ |
| Complex holiday effects | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Easy tuning | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ |
| Works on missing data | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

---

### 🔹 5.1 Real-World Scenario Matching

> Choosing the right model depends on the **data frequency**, **seasonality strength**, and **volatility**. Here are some practical cases:

- **📊 Hourly energy demand**  
  - **Seasonality:** Strong daily/weekly  
  - ❌ Holt may fail to capture short-period fluctuations  
  - ✅ Use: **SARIMA**, **Prophet**, or **LSTM**

- **📈 Stock price prediction**  
  - **Pattern:** Nonlinear, non-stationary, noisy  
  - ❌ SMA/SES too simplistic  
  - ✅ Use: **ARIMA**, **GARCH**, or **LSTM/GRU** (deep learning)

- **🛍️ Retail sales during festive spikes (e.g., Diwali, Christmas)**  
  - **Seasonality:** Sharp peaks, yearly  
  - ✅ Use: **Holt-Winters**, **SARIMA**, or **Prophet with holiday effects**

- **📦 E-commerce monthly sales (moderate trend + mild seasonality)**  
  - ✅ Use: **Holt’s**, **Holt-Winters**, or **Prophet**

---

## 🔹 6. Real-Life Use Cases

| Domain | Forecast Target | Model |
|--------|------------------|--------|
| E-commerce | Monthly sales | Holt-Winters, Prophet |
| Electricity | Hourly demand | SARIMA, LSTM |
| Finance | Daily stock prices | ARIMA, LSTM |
| Weather | Temperature, rainfall | Holt, ARIMA |
| Call Center | Daily ticket volume | Holt-Winters, Prophet |

---

## 🔹 7. Forecasting in Business

### 🔧 Operations
- Staff planning
- Inventory management
- Logistics scheduling

### 💰 Finance
- Revenue projections
- Budgeting
- Cash flow planning

### 📢 Marketing
- Campaign timing
- Product launch windows

---

## 🔹 8. Best Practices

- Always **visualize data first**
- Decompose into trend/seasonality/noise
- Use **validation (train/test split)** for model accuracy
- Tune parameters (e.g., smoothing level α, ARIMA p/d/q)
- Monitor performance over time (MAE, MAPE, RMSE)

---

## 🔹 9. Forecast Accuracy Metrics

| Metric | Description |
|--------|-------------|
| **MAE** | Mean Absolute Error |
| **RMSE** | Root Mean Squared Error |
| **MAPE** | Mean Absolute Percentage Error |
| **R² Score** | How well the model explains variance |

---


