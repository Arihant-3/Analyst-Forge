### Answer 

1. Done

2.  - Avg_Session_Duration_Min is the only feature that's both statistically significant and top-ranked in model.
    - | Attribute                 | Behavior of Likely Churner                    |
      | ------------------------- | --------------------------------------------- |
      | **Avg Session Duration**  | Short sessions (significantly lower)          |
      | **Days Since Last Login** | Long time ago (high value)                    |
      | **Feature Usage Score**   | Generally low interaction                     |
      | **Login Count**           | Moderate to low logins                        |
      | **Tickets Raised**        | Not strongly correlated, but worth monitoring |


3.  - 1. Send retention offers to those at high risk
      2. Ask feedback for their leave and what we can improve  
    - ```
      We know how it feels when an ex walks away.   
      But this time… it’s you who left.   
      And honestly? It hurt.   
      Let’s not stay strangers — we’d love to have you back.```

---

- **Can churn be predicted early?**  
Yes, but with ample amount of dataset and good feature engineering and good model training. 

- **Is loyalty only about usage or something deeper?**  
NO, loyalty also depends on login count, feature usage because sometimes people only open an app occasionally but values it, etc.

- **What one number would you track next month to monitor churn risk?**  
% of Active users with Declining Engagement also called - 
Leading Churn Indicator — because churn is lagging, but decline in engagement happens before users churn.

---
---

# 📉 Universal Churn Analysis – General Notes

## 🔍 What is Churn?
**Churn** refers to the rate at which customers stop engaging with or paying for a product or service.

Types of churn:
- **Customer Churn**: % of users who stop using the product or cancel service
- **Revenue Churn**: % of recurring revenue lost due to cancellations or downgrades
- **Voluntary vs. Involuntary**: Voluntary = user decision; Involuntary = failed payments, credit issues

---

## 🧠 Universal Churn Drivers

Regardless of the domain (SaaS, ecommerce, services, physical goods), churn usually results from one or more of the following:

- Lack of perceived value or ROI
- Poor onboarding or feature discovery
- Infrequent engagement or usage drop-off
- Pricing dissatisfaction or economic constraints
- Bad customer support or friction
- Better alternatives in the market

---

## 🧪 Key Behavioral & Business Metrics to Track

| Metric Type           | Examples                                                  | Applicable Contexts                                      |
|------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| **Engagement Frequency** | Logins, purchases, check-ins, usage days                 | SaaS, Mobile Apps, Ecommerce, EdTech, OTT, Utilities       |
| **Engagement Depth**     | Session duration, time spent, product views              | SaaS, Apps, OTT, Learning platforms                        |
| **Feature Usage**        | Tools/modules used, repeat orders, categories browsed    | SaaS, EdTech, Ecommerce, B2B Platforms                     |
| **Recency**              | Days since last use/order/login                          | All platforms and services                                |
| **Support Interaction**  | Tickets, complaints, negative feedback                   | All customer support-driven businesses                    |
| **Lifecycle Milestones** | Onboarding steps completed, repeat purchase milestones   | Ecommerce, SaaS, Education, Apps                          |
| **Revenue Signals**      | Subscription downgrades, cancellations, refund requests  | SaaS, Subscriptions, Utilities, Insurance                  |

---

## 🧠 Churn Segmentation Framework

Segment users based on **usage** and **retention** status:

- `High Engagement – Loyal`
- `High Engagement – Churned` 🚨
- `Low Engagement – Loyal`
- `Low Engagement – Churned`

> Prioritize understanding and recovering **High Engagement – Churned** users.

---

## 📊 How to Predict Churn

- **Model-based**: Train classification models like Logistic Regression, Random Forests, or XGBoost using behavior, usage, and support features.
- **Statistical Analysis**: Use t-tests or ANOVA to compare features between churned and non-churned groups.
- **Unsupervised Learning**: Use KMeans or DBSCAN to cluster behaviors and spot churn-risk patterns.

---

## 🔢 One Metric to Monitor Monthly

### ✅ **% of Active Users with Declining Engagement**

Track how many users are interacting **less** this month vs. previous month.

```python
# Pseudocode
declining_users = users[usage_this_month < usage_last_month * 0.7]
percent_declining = len(declining_users) / len(active_users)
```

This is a **leading indicator** of future churn.

---

## ✅ Churn Isn't Always Bad

- Some churn is **natural** or even healthy (e.g., free trial users who weren't a fit)
- Focus on **profitable, high-LTV users**
- Use cohort analysis to understand **which groups** churn faster

---

## 📌 Universal Retention Tactics

| Strategy                  | Description                                             | Contexts               |
|---------------------------|---------------------------------------------------------|------------------------|
| **Onboarding Optimization** | Help users reach value fast                            | SaaS, Apps, EdTech     |
| **Personalized Nudges**     | Triggered emails, notifications based on behavior     | Apps, Ecommerce, OTT   |
| **Win-back Campaigns**      | Offers for recently churned users                     | Subscriptions, Retail  |
| **Customer Support Quality**| Fast, empathetic, proactive service                   | All                    |
| **Pricing/Plan Flexibility**| Trials, downgrades, seasonal pauses                   | SaaS, Finance, Utilities|

---

## 🧠 Final Takeaways

- Churn is a **lagging indicator** — look for **leading signals** like behavior drop-offs, friction points, and support needs.
- Not all churn is equal: focus on **high-value churn** and segment by profitability.
- Predict, segment, and act: use models + business logic + interventions.


