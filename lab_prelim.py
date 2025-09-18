import pandas as pd

df = pd.read_csv('philippine_foundations_1100_with_duplicates_and_type.csv')
print(df.head())

# Fill ang mga missing
print(df['Owner/Founder'].isnull().sum())
df['Owner/Founder'] = df['Owner/Founder'].fillna('Unknown')
df['Assets_PHP'] = df['Assets_PHP'].fillna(df['Assets_PHP'].mean())
df['No_of_Members'] = df['No_of_Members'].fillna(df['No_of_Members'].mean())

# Standardize
df['Founding_Date'] = pd.to_datetime(df['Founding_Date']).dt.strftime('%Y-%m-%d')

# Remove duplicates
print(df.duplicated().sum())
df.drop_duplicates(inplace=True)
print(df.duplicated().sum())
print(len(df))

df.to_csv('cleaned_philippine_foundations.csv', index=False)

df_cleaned = pd.read_csv('cleaned_philippine_foundations.csv')
print(df_cleaned.head())

# DATA AGGREGATION
print('\n')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
sum_ass_by_city = df_cleaned.groupby('Location')['Assets_PHP'].sum()
max_ass_city = sum_ass_by_city.idxmax()
print('Location with highest assets:', max_ass_city)
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\n')

print('\n')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('These are the average number of members by location:')
avg_mem_by_city = df_cleaned.groupby('Location')['No_of_Members'].mean()
print(avg_mem_by_city)
print('The location with the largest average number of members is:', avg_mem_by_city.idxmax())
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\n')

print('\n')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('These are the number of foundations by decade:')
df_cleaned['Founding_Date'] = pd.to_datetime(df_cleaned['Founding_Date'])
df_cleaned['decade'] = (df_cleaned['Founding_Date'].dt.year // 10) * 10
foundations_by_decade = df_cleaned.groupby('decade')['Foundation_Name'].count()
print(foundations_by_decade)
print('The decade with the most foundations is:', foundations_by_decade.idxmax())
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('\n')
