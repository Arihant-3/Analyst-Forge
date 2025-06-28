### Answer

1. Done

2. Done

3. Done

4. Done

5.  - Order_value_per_item is the most important feature
    - | Metric                      | Before (`unbalanced`) | After (`balanced`) |
      | --------------------------- | --------------------- | ------------------ |
      | **Returned Precision (1)**  | 0.00                  | 0.12               |
      | **Returned Recall (1)**     | 0.00                  | 0.50               |
      | **Returned F1-Score (1)**   | 0.00                  | 0.19               |
      | **Accuracy**                | 87%                   | 45%                |

After applying class_weight='balanced' to logistic regression:  
    Recall for returned orders improved from 0.00 to 0.50  
    Precision for returned orders improved from 0.00 to 0.12  
    Overall accuracy dropped from 87% to 45%, due to the model no longer ignoring the minority class

✅ This trade-off is often acceptable when the business goal is to detect rare but costly return events, rather than maximizing raw accuracy.

---

- **What kind of behavior leads to returns?**  
High order value per item  
Longer Shipping times
Specific payment methods – Debit and Credit Cards show stronger links than UPI.
Fewer items per order

- **Can we proactively reduce return risk using these insights?**  
Yes:
    - Flag high-risk orders in real time
    - Promote prepaid methods (e.g., UPI over COD)
    - Improve product info for high-value or single-item orders
    - Restrict returns for risky profiles
    - Retrain models regularly to track changing trends




```
before:-

                 precision    recall  f1-score   support
           0       0.87      1.00      0.93       174
           1       0.00      0.00      0.00        26

    accuracy                           0.87       200
   macro avg       0.43      0.50      0.47       200
weighted avg       0.76      0.87      0.81       200


after applying balanced:-

                 precision    recall  f1-score   support
           0       0.86      0.44      0.58       174
           1       0.12      0.50      0.19        26

    accuracy                           0.45       200
   macro avg       0.49      0.47      0.39       200
weighted avg       0.76      0.45      0.53       200
```