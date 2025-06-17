### Answers

1. |Features        |   %Percentage |
   | -------------- | ------------- |
   |Age             |      5.0      | 
   |Blood_Pressure  |     10.0      |
   |Cholesterol     |     10.0      |

2. As blood pressure and cholesterol are continuous variables, we can use mean imputation.  
As, for cholestrol data - Mean Imputation is acceptable, but slightly riskier in skewed data.
Because the age has skewness and multiple peaks, median is robust to outliers and works well with non-normal distributions.

3. I have done different strategies for Age column. Results are almost equal.

4. We can see the drastic change in Blood pressure between 120-125  
We can see the drastic change in Cholestrol around 200    
We can see the drastic change in Age in between 40-50    

5. Risks or consequences of poor imputation in healthcare datasets.
    - Risks of management of treatment of patients
    - It will harm the reputation of the healthcare like 'Hospitals'
    - It will lead to wrong production of the supplies/medicine if data is poorly imputed.


---

### 📘 Imputation and Missing Data Handling

#### 🔍 What is Imputation?

Imputation is the process of **replacing missing values** in a dataset with estimated or calculated values. This helps retain the dataset's structure and allows machine learning algorithms to function properly.

---

#### 🛠️ Common Imputation Methods

| Method                  | Description                                                  | Best Use Case                        |
|-------------------------|--------------------------------------------------------------|--------------------------------------|
| **Mean Imputation**     | Replace missing values with the **mean** of the column.      | Normal distributions                 |
| **Median Imputation**   | Replace missing values with the **median**.                  | Skewed distributions or outliers     |
| **Mode Imputation**     | Replace with the **most frequent** value (categorical data). | Categorical variables                |
| **KNN Imputation**      | Estimate missing values using similar rows (neighbors).      | When data has correlated features    |
| **Regression Imputation** | Predict missing value using other features.                | Continuous numeric features          |
| **MICE** (Multiple Imputation by Chained Equations) | Iteratively predicts missing data using regression models. | Complex and multivariate data |
| **Forward/Backward Fill** | Use previous/next valid value.                             | Time series data                     |
| **Random Sampling**     | Randomly pick from existing values in the column.            | When randomness is acceptable        |

---

### 📌 Summary

- **Use median** if you want quick and safe imputation.
- **Use KNN or MICE** if your data has rich features and you're doing a serious ML task.
- **Visualize the results** to understand the impact of each strategy.
