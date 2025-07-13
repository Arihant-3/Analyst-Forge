## 📌 Difference Between `dt.year` vs `str.split('-').str[0]`

```
| Feature          | `df['Date'].dt.year`                    | `df['Date'].str.split('-').str[0]`          |
|------------------|-----------------------------------------|---------------------------------------------|
| Input Type       | `datetime64[ns]`                        | `str` or `object`                           |
| Output Type      | `int`                                   | `str`                                       |
| Speed & Safety   | Fast, format-safe                       | Slower, format-dependent                    |
| Use Case         | Accurate date-based operations          | Quick fix if string is well-formatted       |
| Best Practice    | ✅ Use this after `pd.to_datetime()`    | ⚠️ Use only if format is guaranteed        |
```

👉 **Tip**: Always prefer `.dt.year` for reliability and performance.

----
----
----

## Basic Formulas for NULL
```
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)
```

----
----
----

## Tokenize and clean the text
```
import pandas as pd
import string

# Load the dataset
df = pd.read_csv("dataset.csv")

# Function to clean and tokenize
def clean_and_tokenize(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")
    # Tokenize by splitting on whitespace
    tokens = text.split()
    return tokens

# Apply the function to the 'Text' column
df['Tokens'] = df['Text'].apply(clean_and_tokenize)

# Display sample
print(df.head())
```

----
----
----

## 📊 Evaluation Metrics – Full Coverage

### 📖 What Are Evaluation Metrics?

**Evaluation metrics** are quantitative tools to assess model performance in:
- 📈 **Regression/Forecasting** – predict continuous values (e.g., sales, energy demand)
- 🧪 **Classification** – assign labels (e.g., spam, fraud, disease)
- 🧩 **Clustering** – group unlabeled data (e.g., customer segments)

They help answer:
- How accurate is the model?
- Does it generalize well?
- Is it biased?
- Is it better than a simple baseline?

---

### ⚖️ Why Use Multiple Metrics?

- Each metric gives a different view (error, bias, fit, robustness).
- No one metric tells the whole story.
- Mixing metrics ensures better evaluation and fairness.

---

### 🔤 Where:

- $y_i$ = actual (observed) value  
- $\hat{y}_i$ = predicted value  
- $\bar{y}$ = mean of actual values  
- $n$ = number of observations  
- $k$ = number of predictors (for Adjusted R²)  
- $TP$ = True Positives, $TN$ = True Negatives  
- $FP$ = False Positives, $FN$ = False Negatives  
- $w_i$ = weight of each observation  
- $p$ = predicted probability (in probabilistic models)

---

### 🔑 Metrics by Task

#### ✅ Regression & Forecasting Metrics

| Metric       | Formula                                         | Description |
|--------------|--------------------------------------------------|-------------|
| **MAE**      | $\frac{1}{n} \sum \|y_i - \hat{y}_i\|$             | Avg absolute error, in same units. Easy to interpret. |
| **MSE**      | $\frac{1}{n} \sum (y_i - \hat{y}_i)^2$           | Squares errors → penalizes large deviations more. |
| **RMSE**     | $\sqrt{\frac{1}{n} \sum (y_i - \hat{y}_i)^2}$    | Root of MSE — emphasizes large errors. |
| **MAPE**     | $\frac{100}{n} \sum \left\| \frac{y_i - \hat{y}_i}{y_i} \right\|$ | Avg % error. Unstable near 0. |
| **SMAPE**    | $\frac{100}{n} \sum \frac{\|\hat{y}_i - y_i\|}{(\|y_i\| + \|\hat{y}_i\|)/2}$ | Symmetric, avoids division by 0. |
| **MBE**      | $\frac{1}{n} \sum (y_i - \hat{y}_i)$             | Measures bias: positive = underpredict. |
| **MASE**     | $\frac{MAE}{MAE_{naive}}$                        | Scale-free; compares to naive baseline. |
| **RAE**      | $\frac{\sum \|y_i - \hat{y}_i\|}{\sum \|y_i - \bar{y}\|}$ | Absolute error relative to mean model. |
| **RSE**      | $\frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$ | Like R² but from error view. |
| **R²**       | $1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}$ | % of variance explained. |
| **Adjusted R²** | $1 - \frac{(1 - R^2)(n - 1)}{n - k - 1}$      | Penalizes extra predictors. |
| **WMAPE**    | $\frac{\sum w_i \|y_i - \hat{y}_i\|}{\sum w_i y_i} \times 100$ | Weighted MAPE — handles size variation. |
| **MdAE**     | Median $\|y_i - \hat{y}_i\|$                       | Median error; robust to outliers. |
| **Huber Loss**| Piecewise: quadratic then linear                | For training; robust to big errors. |
| **Theil’s U**| —                                               | Compares forecast to naive; U < 1 = good. |

---

#### ✅ Classification Metrics

| Metric       | Formula                                      | Description |
|--------------|----------------------------------------------|-------------|
| **Accuracy** | $(TP + TN) / (TP + TN + FP + FN)$            | Overall correct predictions. |
| **Precision**| $TP / (TP + FP)$                             | % of predicted positives that were correct. |
| **Recall**   | $TP / (TP + FN)$                             | % of actual positives correctly predicted. |
| **F1 Score** | $2 \cdot \frac{Precision \cdot Recall}{Precision + Recall}$ | Harmonic mean of precision & recall. |
| **MCC**      | Complex correlation score                    | Balanced for class imbalance. |
| **Log Loss** | $- \frac{1}{N} \sum [y_i \log(p_i) + (1 - y_i) \log(1 - p_i)]$ | For probability-based models. |
| **ROC AUC**  | — Area under TPR vs FPR                      | Ranking quality across thresholds. |
| **PR AUC**   | — Area under precision-recall curve          | Better for imbalanced data. |
| **Balanced Accuracy** | $(Recall_{class1} + Recall_{class2}) / 2$ | Adjusts for imbalance. |
| **Cohen’s Kappa** | —                                       | Agreement vs random chance. |
| **Fβ Score** | — (weighted F1 for recall/precision trade-off) | For favoring recall or precision. |
| **Brier Score** | $\frac{1}{n} \sum (p_i - y_i)^2$          | Measures accuracy of probabilistic predictions. |
| **Expected Calibration Error (ECE)** | —                    | Measures confidence calibration. |

---

#### ✅ Clustering Metrics

| Metric                       | Description |
|------------------------------|-------------|
| **Silhouette Coefficient**   | Measures separation & cohesion. Range: [-1, 1]. |
| **Davies–Bouldin Index**     | Lower = better. Measures cluster overlap. |
| **Dunn Index**               | Higher = better. Compares cluster compactness and separation. |
| **Calinski–Harabasz Index** | Ratio of between/within-cluster variance. |
| **Adjusted Rand Index (ARI)**| Measures agreement with true labels. |
| **Normalized Mutual Info (NMI)**| Information shared between clusters and ground truth. |
| **Fowlkes–Mallows Index**   | Geometric mean of precision and recall for clusters. |
| **Purity**                   | % of dominant class in each cluster. |

---

### ✅ Best Practices

- Use a mix: absolute (MAE), relative (MAPE), bias (MBE), robustness (Huber), and fit (R²).
- Always test on unseen/validation data.
- Compare to simple models (mean, last value, etc.).
- Prioritize business relevance (e.g., MAPE < 5% = good in demand forecasting).
- Use visual tools: residual plots, ROC, PR, confusion matrix heatmaps.

---
---
---

## 📊 pd.cut() vs pd.qcut()

| Feature               | `pd.cut()`                                   | `pd.qcut()`                                      |
|-----------------------|-----------------------------------------------|--------------------------------------------------|
| **Basis**             | Fixed value ranges                            | Quantiles (percentile-based)                     |
| **Bin size**          | Equal-width bins                              | Equal number of samples per bin                  |
| **Output**            | Bins based on interval (e.g., 0–10, 10–20)     | Bins like "Top 25%", "Middle 50%"                |
| **Use Case**          | When actual value ranges are meaningful        | When distribution-based segmentation is needed   |
| **Sensitive to outliers** | ✅ Yes                                   | ❌ Less sensitive                                 |
| **Example use**       | Bucketizing income levels (e.g., 0–50k, etc.) | Grouping users by engagement tiers               |

---
---
---

