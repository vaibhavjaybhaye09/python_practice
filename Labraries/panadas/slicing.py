import pandas as pd

# Creating a series (corrected)
data = pd.Series([20, 10, 30, 40, 402], index=['a', 'b', 'c', 'd', 'e'])

# Slicing by position
print("Slicing by position (1:3):")
print(data[1:3])  # outputs elements at position 1 and 2 -> b and c

# Slicing by label
print("\nSlicing by label ('b' to 'd'):")
print(data['b':'d'])  # includes both start and end labels -> b, c, d

# Creating a DataFrame
data = {
    'Name': ['Vaibhav', 'AKash', 'vaibhavi'],
    'Age': [22, 23, 22],
    'city': ['pune', 'B', 'Ccc']
}
df = pd.DataFrame(data)

# Displaying first two rows using iloc
print("\nDataFrame rows 0 to 1 (iloc[0:2]):")
print(df.iloc[0:1])

