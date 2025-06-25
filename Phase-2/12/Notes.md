### Answer 

1. Done

2. Median survival time of customers is 227 days

3. Done

4. Done

---

- **What % of customers churn within the first 90 days?**  
Estimated 25.90% of customers churned within 90 days (Kaplan-Meier).

- **Which period has the highest hazard (drop-off spike)?**  
Highest hazard (drop-off spike) occurs at day 1009.0,
with an estimated hazard rate of 1.0000

- **What business action could increase survival?**  
1. We can provide discount to the users.
2. Send them personalised message according to their purchase to hook them.
3. Get feedbacks, and then try to apply that to maintain credibility.

---
---

| Expression                                    | What it means                              | Does it include censoring? | Is it a survival metric? |
| --------------------------------------------- | ------------------------------------------ | -------------------------- | ------------------------ |
| `df['Duration'].median()`                     | Median of *all* durations                  | ❌ No                       | ❌ No                     |
| `df[df['Churned'] == 1]['Duration'].median()` | Median of *only churned* users' lifetimes  | ❌ No                       | ❌ No                     |
| `df[df['Churned'] == 0]['Duration'].median()` | Median of *active* users’ durations so far | ✅ Censored users only      | ❌ No                     |
| `kmf.median_survival_time_`                   | Time when 50% users expected to churn      | ✅ Yes                      | ✅ Yes                    |

---

# 📘 Kaplan-Meier Survival Analysis for Churn

## 🔹 What is Survival Analysis?
- Statistical method to study **time until an event occurs** (e.g., churn).
- Handles **censored data** (users who haven't churned yet).

## 🔹 Key Terms

### 1. **Duration**
- Time between **start (signup)** and **event (churn or censoring)**.

### 2. **Event Observed**
- Binary indicator:
  - `1` = churned
  - `0` = still active (censored)

### 3. **Censoring**
- When a customer has **not churned** by the end of the observation period.
- We know they've survived *at least* till a point, but not beyond.

### 4. **Survival Function (S(t))**
- Probability that a user survives (doesn’t churn) beyond time *t*.
- Always starts at 1 and decreases over time.

### 5. **Kaplan-Meier Estimator**
- A **non-parametric** estimator of the survival function.
- Adjusts the survival curve each time a churn event occurs.
- Takes censoring into account.

### 6. **Hazard Function**
- The **instantaneous rate of churn** at a given time *t*.
- Shows where the risk of churn spikes.

## 🔹 Why Use Survival Analysis?

- Understand **when** users are most likely to churn.
- Identify **high-risk periods** in the customer lifecycle.
- Compare **retention across cohorts** (e.g., signup months/quarters).
- Make data-driven decisions to **improve retention**.
