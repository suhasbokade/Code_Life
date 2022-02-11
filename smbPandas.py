# pandas

import pandas as pd

# Series:-


l = [1, 2, 3, 4, 5, 6]
indexes = ["A", "B", "C", "D", "E", "F"]

s = pd.Series(l, index=indexes)
print(s)
print(type(s))

print(s["D"])

d = {
    "A": "Apple",
    "B": "Bat",
    "C": "Cat"
}
s = pd.Series(d)
print(s)

# Dataframe:-

d = {
    "name": ["C", "CPP", "JAVA", "PYTHON", "HTML"],
    "Year": [1980, 1987, 1970, 2001, 2002],
    "Use": [23, 56, 78, 34, 56]
}
df = pd.DataFrame(d)
print(df)

print(df.loc[2])  # accessing rows
print(df["name"])  # accessing column

# Indexing & Slicing:-

print("Slicing\n\n")
print(df.iloc[0:4])

# Print only Name of first 4 rows

print("\n\nname of 4 rows: ")
print(df.loc[0:3, "name"])  # upper limit is considered while slicing

print("\n\n\nPrint name and use column")
print(df[["name","Use"]])

# Dataframe function:-
print("\n\nInfo()\n\n")
print(df.info())

# Describe function:-

print("\n\nDescribe()\n\n")
print(df.describe())


# Unique Function:-

print("\n\nUnique()\n")
print(df["Year"].unique())

print("\n\nisnull()\n\n")
print(df.isnull().sum())


# Arithmatic operation on Integer column:-

print('\nSum of years: ',df["Year"].sum())
print("Mean of years: ",df["Year"].mean())
print("Median of years: ",df["Year"].median())
print("Std Dev of years: ",df["Year"].std())
print("Max of years: ",df["Year"].max())
print("Min of years: ",df["Year"].min())

# Filtering the Data:-

print("\n\nFiltering the Data:\n")
print(df[df["Use"]>50])               # All records with Use greater than 50

print("\n\n")
print(df[df["Year"]==2002])           # All lang develoved in year 2002

print("\n\nHead():\n")
print(df.head())                      # Print only first 5 record

print("\n\nhead(2):\n")
print(df.head(2))                     # Print starting 2 record

print("\n\ntail():\n")
print(df.tail())                      # Print only last 5 record

print("\n\ntail(2):\n")
print(df.tail(2))                     # Print last 2 record

# Cleaning the Data:=
# 1. Deleting empty cells--

new_df=df.dropna()                  # Return a new dataframe with empty cells deleted
df.dropna(inplace=True)             # Will change the original dataframe and not return new

# 2. Fill the empty record--

new_df=df.fillna()                  # Return a new dataframe with empty cells filled with given value
df.fillna(inplace=True)             # Will change the original dataframe and not return new

# 3. Fill only given column--

df["Year"].fillna(0,inplace=True)   # Only Year column will be changed and empty will become 0

avg=df["Use"].mean()
df["Use"].fillna(avg,inplace=True)  # Empty cells will be filled with average value only in "Use" column

# 4. Remove duplicate records--

print("\n\nDuplicate check:\n")
print(df.duplicated())              # It return True for rows containing duplicate value

print("\n\nOriginal Dataframe:\n")
print(df)

df.drop_duplicates(inplace=True)
print("\n\nDuplicate Removed Dataframe:\n")
print(df)

# 5. Deleting a Column--

print("\n\nDataframe after delection:\n")
new_df=df.drop(["Use"],axis=1)           # Axis=1  indicate you are trying to delete a column
print(new_df)

# 6. Delection of Row--

print("\n\nDataframe after delection of Row:\n")
new_df=df.drop([2,4])                    # Axis=0 is default value and indicate you are trying to delete a row
print(new_df)