### Answer

1. Done

2. Done

3. Done

4. -  |positive_word | positive_frequency |
      | ------------ | ------------------ |               
      |  good	     |      689           |
      |  useful	     |      698           |
      |  durable	 |      697           |

   -  |negative_word | negative_frequncy |
      | ------------ | ----------------- |
      | expensive	 |      693          |
      | useless	     |      670          |
      | broken	     |      689          |

---

- **Do users tend to emphasize positives or negatives?**  
Yes

- **Which product traits seem most commented on?**  
useful and expensive

- **What could a brand improve based on frequent negatives?**  
Brand should cost cut few months to build trust and then gradually increase the cost to maintain the overall cost. And see the warehouse and improve the quality of the product and also make sure that the delivery person handling the product without breaking it.

---
---

### 🔍 Total Occurrence vs Frequency

#### 📌 Basic Definitions:

- **Total Occurrence**:  
  Total number of times a word appears across **all reviews**.  
  → Counts every repetition.

- **Frequency**:  
  Number of **reviews** in which a word appears **at least once**.  
  → Ignores how many times the word appears in a single review.

```
# Total Occurrence
def total_occurrence(word):
    return sum(review.count(word) for review in df['Token'])

# Frequency
def frequency(word):
    return sum(word in review for review in df['Token'])
```

---
---

# ✅ Word Frequency: str.contains() vs Token List

## 🔹 Version 1: Using `str.contains()`
```
python
def freq_word(word):
    return df['Text'].str.contains(word).sum()
```
🔍 What it does:

- Searches if the string word appears as a substring in the review

- Case-sensitive by default

- May match partial words  
👉 Example: searching "use" will match "useful" and "useless"  

*⚠️ Problems:*

- Not suitable if you want exact word matches

- Can give false positives when word is part of another word


## 🔹Version 2: Using Token List
```
def freq_word(word):
    return sum(word in review for review in df['Token'])
```
🔍 What it does:

- Assumes each review is already tokenized into a list of words

- Checks if the exact word is in the list of tokens

- ✅ Much more accurate for exact word frequency counting

