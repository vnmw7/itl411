import pandas as pd

df = pd.read_csv('yes2_clean.csv')
print(df.head())

company_assets = df[['Company Name', 'Assets (PHP)']]
company_idx = company_assets['Assets (PHP)'].idxmax()
company_name = company_assets.loc[company_idx, 'Company Name']

print(f"COMPANY WITH HIGHEST ASSETS: {company_name}")

print('NUM OF COMPANIES WITH MORE THAN 10 PROJECTS:', (df['Total Projects'] > 10).sum())

print('NUM OF COMPANIES IN CEBU:', (df['Address'] == 'Cebu City').sum())

company_idx = df['Total Projects'].idxmax()
company_name = df.loc[company_idx, 'Company Name']

print(f"MOST NUMBER OF PROJECTS: {company_name} with {df.loc[company_idx, 'Total Projects']}")


# additional notes:
# gamit .mean() .median() .mode() sa dataframe columns
# pd.concat([df1, df2], axis=1) to combine dataframes