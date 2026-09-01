# Pandas Data Cleaning & Preprocessing — Complete Notes

> Goal: Learn the common Pandas operations used to inspect, clean, transform, preprocess, validate, and save datasets.

---

# 1. Setup

## Install Pandas

```bash
pip install pandas numpy
```

**Why use it:** Installs Pandas for data manipulation and NumPy for numerical operations.

## Import Libraries

```python
import pandas as pd
import numpy as np
```

**Why use it:** `pd` is the standard short name for Pandas and `np` is the standard short name for NumPy.

---

# 2. Create a DataFrame

```python
data = {
    "name": ["Hemil", " Rahul ", "Priya", "Hemil"],
    "age": [22, np.nan, 21, 22],
    "city": ["Surat", "surat", "SURAT", "Surat"],
    "salary": [30000, 35000, np.nan, 30000]
}

df = pd.DataFrame(data)
```

**Why use it:** Creates a table-like DataFrame that can be inspected and cleaned using Pandas.

Check it:

```python
df
```

**Why use it:** Displays the complete DataFrame when it is small enough to view.

---

# 3. Load Datasets

## Read CSV

```python
df = pd.read_csv("data.csv")
```

**Why use it:** Loads a CSV file into a Pandas DataFrame.

Useful options:

```python
df = pd.read_csv(
    "data.csv",
    sep=",",
    encoding="utf-8"
)
```

**Why use it:** Lets you control the delimiter and character encoding when a CSV is not in the default format.

## Read Excel

```python
df = pd.read_excel("data.xlsx")
```

**Why use it:** Loads spreadsheet data into Pandas.

> Note: Excel support may require an Excel engine package depending on your environment. This guide does not install `openpyxl`.

## Read JSON

```python
df = pd.read_json("data.json")
```

**Why use it:** Loads structured JSON data into a DataFrame.

---

# 4. Inspect the Dataset

Inspection should normally happen **before cleaning**.

## `head()`

```python
df.head()
```

**Why use it:** Shows the first 5 rows so you can quickly understand the dataset.

```python
df.head(10)
```

**Why use it:** Shows a specific number of rows from the beginning.

## `tail()`

```python
df.tail()
```

**Why use it:** Shows the last 5 rows and helps check the end of the dataset.

```python
df.tail(10)
```

**Why use it:** Shows a specific number of rows from the end.

## `sample()`

```python
df.sample(5)
```

**Why use it:** Shows random records and can reveal problems that are not visible at the beginning or end.

## `shape`

```python
df.shape
```

**Why use it:** Returns `(rows, columns)` so you know the size of the dataset.

Example:

```text
(1000, 8)
```

This means 1000 rows and 8 columns.

## `columns`

```python
df.columns
```

**Why use it:** Shows all column names so you can understand available fields and detect naming problems.

## `dtypes`

```python
df.dtypes
```

**Why use it:** Shows the data type of each column and helps identify incorrect types.

## `info()`

```python
df.info()
```

**Why use it:** Shows column names, non-null counts, data types, and memory usage in one summary.

## `describe()`

```python
df.describe()
```

**Why use it:** Gives statistical information such as count, mean, standard deviation, minimum, quartiles, and maximum for numerical columns.

## `describe(include="object")`

```python
df.describe(include="object")
```

**Why use it:** Summarizes text/categorical columns, including count, unique values, most common value, and frequency.

## `describe(include="all")`

```python
df.describe(include="all")
```

**Why use it:** Gives a general summary of both numerical and categorical columns.

## `memory_usage()`

```python
df.memory_usage(deep=True)
```

**Why use it:** Shows how much memory each column uses, which is useful when working with large datasets.

```python
df.memory_usage(deep=True).sum()
```

**Why use it:** Calculates the total memory used by the DataFrame.

---

# 5. Select Columns

## Select One Column

```python
df["name"]
```

**Why use it:** Accesses one column for inspection, cleaning, filtering, or calculations.

## Select Multiple Columns

```python
df[["name", "age", "salary"]]
```

**Why use it:** Selects only the columns needed for a particular operation.

## Select Columns with `loc`

```python
df.loc[:, ["name", "age"]]
```

**Why use it:** Selects columns by their labels and is especially useful when combined with conditions.

## Select Columns with `iloc`

```python
df.iloc[:, [0, 1]]
```

**Why use it:** Selects columns by their integer positions.

---

# 6. Select Rows

## Select First Row

```python
df.iloc[0]
```

**Why use it:** Accesses the first row by position.

## Select First 5 Rows

```python
df.iloc[:5]
```

**Why use it:** Selects a range of rows by integer position.

## Select Specific Rows

```python
df.iloc[[0, 2, 4]]
```

**Why use it:** Selects non-consecutive rows using their positions.

## Select One Cell

```python
df.iloc[0, 1]
```

**Why use it:** Accesses one exact value using row and column positions.

## Select by Label

```python
df.loc[0]
```

**Why use it:** Selects a row using its index label.

---

# 7. Check Missing Values

## `isnull()`

```python
df.isnull()
```

**Why use it:** Identifies cells containing missing values.

## `isna()`

```python
df.isna()
```

**Why use it:** Does the same job as `isnull()` and is commonly used to detect missing values.

## Count Missing Values

```python
df.isnull().sum()
```

**Why use it:** Counts missing values in every column.

## Missing Percentage

```python
df.isnull().mean() * 100
```

**Why use it:** Shows the percentage of missing values in each column.

## Find Rows Containing Missing Values

```python
df[df.isnull().any(axis=1)]
```

**Why use it:** Displays records where at least one column is missing.

## Check One Column

```python
df[df["age"].isnull()]
```

**Why use it:** Finds rows where a specific column contains missing data.

## `notna()`

```python
df.notna().sum()
```

**Why use it:** Counts non-missing values in each column.

---

# 8. Handle Missing Values

## Remove All Rows with Missing Values

```python
df = df.dropna()
```

**Why use it:** Removes rows containing missing values.

**When to use:** When only a small number of records are missing data and deleting them will not hurt the analysis.

## Remove Rows Missing a Specific Column

```python
df = df.dropna(subset=["age"])
```

**Why use it:** Removes only records where the selected important column is missing.

## Remove Columns with Missing Values

```python
df = df.dropna(axis=1)
```

**Why use it:** Removes columns containing missing values.

**Warning:** Do not use blindly because a column may contain useful information even if some values are missing.

## Keep Rows with Minimum Non-Null Values

```python
df = df.dropna(thresh=3)
```

**Why use it:** Keeps rows that have at least 3 non-missing values.

## Fill with a Fixed Value

```python
df["city"] = df["city"].fillna("Unknown")
```

**Why use it:** Replaces missing categorical values with a meaningful default.

## Fill Numerical Values with Mean

```python
df["salary"] = df["salary"].fillna(df["salary"].mean())
```

**Why use it:** Replaces missing numerical values with the average.

**Best for:** Data without strong outliers.

## Fill Numerical Values with Median

```python
df["age"] = df["age"].fillna(df["age"].median())
```

**Why use it:** Replaces missing values with the middle value and is more resistant to outliers than the mean.

## Fill with Mode

```python
df["city"] = df["city"].fillna(df["city"].mode()[0])
```

**Why use it:** Replaces missing categorical values with the most frequent category.

## Forward Fill

```python
df["city"] = df["city"].ffill()
```

**Why use it:** Uses the previous valid value to fill a missing value.

**Best for:** Ordered or time-series data where carrying the previous value forward makes sense.

## Backward Fill

```python
df["city"] = df["city"].bfill()
```

**Why use it:** Uses the next valid value to fill a missing value.

**Best for:** Ordered or time-series data where the next value is appropriate.

---

# 9. Detect and Remove Duplicates

## Check Duplicates

```python
df.duplicated()
```

**Why use it:** Identifies rows that are duplicates of earlier rows.

## Count Duplicates

```python
df.duplicated().sum()
```

**Why use it:** Quickly finds the total number of duplicate records.

## Remove Duplicates

```python
df = df.drop_duplicates()
```

**Why use it:** Removes repeated rows from the dataset.

## Duplicate Based on Selected Columns

```python
df = df.drop_duplicates(
    subset=["name", "age"]
)
```

**Why use it:** Finds duplicates based only on selected identifying columns.

## Keep First Duplicate

```python
df.drop_duplicates(keep="first")
```

**Why use it:** Keeps the first occurrence and removes later duplicates.

## Keep Last Duplicate

```python
df.drop_duplicates(keep="last")
```

**Why use it:** Keeps the last occurrence instead of the first.

## Remove Every Record in a Duplicate Group

```python
df.drop_duplicates(keep=False)
```

**Why use it:** Removes all rows that have duplicates instead of keeping one copy.

---

# 10. Replace Values

## Replace One Value

```python
df["city"] = df["city"].replace(
    "surat",
    "Surat"
)
```

**Why use it:** Corrects inconsistent values in a column.

## Replace Multiple Values

```python
df = df.replace({
    "N/A": np.nan,
    "NA": np.nan,
    "null": np.nan,
    "-": np.nan
})
```

**Why use it:** Converts different representations of missing data into one standard `NaN` value.

## Replace Using `loc`

```python
df.loc[
    df["city"] == "Bombay",
    "city"
] = "Mumbai"
```

**Why use it:** Changes values only in rows that meet a specific condition.

---

# 11. Clean String Data

## Remove Leading/Trailing Spaces

```python
df["name"] = df["name"].str.strip()
```

**Why use it:** Removes unwanted spaces that can cause matching and filtering problems.

## Convert to Lowercase

```python
df["name"] = df["name"].str.lower()
```

**Why use it:** Standardizes text for consistent comparisons.

## Convert to Uppercase

```python
df["name"] = df["name"].str.upper()
```

**Why use it:** Converts all text to uppercase for consistent formatting.

## Convert to Title Case

```python
df["name"] = df["name"].str.title()
```

**Why use it:** Formats names and labels consistently.

## Replace Text

```python
df["city"] = df["city"].str.replace(
    "Bombay",
    "Mumbai",
    regex=False
)
```

**Why use it:** Replaces a specific text value or phrase.

## Find Text with `contains()`

```python
df[
    df["name"].str.contains(
        "hemil",
        case=False,
        na=False
    )
]
```

**Why use it:** Finds records containing a specific piece of text.

## Check Starting Text

```python
df[
    df["name"].str.startswith(
        "H",
        na=False
    )
]
```

**Why use it:** Finds values that start with a specific character or string.

## Check Ending Text

```python
df[
    df["name"].str.endswith(
        "l",
        na=False
    )
]
```

**Why use it:** Finds values that end with a specific character or string.

## String Length

```python
df["name"].str.len()
```

**Why use it:** Finds the number of characters in each string and helps detect abnormal values.

## Split Strings

```python
df["full_name"].str.split(" ")
```

**Why use it:** Splits a string into multiple parts.

Example:

```python
df[["first_name", "last_name"]] = (
    df["full_name"].str.split(
        " ",
        n=1,
        expand=True
    )
)
```

**Why use it:** Separates combined text fields into individual columns.

---

# 12. Normalize Text

```python
df["city"] = (
    df["city"]
    .str.strip()
    .str.lower()
    .str.title()
)
```

**Why use it:** Standardizes spaces and letter casing so values such as `" surat "`, `"SURAT"`, and `"surat"` become `"Surat"`.

---

# 13. Clean Column Names

## Rename One Column

```python
df = df.rename(
    columns={"name": "student_name"}
)
```

**Why use it:** Gives a column a clearer or more consistent name.

## Rename Multiple Columns

```python
df = df.rename(columns={
    "name": "student_name",
    "salary": "annual_salary"
})
```

**Why use it:** Renames several columns at once.

## Lowercase All Column Names

```python
df.columns = df.columns.str.lower()
```

**Why use it:** Makes column naming consistent.

## Replace Spaces

```python
df.columns = df.columns.str.replace(
    " ",
    "_"
)
```

**Why use it:** Converts names such as `first name` into `first_name`.

## Clean Column Names Together

```python
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)
```

**Why use it:** Quickly standardizes column names for easier coding.

---

# 14. Data Type Conversion

## Check Data Types

```python
df.dtypes
```

**Why use it:** Identifies columns stored using an incorrect type.

## `astype()`

```python
df["age"] = df["age"].astype(int)
```

**Why use it:** Converts a column to a specified type when all values are valid for that type.

## Convert to String

```python
df["age"] = df["age"].astype(str)
```

**Why use it:** Converts values to text when string operations are required.

## Convert to Float

```python
df["salary"] = df["salary"].astype(float)
```

**Why use it:** Converts numerical values to floating-point numbers.

## `pd.to_numeric()`

```python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

**Why use it:** Safely converts mixed values to numbers.

`errors="coerce"` converts invalid values to `NaN` instead of raising an error.

---

# 15. Clean Numeric Data

Suppose salary contains:

```text
₹30,000
₹45,000
50,000
```

Clean it:

```python
df["salary"] = (
    df["salary"]
    .astype(str)
    .str.replace("₹", "", regex=False)
    .str.replace(",", "", regex=False)
)
```

**Why use it:** Removes currency symbols and commas before numeric conversion.

Convert to number:

```python
df["salary"] = pd.to_numeric(
    df["salary"],
    errors="coerce"
)
```

**Why use it:** Converts the cleaned salary values into actual numeric data.

---

# 16. Date and Time Cleaning

## Convert to Datetime

```python
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)
```

**Why use it:** Converts date strings into Pandas datetime values that can be sorted, filtered, and analyzed.

## Extract Year

```python
df["year"] = df["date"].dt.year
```

**Why use it:** Creates a year feature for yearly analysis.

## Extract Month

```python
df["month"] = df["date"].dt.month
```

**Why use it:** Creates a numeric month feature.

## Extract Day

```python
df["day"] = df["date"].dt.day
```

**Why use it:** Extracts the day of the month.

## Day Name

```python
df["day_name"] = df["date"].dt.day_name()
```

**Why use it:** Creates values such as Monday, Tuesday, etc., useful for weekday analysis.

## Date Difference

```python
df["days_since"] = (
    pd.Timestamp.today() - df["date"]
).dt.days
```

**Why use it:** Calculates how many days have passed since each date.

---

# 17. Filter Data

## Greater Than

```python
df[df["age"] > 20]
```

**Why use it:** Selects records where age is greater than 20.

## Less Than

```python
df[df["age"] < 25]
```

**Why use it:** Selects records below a specific value.

## Equal To

```python
df[df["city"] == "Surat"]
```

**Why use it:** Selects records matching a specific value.

## Not Equal

```python
df[df["city"] != "Surat"]
```

**Why use it:** Excludes records matching a specific value.

## AND Condition

```python
df[
    (df["age"] > 20) &
    (df["salary"] > 30000)
]
```

**Why use it:** Requires both conditions to be true.

> With Pandas conditions, use `&` for AND and put each condition inside parentheses.

## OR Condition

```python
df[
    (df["city"] == "Surat") |
    (df["city"] == "Mumbai")
]
```

**Why use it:** Selects records matching at least one condition.

## NOT Condition

```python
df[
    ~df["city"].isin(["Surat", "Mumbai"])
]
```

**Why use it:** Excludes values from a specified list.

---

# 18. `isin()`

```python
df[
    df["city"].isin(
        ["Surat", "Mumbai"]
    )
]
```

**Why use it:** Checks whether a value belongs to a list of allowed values.

NOT IN:

```python
df[
    ~df["city"].isin(
        ["Surat", "Mumbai"]
    )
]
```

**Why use it:** Selects values that are not in the specified list.

---

# 19. `between()`

```python
df[
    df["age"].between(20, 30)
]
```

**Why use it:** Selects values inside a range. By default, both boundaries are included.

---

# 20. `query()`

```python
df.query("age > 20")
```

**Why use it:** Provides a readable way to write filtering conditions.

Multiple conditions:

```python
df.query(
    "age > 20 and salary > 30000"
)
```

**Why use it:** Makes complex filters easier to read.

---

# 21. Sorting

## Ascending

```python
df.sort_values("salary")
```

**Why use it:** Sorts values from smallest to largest.

## Descending

```python
df.sort_values(
    "salary",
    ascending=False
)
```

**Why use it:** Sorts values from largest to smallest.

## Multiple Columns

```python
df.sort_values(
    ["city", "salary"],
    ascending=[True, False]
)
```

**Why use it:** Sorts by multiple columns with different sort directions.

## Sort Index

```python
df.sort_index()
```

**Why use it:** Sorts records according to their index.

---

# 22. Unique and Frequency Operations

## `unique()`

```python
df["city"].unique()
```

**Why use it:** Shows every distinct value in a column and helps find inconsistent categories.

## `nunique()`

```python
df["city"].nunique()
```

**Why use it:** Counts how many unique values exist.

## `value_counts()`

```python
df["city"].value_counts()
```

**Why use it:** Shows how frequently each category occurs.

Include missing values:

```python
df["city"].value_counts(
    dropna=False
)
```

**Why use it:** Includes missing values in the frequency calculation.

---

# 23. Create and Modify Columns

## Create a New Column

```python
df["monthly_salary"] = (
    df["salary"] / 12
)
```

**Why use it:** Creates a new feature from an existing column.

## Create a Percentage

```python
df["bonus"] = (
    df["salary"] * 0.10
)
```

**Why use it:** Creates a calculated value based on an existing field.

## Create a Conditional Column

```python
df["age_group"] = np.where(
    df["age"] >= 18,
    "Adult",
    "Minor"
)
```

**Why use it:** Creates categories based on a condition.

---

# 24. `apply()`

## Apply a Function

```python
def salary_category(x):
    if x >= 50000:
        return "High"
    elif x >= 30000:
        return "Medium"
    return "Low"

df["salary_category"] = (
    df["salary"].apply(salary_category)
)
```

**Why use it:** Applies custom logic to every value when normal Pandas operations are not enough.

## `lambda`

```python
df["salary_with_bonus"] = (
    df["salary"].apply(
        lambda x: x * 1.10
    )
)
```

**Why use it:** Performs a small custom operation without creating a separate function.

---

# 25. `map()`

```python
df["gender"] = df["gender"].map({
    "Male": 1,
    "Female": 0
})
```

**Why use it:** Maps specific values to replacement values, which is useful for simple categorical encoding.

---

# 26. Conditional Updates with `loc`

## Replace Invalid Salary

```python
df.loc[
    df["salary"] < 0,
    "salary"
] = np.nan
```

**Why use it:** Finds invalid values and changes only those cells.

## Update a Category

```python
df.loc[
    df["city"] == "Bombay",
    "city"
] = "Mumbai"
```

**Why use it:** Updates values only where a condition is true.

---

# 27. Delete Rows and Columns

## Delete a Column

```python
df = df.drop(
    columns=["temporary_column"]
)
```

**Why use it:** Removes unnecessary columns.

## Delete Multiple Columns

```python
df = df.drop(
    columns=["temp1", "temp2"]
)
```

**Why use it:** Removes multiple unnecessary columns at once.

## Delete Rows by Index

```python
df = df.drop(
    index=[0, 1]
)
```

**Why use it:** Removes specific rows using their index.

---

# 28. Empty and Blank Values

## Find Empty Strings

```python
(df == "").sum()
```

**Why use it:** Finds cells containing empty strings rather than actual `NaN` values.

## Convert Blank/Whitespace to NaN

```python
df = df.replace(
    r"^\s*$",
    np.nan,
    regex=True
)
```

**Why use it:** Converts empty or whitespace-only strings into proper missing values.

---

# 29. Infinite Values

## Detect Infinity

```python
np.isinf(
    df.select_dtypes(
        include="number"
    )
).sum()
```

**Why use it:** Finds positive or negative infinity values, often created by calculations such as division by zero.

## Replace Infinity

```python
df = df.replace(
    [np.inf, -np.inf],
    np.nan
)
```

**Why use it:** Converts infinite values into `NaN` so they can be handled as missing data.

---

# 30. Invalid Values

## Find Invalid Ages

```python
df[
    ~df["age"].between(0, 100)
]
```

**Why use it:** Finds ages outside a reasonable range.

## Replace Invalid Ages

```python
df.loc[
    ~df["age"].between(0, 100),
    "age"
] = np.nan
```

**Why use it:** Marks invalid ages as missing so they can be handled later.

## Find Negative Salary

```python
df[df["salary"] < 0]
```

**Why use it:** Detects values that violate a business rule such as salary not being negative.

---

# 31. Grouping and Aggregation

## `groupby().size()`

```python
df.groupby("city").size()
```

**Why use it:** Counts how many records belong to each group.

## Group Mean

```python
df.groupby("city")["salary"].mean()
```

**Why use it:** Calculates the average salary for each city.

## Group Sum

```python
df.groupby("city")["salary"].sum()
```

**Why use it:** Calculates the total salary for each city.

## Group Minimum

```python
df.groupby("city")["salary"].min()
```

**Why use it:** Finds the minimum salary in each group.

## Group Maximum

```python
df.groupby("city")["salary"].max()
```

**Why use it:** Finds the maximum salary in each group.

## Multiple Aggregations

```python
df.groupby("city")["salary"].agg(
    ["count", "mean", "min", "max"]
)
```

**Why use it:** Calculates several summary statistics at the same time.

## Multiple Columns

```python
df.groupby("city").agg({
    "salary": "mean",
    "age": "mean"
})
```

**Why use it:** Calculates different aggregations for multiple columns.

---

# 32. `agg()`

```python
df["salary"].agg(
    ["count", "mean", "min", "max", "sum"]
)
```

**Why use it:** Applies several aggregation functions to a column.

Custom aggregation:

```python
df["salary"].agg(
    ["mean", "median", "std"]
)
```

**Why use it:** Quickly compare different statistical measurements.

---

# 33. Combine DataFrames

## `concat()`

```python
result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

**Why use it:** Combines DataFrames by stacking rows.

## `merge()`

```python
result = pd.merge(
    users,
    orders,
    on="user_id",
    how="inner"
)
```

**Why use it:** Combines related tables using a common key, similar to a SQL JOIN.

Common join types:

```text
inner
left
right
outer
```

## Left Join

```python
pd.merge(
    users,
    orders,
    on="user_id",
    how="left"
)
```

**Why use it:** Keeps every record from the left DataFrame and matching records from the right.

## Outer Join

```python
pd.merge(
    users,
    orders,
    on="user_id",
    how="outer"
)
```

**Why use it:** Keeps records from both DataFrames, even when there is no match.

---

# 34. Pivot Tables

```python
pd.pivot_table(
    df,
    values="salary",
    index="city",
    aggfunc="mean"
)
```

**Why use it:** Creates a spreadsheet-style summary for analyzing data by categories.

Multiple aggregations:

```python
pd.pivot_table(
    df,
    values="salary",
    index="city",
    aggfunc=["mean", "sum"]
)
```

**Why use it:** Compares multiple summary calculations across groups.

---

# 35. Reset and Set Index

## Reset Index

```python
df = df.reset_index(
    drop=True
)
```

**Why use it:** Creates a clean sequential index after filtering or deleting rows.

## Set Index

```python
df = df.set_index("id")
```

**Why use it:** Uses a meaningful column as the DataFrame index.

## Restore Index

```python
df = df.reset_index()
```

**Why use it:** Converts the index back into a normal column.

---

# 36. Encoding Categorical Data

## One-Hot Encoding

```python
df = pd.get_dummies(
    df,
    columns=["city"],
    dtype=int
)
```

**Why use it:** Converts categories into separate 0/1 columns for machine learning.

Example:

```text
city_Mumbai  city_Surat
0            1
1            0
```

## Binary Encoding with `map()`

```python
df["gender"] = df["gender"].map({
    "Male": 1,
    "Female": 0
})
```

**Why use it:** Converts two categories into numeric values.

---

# 37. Scaling

## Min-Max Scaling

```python
df["salary_scaled"] = (
    (df["salary"] - df["salary"].min()) /
    (df["salary"].max() - df["salary"].min())
)
```

**Why use it:** Converts values to approximately a 0–1 range.

## Standardization

```python
df["salary_standardized"] = (
    df["salary"] - df["salary"].mean()
) / df["salary"].std()
```

**Why use it:** Centers values around 0 and scales them according to standard deviation.

> For machine-learning projects, `MinMaxScaler` and `StandardScaler` from scikit-learn are usually preferred because preprocessing can be fitted on training data and then applied consistently to validation/test data.

---

# 38. Outlier Detection

## IQR Calculation

```python
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
```

**Why use it:** Creates lower and upper boundaries for identifying potential outliers.

## Find Outliers

```python
outliers = df[
    (df["salary"] < lower) |
    (df["salary"] > upper)
]
```

**Why use it:** Shows records outside the IQR boundaries.

## Remove Outliers

```python
df = df[
    (df["salary"] >= lower) &
    (df["salary"] <= upper)
]
```

**Why use it:** Removes values outside the chosen boundaries when those values are confirmed to be unsuitable.

## Cap Outliers

```python
df["salary"] = df["salary"].clip(
    lower=lower,
    upper=upper
)
```

**Why use it:** Limits extreme values without deleting the entire record.

**Important:** An outlier is not automatically an error. Investigate it before removing or changing it.

---

# 39. Copy DataFrame

```python
clean_df = df.copy()
```

**Why use it:** Creates an independent DataFrame so cleaning operations do not unintentionally modify the original data.

Useful workflow:

```python
raw_df = pd.read_csv("raw_data.csv")

clean_df = raw_df.copy()
```

**Why use it:** Keeps the raw dataset available for comparison or recovery.

---

# 40. Check DataFrame Equality

```python
df1.equals(df2)
```

**Why use it:** Checks whether two DataFrames have the same shape and values.

---

# 41. Random Sampling

## Random Rows

```python
df.sample(10)
```

**Why use it:** Randomly selects records for manual inspection.

## Random Fraction

```python
df.sample(frac=0.10)
```

**Why use it:** Selects 10% of the dataset randomly.

---

# 42. Count Rows

```python
len(df)
```

**Why use it:** Returns the number of rows.

```python
df.shape[0]
```

**Why use it:** Returns the row count directly from the DataFrame shape.

---

# 43. Count Columns

```python
len(df.columns)
```

**Why use it:** Counts the number of columns.

```python
df.shape[1]
```

**Why use it:** Returns the number of columns directly from the DataFrame shape.

---

# 44. Check Data Quality

## Check Missing Values

```python
df.isnull().sum()
```

**Why use it:** Confirms whether missing values remain after cleaning.

## Check Duplicates

```python
df.duplicated().sum()
```

**Why use it:** Confirms whether duplicate rows remain.

## Check Data Types

```python
df.dtypes
```

**Why use it:** Confirms that columns have the expected types.

## Check Statistics

```python
df.describe()
```

**Why use it:** Helps identify unusual values, unexpected ranges, and possible outliers.

---

# 45. Save Cleaned Dataset

## Save CSV

```python
df.to_csv(
    "cleaned_data.csv",
    index=False
)
```

**Why use it:** Saves the cleaned DataFrame as a CSV file.

`index=False` prevents the Pandas index from being saved as an extra column.

## Save Excel

```python
df.to_excel(
    "cleaned_data.xlsx",
    index=False
)
```

**Why use it:** Saves the cleaned data in Excel format.

> Depending on your environment, Excel export may require an Excel engine package. This guide intentionally does not install `openpyxl`.

## Save JSON

```python
df.to_json(
    "cleaned_data.json",
    orient="records",
    indent=4
)
```

**Why use it:** Saves structured records in JSON format, which is useful for applications and APIs.

---

# 46. Complete Data Cleaning Workflow

A practical cleaning workflow can look like this:

```python
import pandas as pd
import numpy as np

# 1. Load raw data
df = pd.read_csv("raw_data.csv")

# 2. Keep a backup
clean_df = df.copy()

# 3. Inspect
print(clean_df.shape)
print(clean_df.columns)
clean_df.info()
print(clean_df.describe(include="all"))

# 4. Standardize missing markers
clean_df = clean_df.replace(
    ["N/A", "NA", "null", "NULL", "-", ""],
    np.nan
)

# 5. Remove duplicate rows
clean_df = clean_df.drop_duplicates()

# 6. Clean text columns
for col in clean_df.select_dtypes(
    include="object"
).columns:
    clean_df[col] = clean_df[col].str.strip()

# 7. Normalize selected categorical columns
if "city" in clean_df.columns:
    clean_df["city"] = (
        clean_df["city"]
        .str.lower()
        .str.title()
    )

# 8. Convert numeric columns
if "age" in clean_df.columns:
    clean_df["age"] = pd.to_numeric(
        clean_df["age"],
        errors="coerce"
    )

if "salary" in clean_df.columns:
    clean_df["salary"] = pd.to_numeric(
        clean_df["salary"],
        errors="coerce"
    )

# 9. Handle invalid age
if "age" in clean_df.columns:
    clean_df.loc[
        ~clean_df["age"].between(0, 100),
        "age"
    ] = np.nan

# 10. Handle missing values
if "age" in clean_df.columns:
    clean_df["age"] = clean_df["age"].fillna(
        clean_df["age"].median()
    )

if "salary" in clean_df.columns:
    clean_df["salary"] = clean_df["salary"].fillna(
        clean_df["salary"].median()
    )

if "city" in clean_df.columns:
    clean_df["city"] = clean_df["city"].fillna(
        "Unknown"
    )

# 11. Replace infinity
clean_df = clean_df.replace(
    [np.inf, -np.inf],
    np.nan
)

# 12. Final validation
print("Shape:", clean_df.shape)
print("Missing values:")
print(clean_df.isnull().sum())
print("Duplicates:", clean_df.duplicated().sum())
print("Data types:")
print(clean_df.dtypes)

# 13. Save
clean_df.to_csv(
    "cleaned_data.csv",
    index=False
)
```

**Why use this workflow:** It follows a practical order: load → inspect → standardize → clean → transform → validate → save.

---

# 47. Recommended Cleaning Order

```text
1. Load dataset
        ↓
2. Make a copy / preserve raw data
        ↓
3. Inspect shape, columns, types, statistics
        ↓
4. Standardize column names
        ↓
5. Standardize missing-value markers
        ↓
6. Remove or handle duplicates
        ↓
7. Clean string values
        ↓
8. Convert data types
        ↓
9. Validate business rules
        ↓
10. Handle missing values
        ↓
11. Detect and handle outliers
        ↓
12. Encode categorical values
        ↓
13. Scale numerical features
        ↓
14. Validate cleaned dataset
        ↓
15. Save cleaned dataset
```

---

# 48. Important Pandas Cheat Sheet

## Load

```python
pd.read_csv()
pd.read_excel()
pd.read_json()
```

**Use:** Load datasets.

## Inspect

```python
df.head()
df.tail()
df.sample()
df.shape
df.columns
df.dtypes
df.info()
df.describe()
```

**Use:** Understand the dataset before cleaning.

## Missing Values

```python
df.isnull()
df.isna()
df.notna()
df.dropna()
df.fillna()
df.ffill()
df.bfill()
```

**Use:** Find, remove, or fill missing values.

## Duplicates

```python
df.duplicated()
df.drop_duplicates()
```

**Use:** Find and remove repeated records.

## Strings

```python
.str.strip()
.str.lower()
.str.upper()
.str.title()
.str.replace()
.str.contains()
.str.startswith()
.str.endswith()
.str.split()
.str.len()
```

**Use:** Clean and standardize text.

## Data Types

```python
df.astype()
pd.to_numeric()
pd.to_datetime()
```

**Use:** Convert data into the correct type.

## Filtering

```python
df[]
df.loc[]
df.iloc[]
df.query()
df.isin()
df.between()
```

**Use:** Select records based on conditions.

## Transform

```python
df.apply()
df.map()
df.replace()
np.where()
```

**Use:** Modify and create values.

## Sorting

```python
df.sort_values()
df.sort_index()
```

**Use:** Order data.

## Categories

```python
df.unique()
df.nunique()
df.value_counts()
pd.get_dummies()
```

**Use:** Analyze and encode categorical data.

## Grouping

```python
df.groupby()
df.agg()
```

**Use:** Summarize data by groups.

## Combine

```python
pd.concat()
pd.merge()
```

**Use:** Combine DataFrames.

## Outliers

```python
df.quantile()
df.clip()
```

**Use:** Detect and limit extreme values.

## Index

```python
df.set_index()
df.reset_index()
```

**Use:** Manage DataFrame indexes.

## Save

```python
df.to_csv()
df.to_excel()
df.to_json()
```

**Use:** Export cleaned data.

---

# 49. Best Practices

1. **Never overwrite the raw dataset.** Keep the original data unchanged.
2. **Inspect before cleaning.** Understand the problem before changing values.
3. **Do not delete missing rows blindly.** Choose a strategy based on the data.
4. **Do not remove every outlier automatically.** Some outliers are legitimate.
5. **Use consistent text formatting.** For example, standardize `"Surat"`, `"surat"`, and `" SURAT "`.
6. **Validate data types after conversion.**
7. **Check duplicates after cleaning.**
8. **Validate the final dataset before saving.**
9. **For ML, fit preprocessing transformations only on training data** to avoid data leakage.
10. **Keep a clear raw → cleaned workflow** so the process can be reproduced.

---

# 50. Final Learning Checklist

- [ ] Load CSV/Excel/JSON data
- [ ] Inspect rows and columns
- [ ] Understand data types
- [ ] Find missing values
- [ ] Remove missing values
- [ ] Fill missing values
- [ ] Find duplicates
- [ ] Remove duplicates
- [ ] Clean string values
- [ ] Standardize text
- [ ] Rename columns
- [ ] Convert numeric values
- [ ] Convert dates
- [ ] Filter data
- [ ] Sort data
- [ ] Create new columns
- [ ] Use `apply()` and `map()`
- [ ] Replace invalid values
- [ ] Group and aggregate data
- [ ] Merge and concatenate DataFrames
- [ ] Encode categorical features
- [ ] Scale numerical features
- [ ] Detect and handle outliers
- [ ] Validate the cleaned dataset
- [ ] Save CSV/Excel/JSON output
