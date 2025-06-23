## 📌 Difference Between `dt.year` vs `str.split('-').str[0]`

```
| Feature          | `df['Date'].dt.year`                    | `df['Date'].str.split('-').str[0]`          |
|------------------|-----------------------------------------|---------------------------------------------|
| Input Type       | `datetime64[ns]`                        | `str` or `object`                           |
| Output Type      | `int`                                   | `str`                                       |
| Speed & Safety   | Fast, format-safe                       | Slower, format-dependent                    |
| Use Case         | Accurate date-based operations          | Quick fix if string is well-formatted       |
| Best Practice    | ✅ Use this after `pd.to_datetime()`    | ⚠️ Use only if format is guaranteed        |
```

👉 **Tip**: Always prefer `.dt.year` for reliability and performance.

----
----

## Basic Formulas for NULL
```
missing_percentage = df.isnull().mean() * 100
print(missing_percentage)
```

----
----

## Tokenize and clean the text
```
import pandas as pd
import string

# Load the dataset
df = pd.read_csv("dataset.csv")

# Function to clean and tokenize
def clean_and_tokenize(text):
    # Lowercase
    text = text.lower()
    # Remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")
    # Tokenize by splitting on whitespace
    tokens = text.split()
    return tokens

# Apply the function to the 'Text' column
df['Tokens'] = df['Text'].apply(clean_and_tokenize)

# Display sample
print(df.head())
```

----
----

