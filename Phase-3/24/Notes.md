### Answer

1.  - Conversion Rate for Group A: 10.75%  
      Conversion Rate for Group B: 12.82%  
    - Null (H₀): Conversion rate for A = Conversion rate for B  
      Alternative (H₁): Conversion rate for B > A (one-tailed)  
        - If p_val < 0.05, reject H₀ → Version B has statistically significantly higher conversions.  
          If p_val >= 0.05, insufficient evidence to say B is better.   
- Since p = 0.9243 ≥ 0.05, we fail to reject the null hypothesis.  
Therefore, we do not have sufficient evidence to conclude that Version B has a higher conversion rate than Version A.  
In fact, the negative Z-value (–1.4346) suggests that Version B performed worse in this sample, but our one-tailed test only checks for B > A, so we cannot make a formal statistical conclusion about B being worse without re-running a two-tailed test.

2. Done

3.  - Do NOT roll out Version B yet.
    - 1. Run a Larger A/B Test (Increase Sample Size)
      2. Test More Than Just the Button Design
      3. Optimize for Load Time

---

- **Can higher conversion be misleading?**  
A higher conversion rate can be misleading if not analyzed in the right context.  
A higher conversion rate is a signal, not a conclusion.
You need significance, context, and alignment with goals to act on it.

- **What other hidden metrics could affect user behavior?**  
1. Bounce Rate – Users who leave without interacting.
2. Return Visits – May signal uncertainty before conversion.
3. Churn – Users who sign up but drop off quickly.

- **What happens if your sample was biased?**  
1. False Positives or Negatives
2. Poor Generalization
3. Loss of Trust
4. Wasted Resources
5. Skewed Performance Metrics

---
---

# 📊 A/B Testing Master Guide

A/B testing (also called split testing) is a **controlled experiment** used to compare two versions of something — usually in a digital product — to determine **which one performs better**.

---

## 🧠 What Is A/B Testing?

**A/B testing** is a type of **hypothesis testing** used to compare two groups (usually A and B) to understand which one has a statistically significant better outcome.

- **Group A** = Control group (existing version)
- **Group B** = Treatment group (new variation)

---

## 🎯 Why Use A/B Testing?

To make **data-driven decisions** and remove guesswork.

Used to:
- Improve **conversion rates**
- Increase **click-through rates (CTR)**
- Reduce **drop-off / bounce rates**
- Test **design, copy, or UX changes**
- Optimize **funnel or pricing strategies**

---

## 🧪 What Data Is It Used On?

A/B testing is applied on any **binary outcome** (e.g., success/failure), including:

| Use Case                        | Metric Analyzed             |
|----------------------------------|-----------------------------|
| Button redesign                 | Conversion (clicked or not) |
| Email subject line change       | Open rate (opened or not)   |
| Pricing update                  | Purchase rate               |
| Landing page change             | Signups                     |
| Ad creative                     | CTR                         |

---

## ⚙️ How A/B Testing Works

1. **Split users randomly** into Group A and Group B
2. Show each group a different version
3. Track an outcome (conversion, click, etc.)
4. **Statistically compare** the conversion rates using a **proportion Z-test**

---

## 🔬 Statistical Hypotheses (One-Tailed)

When testing if **B is better than A**:

- **Null Hypothesis (H₀):** Conversion rate of B ≤ A
- **Alternative Hypothesis (H₁):** Conversion rate of B > A

✅ Reject H₀ if **p-value < 0.05**

---

## 🔬 Statistical Hypotheses (Two-Tailed)

When testing if B is **different** from A (better or worse):

- **H₀:** Conversion rate of A = B
- **H₁:** Conversion rate of A ≠ B

✅ Reject H₀ if **p-value < 0.05**

---

## 📈 Interpreting Z-Test Results

| Z-Statistic | P-Value | Interpretation                                      |
|-------------|---------|-----------------------------------------------------|
| Z > 0       | p < 0.05 | B is significantly better than A (in 1-tailed test) |
| Z < 0       | p ≫ 0.05 | No evidence B is better; might be worse             |
| Z close to 0| p > 0.05 | No statistically significant difference             |

---

## ⚠️ Common Pitfalls & How to Prevent Them

### ❌ Biased Samples
- Problem: Results don’t represent real users
- ✅ Fix: Randomize users carefully (e.g., by user ID)

### ❌ Small Sample Size
- Problem: Results may be due to chance
- ✅ Fix: Run a **power analysis** to calculate minimum required users

### ❌ Misinterpreting p-values
- Problem: p > 0.05 ≠ B is worse
- ✅ Fix: Understand that p > 0.05 only means **"insufficient evidence"**

### ❌ One-tailed test used incorrectly
- Problem: You can’t conclude B is worse using a B > A test
- ✅ Fix: Use **two-tailed test** when you're unsure of the direction

### ❌ Only measuring top-line conversions
- Problem: Trial signups go up, but churn increases
- ✅ Fix: Track **downstream metrics** like retention and LTV

---

## 📊 Hidden Metrics to Consider

- **Click-Through Rate (CTR)**
- **Bounce Rate**
- **Scroll Depth**
- **Time on Page**
- **Form Drop-off**
- **Post-conversion churn**
- **Dwell time before click**
- **Return visit rate**

---

## 📋 Best Practices for A/B Testing

- ✅ Always randomize assignment to groups
- ✅ Run test long enough to capture real behavior (minimum 7–14 days)
- ✅ Check for sample balance (device, geo, etc.)
- ✅ Analyze results **only after** the test completes
- ✅ Use two-tailed tests unless you have strong directional expectations
- ✅ Track **secondary metrics** (not just conversions)
- ✅ Document your hypotheses **before** the test

---

## 📚 Python Snippet for Two-Proportion Z-Test

```python
from statsmodels.stats.proportion import proportions_ztest

# Example data
count = [conversions_A, conversions_B]
nobs = [total_users_A, total_users_B]

z_stat, p_val = proportions_ztest(count, nobs, alternative='larger')  # or 'two-sided'

print(f"Z-Statistic: {z_stat:.4f}")
print(f"P-Value: {p_val:.4f}")

