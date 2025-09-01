import pandas as pd


df = pd.read_csv('yes2.csv')
print(df.head())

print(df.isnull().sum())
mode = df['Address'].mode()[0]
df['Address'].fillna(mode, inplace=True)
df['Date of Birth'].fillna(method='ffill', inplace=True)




