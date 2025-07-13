### Answer

1.  - Done
    - Week 6 and 9 have week signup cohort and Week 11 and 12 have strong signup cohort.

2.  - |                         | Churned |
      | ----------------------- | ------- |
      |Referral                 | 0.026245|
      |Avg_Session_Length_Min   |-0.021224|

3.  Q: **Why is retention dropping?**  
    A: Retention dropped after Week 9. Feedback data shows a rise in themes like "Missing features", "Slow performance" and "Too many bugs". This aligns with a product update during that time, suggesting the update may have caused user dissatisfaction.

    Q: **Who is churning?**  
    A: Users who churned after Week 9 were more likely to:
    - Leave feedback related to bugs/performance/missing features
    - Not come from referrals (lower trust)

    Q: **What should we do?**  
    - Roll back or patch the update quickly
    - Use feedback to prioritize fixes (especially bugs and missing features)
    - Send personalized emails:
        - Bugs: "We fixed what was broken. Try the improved experience now!"
        - Content: "New content just dropped — picked based on your feedback!"
        - Pricing: "You asked. We listened. Special pricing for you this week only!"
    - Launch a quick survey to ask, "What would bring you back?"

---
---

## 🧠 What’s the Difference Between pd.get_dummies() vs. groupby().mean() for Churn Analysis?

| Feature              | `groupby().mean()`                           | `pd.get_dummies()` + `.corr()`                          |
| -------------------- | -------------------------------------------- | ------------------------------------------------------- |
| **Purpose**          | Understand **average churn rate** per theme  | Understand **linear correlation** with churn            |
| **Type of Result**   | Simple summary (mean churn % for each theme) | Numeric correlation score (-1 to +1)                    |
| **Good For**         | Direct interpretation, clear comparison      | Feature selection, modeling insight                     |
| **Works With**       | Any data (including non-numeric)             | Only after converting to numeric (via dummies/encoder)  |
| **Interpretability** | Very high (easy to explain to stakeholders)  | Medium (requires understanding of correlation strength) |
| **Used In**          | EDA, dashboards, reporting                   | ML preprocessing, advanced analytics                    |
