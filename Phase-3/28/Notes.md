### Answer

1. Done

2.  - Top 2 Themes from Loyal Users:- Other, Content Issues
    - Top 2 Themes from At-Risk Users:- Other, Positive Experience
    - Recommendations: 
        - Address the content issuses from loyal users like Update outdated material, Add more advanced/practical examples, etc.
        - Re-engage Happy-but-Inactive Users by Offering content previews or free unlocks to draw them back.

3. Done

---

- **Why is it risky to ignore free-text feedback in data analysis?**  
1. Loss of nuance: Structured data misses emotions, pain points, and suggestions users express in their own words.
2. Missed trends: Emerging issues or ideas may only appear in open text before they're reflected in metrics.
3. Blind spots: You may overlook critical feedback not captured by predefined categories.

- **What insights can only come from qualitative data?**  
1. User emotions & tone
2. Unexpected issues or edge cases
3. Contextual stories that explain why something happened, not just what
4. Specific suggestions or feature requests by user's own words
5. Intention and motivation behind the action of the user

- **How would you automate this at scale?**  
By integrating NLP techniques on the Feedback_Text column, we can extract key patterns, themes, and sentiment. This allows us to convert unstructured text into valuable features (tokens or embeddings) that machine learning models can train on at scale.

---
---

## 🔢 `rank(pct=True)` – What & Why

- **What it does**:  
  Converts a numeric column into **percentile ranks** (values from 0 to 1).

- **Why it’s useful**:
  - Normalizes features with different scales.
  - Ensures no single variable dominates when building weighted scores.
  - Helps build balanced metrics like engagement or risk scores.

- **Common use cases**:
  - Scoring users based on multiple behaviors (e.g., sessions, courses, recency).
  - Creating fair segmentations from mixed-scale features.

---