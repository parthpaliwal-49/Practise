### 1. **Reading a CSV File**
```python
df = pd.read_csv(file_path, sep='|', index_col=False, dtype={'col1': dtype},
                 converters={'col1': function_to_change_format1, 'col2': function_to_change_format2},
                 encoding='latin-1', on_bad_lines='warn', skiprows=1, names=[header_list])
```
- **sep**: Specifies the delimiter (`'|'` in this case).
- **index_col**: Defines the column(s) to set as index (`False` if no index is needed).
- **dtype**: Ensures the data type of each column is correct.
- **converters**: Allows applying custom conversion functions.
- **encoding**: Defines the file encoding (`'latin-1'` for non-UTF8 files).
- **on_bad_lines**: Handles bad lines (`'warn'` to log and skip).
- **skiprows**: Skips the first `n` rows.
- **names**: Assigns column names if headers are missing.

### 2. **Handling Missing Data**
```python
df.isnull().sum()  # Count missing values in each column

df_clean = df.dropna()  # Drop rows with missing values

df_filled = df.fillna(0)  # Fill missing values with 0
```
- **dropna()**: Removes rows with `NaN` values. 
  - **Important Parameters**: `how`, `thresh`, `subset`
- **fillna()**: Replaces `NaN` values.
  - **Important Parameters**: `value`, `method`, `axis`

### 3. **Renaming and Dropping Columns**
```python
df.rename(columns={'old_name': 'new_name'}, inplace=True)  # Rename a column

df.drop('column_name', axis=1, inplace=True)  # Drop a column
```
- **rename()**: Used to change column names.
  - **Important Parameters**: `columns`, `index`, `inplace`
- **drop()**: Removes specified rows or columns.
  - **Important Parameters**: `labels`, `axis`, `inplace`

### 4. **Sorting DataFrame**
```python
df_sorted = df.sort_values('column_name')  # Sort DataFrame by a column
```
- **sort_values()**: Sorts by column(s).
  - **Important Parameters**: `by`, `ascending`, `inplace`, `na_position`

### 5. **Applying Functions**
```python
df['new_column'] = df['column'].apply(lambda x: x*2)  # Apply a function to a column
```
- **apply()**: Applies a function along the axis.
  - **Important Parameters**: `func`, `axis`

### 6. **Merging and Concatenating DataFrames**
```python
df_merged = pd.merge(df1, df2, on='key_column')  # Merge two DataFrames

df_combined = pd.concat([df1, df2])  # Concatenate two DataFrames
```
- **merge()**: Joins DataFrames on key columns.
  - **Important Parameters**: `how`, `on`, `left_on`, `right_on`, `suffixes`
- **concat()**: Combines DataFrames along a particular axis.
  - **Important Parameters**: `objs`, `axis`, `ignore_index`, `join`

### 7. **Reshaping DataFrame**
```python
df_melted = df.melt(id_vars=['id'], value_vars=['var1', 'var2'])  # Unpivot a DataFrame from wide to long format
```
- **melt()**: Converts wide format to long format.
  - **Important Parameters**: `id_vars`, `value_vars`, `var_name`, `value_name`

### 8. **Calculating Correlation**
```python
df_corr = df.corr()  # Compute pairwise correlation of columns
```
- **corr()**: Computes correlation between columns.
  - **Important Parameters**: `method`, `min_periods`

### 9. **Handling Duplicates**
```python
df_unique = df.drop_duplicates()  # Remove duplicate rows
duplicates = df.drop_duplicates(subset=['column1','column2'])  # Remove duplicate rows based on specific columns
```
- **drop_duplicates()**: Removes duplicate rows.
  - **Important Parameters**: `subset`, `keep`, `inplace`

### 10. **Counting Unique Values**
```python
df.nunique()  # Count the number of unique values per column

df['column'].value_counts()  # Count unique values in a column
```
- **nunique()**: Returns the count of unique values per column.
- **value_counts()**: Returns the counts of unique values.

### 11. **Index Manipulation**
```python
df_indexed = df.set_index('column_name')  # Set a column as the index

df_reset = df.reset_index()  # Reset the index to default integer index
```
- **set_index()**: Sets a DataFrame column as the index.
- **reset_index()**: Resets the index to a default integer index.

### 12. **Saving to CSV**
```python
df.to_csv('output.csv', index=False)  # Save DataFrame to a CSV file without the index
```
- **to_csv()**: Exports DataFrame to CSV.
  - **Important Parameters**: `path_or_buf`, `sep`, `index`, `header`

### 13. **Filtering Data**
```python
df[df['column'] > 10]  # Filter rows where column values are greater than 10

df[(df['column1'] > 10) & (df['column2'] < 5)]  # Filter with multiple conditions using AND

df[(df['column1'] > 10) | (df['column2'] < 5)]  # Filter with multiple conditions using OR
```
- **Filtering**: Use conditions to filter rows.
  - **AND**: `&`, **OR**: `|`, **NOT**: `~`

### 14. **Working with Missing Data**
```python
df['column'].isnull()  # Check for missing values in a column

df['column'].fillna('Unknown', inplace=True)  # Fill missing values in a column
```
- **isnull()**: Checks for `NaN` values.
- **fillna()**: Fills `NaN` with specified values.

### 15. **Replacing Values**
```python
df['column'].replace({'old_value': 'new_value'}, inplace=True)  # Replace specific values in a column
```
- **replace()**: Replaces values in a DataFrame.
  - **Important Parameters**: `to_replace`, `value`, `inplace`

### 16. **Conditional Operations**
```python
df['new_column'] = df['column'].apply(lambda x: 'Yes' if x > 10 else 'No')  # Conditional column creation

df['new_column'] = np.where(df['column'] > 10, 'High', 'Low')  # Use np.where to assign based on condition
```
- **apply()**: Applies a function for conditional logic.
- **np.where()**: Vectorized alternative for conditional operations.

### 17. **Cumulative and Rolling Calculations**
```python
df['cumsum'] = df['column'].cumsum()  # Cumulative sum of a column

df['rolling_mean'] = df['column'].rolling(window=3).mean()  # Rolling mean with a window of 3
```
- **cumsum()**: Computes cumulative sum.
- **rolling()**: Applies rolling window operations.
  - **Important Parameters**: `window`, `min_periods`, `center`

### 18. **Assigning Values Based on Condition**
```python
df.loc[df['column'] > 10, 'new_column'] = 'High'  # Assign 'High' where column values are greater than 10
```
- **loc[]**: Accesses a group of rows and columns by labels or conditions.

### 19. **Selecting Specific Rows/Columns**
```python
df.iloc[0:5, 0:3]  # Select first 5 rows and first 3 columns
```
- **iloc[]**: Selects by integer-location indexing.
  - **loc[]**: Selects by label-based indexing.

### 20. **Sorting by Multiple Columns**
```python
df.sort_values(by=['column1', 'column2'], ascending=[True, False], inplace=True)  # Sort by multiple columns
```
- **sort_values()**: Sorts by multiple columns with different orders.

### 21. **Grouping and Aggregating Data**
```python
df_grouped = df.groupby('column_name').mean()  # Group by a column and calculate the mean

df.groupby('column').agg({'col1': 'mean', 'col2': 'sum'})  # Group by a column and aggregate

df_agg = df.agg({'col1': 'mean', 'col2': 'sum'})  # Aggregate data with different functions
```
- **groupby()**: Groups DataFrame by a column.
  - **agg()**: Performs aggregate operations.
```

### 22. **Pivoting DataFrame**
```python
df_pivot = df.pivot(index='row', columns='column', values='value')  # Pivot a DataFrame
```
- **pivot()**: Reshapes data (produces a "pivot" table) where rows become columns.
  - **Important Parameters**: `index`, `columns`, `values`
  - **Use Case**: Useful for transforming data from a long format to a wide format, where each unique value in the specified column becomes a separate column.

### 23. **Dropping Duplicates**
```python
df_unique = df.drop_duplicates()  # Drop duplicate rows
```
- **drop_duplicates()**: Removes duplicate rows from the DataFrame.
  - **Important Parameters**: `subset`, `keep`, `inplace`
  - **Use Case**: Useful when you need to ensure that the data in your DataFrame is unique, particularly when merging or concatenating DataFrames.

### 24. **Finding Index of Maximum/Minimum Values**
```python
max_index = df['column'].idxmax()  # Index of the maximum value in a column

min_index = df['column'].idxmin()  # Index of the minimum value in a column
```
- **idxmax()**: Returns the index of the first occurrence of the maximum value.
- **idxmin()**: Returns the index of the first occurrence of the minimum value.
  - **Use Case**: Useful for identifying the position of the highest or lowest value in a DataFrame column, which can be crucial for data analysis tasks such as outlier detection.

### 25. **Calculating Percentage Change**
```python
df['pct_change'] = df['column'].pct_change()  # Percentage change in a column
```
- **pct_change()**: Calculates the percentage change between the current and a prior element.
  - **Important Parameters**: `periods`, `fill_method`, `limit`
  - **Use Case**: Commonly used in financial analysis to calculate the percentage change in stock prices, sales data, or other time series data.

### 26. **Correlation Between Two Columns**
```python
correlation = df[['column1', 'column2']].corr()  # Correlation between two columns
```
- **corr()**: Computes the correlation coefficient between pairs of columns.
  - **Use Case**: Useful for understanding the relationship between two variables, which can be particularly valuable in exploratory data analysis and feature selection for machine learning.

### 27. **Converting Data Types**
```python
df['column1'] = pd.to_datetime(df['column1'], format='%Y-%m-%d')  # Convert datatype to DATE
```
- **pd.to_datetime()**: Converts an argument to datetime.
  - **Important Parameters**: `format`, `errors`, `utc`
  - **Use Case**: Essential for converting string representations of dates into `datetime` objects, which enables date-based indexing and other time-series operations.

### 28. **Modifying Column Names**
```python
df.columns = [col.upper() for col in df.columns]  # Convert all column names to uppercase
```
- **columns**: Allows you to modify column names.
  - **Use Case**: Helpful for standardizing column names, especially when dealing with case-sensitive systems or when preparing data for presentation.

### 29. **Reordering Columns**
```python
df = df[['col3', 'col1', 'col2']]  # Reorder columns in a specific order
```
- **Reordering**: Directly specify the order of columns.
  - **Use Case**: This is useful when you need to rearrange columns for easier data analysis or to meet the format requirements of specific algorithms or data exports.

### 30. **Filtering Columns by Pattern**
```python
df_filtered = df.filter(like='pattern')  # Select columns that contain a specific pattern
```
- **filter()**: Subsets the DataFrame’s columns or rows based on labels.
  - **Important Parameters**: `items`, `like`, `regex`, `axis`
  - **Use Case**: Ideal for selecting columns that match a certain naming pattern, which can save time when dealing with large datasets with many columns.

### 31. **Getting Unique Values**
```python
unique_values = df['column'].unique()  # Get unique values in a column
```
- **unique()**: Returns the unique values in a column.
  - **Use Case**: Useful for identifying all distinct values in a column, which is important for data cleaning, exploratory data analysis, and reducing redundancy in datasets.
