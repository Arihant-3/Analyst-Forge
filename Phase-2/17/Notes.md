### Answer

1. Done

2. Done

3. Done

4.  - A is significantly better
    - NO 

---

- **What is the p-value and what does it mean?**  
It's the chance of seeing your result if there's no true difference.  


- **Is the sample size large enough?**  
No, the sample size is likely not large enough to detect a small difference with high confidence.

- **Would you recommend launching the new version?**  
Result: The difference is NOT statistically significant (p ≥ 0.05).
Recommendation: Stick to current version or collect more data.

---
---

# 🧪 A/B Testing — Complete Notes

## 📘 What is A/B Testing?
A/B testing is a controlled experiment comparing two versions (A and B) to determine which performs better on a key metric (e.g., conversion rate, click-through rate, revenue per user, etc.).

---

## 🔤 Key Terminology

- **Group A (Control)**: The current or original version.
- **Group B (Variant)**: The new or modified version being tested.
- **Conversion**: A user completing the desired action (e.g., purchase, sign-up).
- **Conversion Rate**: Conversions / Total Visitors.
- **Null Hypothesis (H₀)**: Assumes no difference between A and B.
- **Alternative Hypothesis (H₁)**: Assumes a meaningful difference between A and B.
- **P-value**: Probability of observing the result (or more extreme) under H₀.
- **Alpha (α)**: The threshold for significance (commonly 0.05).
- **Effect Size**: Magnitude of the difference between A and B.
- **Power**: Probability of detecting a true effect (commonly 80%).

---

## 🔬 Statistical Testing for Conversion Rates

### ✅ Use Case:
Use **Two-Proportion Z-Test** when:
- You are comparing **two groups**.
- The outcome is **binary** (e.g., converted: yes/no).
- You want to test **proportions** (e.g., 10% vs 13%).

### 🧪 Hypotheses
- **H₀**: Conversion_A = Conversion_B
- **H₁**: Conversion_A ≠ Conversion_B (two-sided)

### 📉 Z-Test for Proportions (Python Example)
```python
from statsmodels.stats.proportion import proportions_ztest

count = [converted_A, converted_B]      # number of conversions
nobs = [total_A, total_B]               # total users in each group

z_stat, p_val = proportions_ztest(count=count, nobs=nobs)
```

---

## 📌 P-Value Interpretation

- **p < 0.05** → Statistically significant → Reject H₀ → Likely a real difference.
- **p ≥ 0.05** → Not statistically significant → Not enough evidence to reject H₀.

⚠️ A non-significant result doesn't mean B is worse — it could mean **not enough data**.

---

## 🔢 Calculating Effect Size

$
\text{Effect Size} = \text{Conversion}_B - \text{Conversion}_A
$

Even if the effect is small (e.g., 3%), it might still be **practically significant** depending on business goals.

---

## 🎯 Sample Size & Power

To detect a meaningful difference with:
- **α = 0.05** (confidence level = 95%)
- **Power = 0.80** (80% chance of detecting a real effect)
- Small effect (e.g., 3%)

🔢 You typically need **>1,000 users per group**

Use tools like:
- [Evan Miller's Sample Size Calculator](https://www.evanmiller.org/ab-testing/sample-size.html)

---

## 📊 Visualization (Optional)

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(data=df, x='Group', y='Converted', ci=95)
plt.title("Conversion Rate by Group (95% CI)")
plt.ylim(0, 0.2)
plt.show()
```

---

## ✅ Decision Checklist

| Question                          | Yes/No |
|----------------------------------|--------|
| Did you define a clear hypothesis?         | ✅    |
| Is the sample size large enough?          | ✅/❌ |
| Is the p-value < α (e.g., 0.05)?           | ✅/❌ |
| Is the effect size practically significant?| ✅/❌ |
| Did you check power before starting?       | ✅/❌ |

---

## ⚠️ Common Mistakes

- Stopping test too early (before enough data)
- Interpreting p > 0.05 as "no difference"
- Not accounting for multiple testing
- Ignoring practical/business significance

---

## 🧠 Pro Tips

- Always predefine: goal, hypothesis, metric, alpha, and sample size.
- Visualize results with confidence intervals.
- Consider **Bayesian A/B testing** if sample size is small or you want probability-based insights.

---

## 📚 Resources

- [Statsmodels Documentation](https://www.statsmodels.org/)
- [Optimizely A/B Testing Guide](https://www.optimizely.com/)
- [Evan Miller's Tools](https://www.evanmiller.org/)

---
