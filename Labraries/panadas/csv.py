import pandas as pd

df = pd.read_csv("C:\\Users\\cg636\\Documents\\python\\data_my.csv")
print(df.head())
print(df.tail())
print(df.haead(20))

#rows details
print(df.iloc())

#column and column datils name
print(df.info())

# just column name
print(df.column())

# number size check 
print(df.shape())

#  essencial mathmatical funcion
print(df.describe())

# minimum value findout
print(df(min['Applicatoion']))

#show total count 
print(df['ApplicantIncome'].count())

#  Output: Null Value Counts from Your Data ; all dataset
print(df.isnull().sum())


# Get rows with nulls in a specific column (e.g. LoanAmount)col
print(df[df['LoanAmount'].isnull()])

#  Rename specific column(s)
df.rename(columns={
    'ApplicantIncome': 'Income',
    'CoapplicantIncome': 'CoIncome'
}, inplace=True)

print(df.head())  # Now print the updated DataFrame
