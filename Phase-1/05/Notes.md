### Answer

1. In Z-score and IQR score, the number of outliers are same i.e. 50.

2. Electronics Mechant_type have most of the outliers.  
But in luxury and grocery has also have too many outliers(just 1 less than electronics)
    - Also in luxury(Merchant_type) the number of customer are more who are spending in one specific range. Wheras in electronics and grocery the no. of customers are distributed along outliers.

3. Difference in average spend with/without outliers = 70.075

4. As most of the amount lies between 300 to 700, we have to offer more discounts and points over all the merchant_type. And for outliers we have to increase the supply of electronics to get more customers.

- Removing outliers blindly in fraud detection might cause real high-value transactions to be excluded, harming the business or missing fraud.

---
---

### ✅ 1. Z-score Method

#### 📖 Definition:
Z-score measures how many standard deviations a value is away from the mean.

#### 🧠 Meaning:
A Z-score tells you how unusual a value is in a normally distributed dataset. High absolute Z-scores indicate outliers. Typically, values with |Z| > 3 are considered outliers.

#### 💻 General Syntax:
```python
from scipy.stats import zscore
df['Z'] = zscore(df['Column'])
df['Outlier_Z'] = df['Z'].abs() > 3
```

---

### ✅ 2. IQR (Interquartile Range) Method

#### 📖 Definition:
IQR is the difference between the third quartile (Q3) and the first quartile (Q1), representing the middle 50% of the data.

#### 🧠 Meaning:
This method identifies outliers that fall significantly below or above the central data spread. Values outside the range [Q1 - 1.5 × IQR, Q3 + 1.5 × IQR] are flagged as outliers.

#### 📌 What is a Quantile?
A quantile is a statistical term describing the value below which a given percentage of data falls.

- `Q1` (First Quartile) = 25th percentile → 25% of data falls **below** this value.  
- `Q3` (Third Quartile) = 75th percentile → 75% of data falls **below** this value.

#### 💻 General Syntax:
```python
Q1 = df['Column'].quantile(0.25)  # First quartile (25th percentile)
Q3 = df['Column'].quantile(0.75)  # Third quartile (75th percentile)
IQR = Q3 - Q1
df['Outlier_IQR'] = (df['Column'] < Q1 - 1.5*IQR) | (df['Column'] > Q3 + 1.5*IQR)
```
