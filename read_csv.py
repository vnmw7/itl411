import pandas as pd


df = pd.read_csv('yes2.csv')
print(df.head())

print(df.isnull().sum())
mode = df['Address'].mode()[0]
df['Address'].fillna(mode, inplace=True)
df['Date of Birth'].fillna(method='ffill', inplace=True)


df.drop_duplicates(inplace=True)


numeric_cols = ['Assets (PHP)', 'Total Projects']
for col in numeric_cols:
	if col not in df.columns:
		continue

	df[col] = pd.to_numeric(df[col], errors='coerce')
	q1 = df[col].quantile(0.25)
	q3 = df[col].quantile(0.75)
	iqr = q3 - q1
	lower, upper = q1 - 1.5 * iqr, q3 + 1.5 * iqr
	before = len(df)
	df = df[(df[col] >= lower) & (df[col] <= upper)]
	after = len(df)
	print(f"Removed {before-after} outliers from '{col}' (kept {after}/{before})")


df.to_csv('yes2_clean.csv', index=False)

