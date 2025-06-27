### Answer 

1. Done

2. Done

3. Done

4.  - Yes, there are natural groupings.
    - Cluster 0 :- Older, Low income, Moderate Spending, Infrequent Visitors  
      Cluster 1 :- Middle-aged, Average Income, High Spending, Frequent Visits  
      Cluster 2 :- Middle-aged, High Income, Low spending, Frequent Visits  
      Cluster 3 :- Young, Low Income, Moderate Spending, High Visits

---

- **Are high spenders forming their own cluster?**  
Yes

- **Do age/income/visit behavior correlate with separation?**  
Age correlates strongly with t-SNE separation.  
Annual Income does correlate well with t-SNE separation.  
Visits per Month does not strongly correlate with t-SNE separation

- **How might this help in marketing personalization?**  
This data analysis can help to customize the offers, emails, and 
give them the type of content they like to hook them, etc.

---
---

# 🧠 t-SNE for Customer Behavior Analysis

## 🔍 What is t-SNE?

**t-SNE (t-distributed Stochastic Neighbor Embedding)** is a non-linear dimensionality reduction technique used to visualize high-dimensional data in 2 or 3 dimensions. It focuses on preserving **local similarities**—customers who behave similarly in the original data stay close together in the plot.

---

## 🛠️ How it Works

- Converts pairwise distances into **probability distributions**.
- Tries to keep similar points close and dissimilar ones far in 2D/3D space.
- Best used after **normalizing data**.
- Often visualized with color-coded clusters (e.g., using **KMeans**).

---

## 🎯 Applications

- **Customer Segmentation**: Discover behavioral groups based on age, income, visits, etc.
- **Anomaly Detection**: Spot outliers who don't fit normal spending or browsing patterns.
- **Behavioral Profiling**: Understand how features like income or engagement affect actions.
- **Marketing**: Tailor strategies to distinct segments identified in t-SNE space.

---

## 📈 Predicting Customer Behavior with t-SNE

While t-SNE is not a predictive model itself, it **reveals clusters** that hint at behavior patterns:

- Customers grouped closely tend to **behave similarly** (e.g., high-spenders, frequent visitors).
- Marketers or analysts can assign **labels** (e.g., "bargain hunters", "loyal high spenders") based on cluster properties.
- Use these clusters to **train models**, personalize offers, or detect shifts in engagement.

**Example insights:**
- A cluster of young, high-click, low-income users → likely browsing more than buying.
- High-income cluster separated from low spenders → target for premium upselling.

---

## 📊 Typical Graph Patterns & Correlation Cases

| Feature              | Visual Pattern in t-SNE       | Possible Insight                             |
|----------------------|-------------------------------|----------------------------------------------|
| **Age**              | Vertical gradient             | Younger vs. older behavior contrast          |
| **Annual Income**    | Horizontal split or gradient  | Spending capacity impacts behavior           |
| **Visits per Month** | Scattered pattern             | No strong cluster separation                 |
| **Spending Score**   | Dense clusters or blobs       | Indicates behavioral segmentation            |
| **Clicks per Visit** | Tight clusters or overlaps    | High digital engagement regions              |

- **Gradient**: Suggests linear correlation with t-SNE dimensions.
- **Tight blobs**: Strong local similarity; useful for customer targeting.
- **Scattered points**: Weak or no correlation; feature may be less impactful.

---

## ✅ Summary

t-SNE doesn’t directly predict customer behavior but **visualizes structure** in a way that makes it easier to:
- **Spot behavioral patterns**
- **Segment customers**
- **Target campaigns**
- **Build better predictive models**

Combine it with clustering (like KMeans) and follow up with domain-specific labeling for impactful insights.

