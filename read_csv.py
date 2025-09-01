import pandas as pd

# 1
df = pd.read_csv('yes2.csv')
print(df.head())

# 2
print(df.isnull().sum())
mode = df['Address'].mode()[0]
df['Address'] = df['Address'].fillna(mode)
df['Date of Birth'] = df['Date of Birth'].ffill()

# 3
df.drop_duplicates(inplace=True)

# 4
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


# Step 5: Standardize and Normalize Data
for col in numeric_cols:
	if col in df.columns:
		mean = df[col].mean()
		std = df[col].std()
		mn = df[col].min()
		mx = df[col].max()
		df[col + '_std'] = (df[col] - mean) / std if std and std != 0 else 0
		df[col + '_norm'] = (df[col] - mn) / (mx - mn) if mx != mn else 0


# 6: Convert Data Types ---
df['Date of Birth'] = pd.to_datetime(df['Date of Birth'], errors='coerce')
if df['Total Projects'].notna().all():
	df['Total Projects'] = df['Total Projects'].astype('Int64')


# 7: Handle Categorical Data 
# simple code for Address and one-hot encode
df['Address'] = df['Address'].astype(str).str.strip()


# 8: Handle Text Data
df['Company Name'] = df['Company Name'].astype(str).str.strip().str.lower()
df['Company Name'] = df['Company Name'].str.replace('[^a-z0-9 ]', '', regex=True)


# 9: Filter and Clean Data ---
df = df.dropna(subset=numeric_cols)
df = df.drop_duplicates()


negative_assets = (df['Assets (PHP)'] < 0).sum() if 'Assets (PHP)' in df.columns else 0
if negative_assets:
	df = df[df['Assets (PHP)'] >= 0]

future_dobs = (df['Date of Birth'] > pd.Timestamp.today()).sum()
if future_dobs:
	df = df[df['Date of Birth'] <= pd.Timestamp.today()]

drop_cols = []
for c in numeric_cols:
	drop_cols.extend([c + '_std', c + '_norm'])
to_drop = [col for col in drop_cols if col in df.columns]
if to_drop:
	df = df.drop(columns=to_drop)
	print(f"Dropped columns: {', '.join(to_drop)}")

df['Date of Birth'] = df['Date of Birth'].ffill()

df.to_csv('yes2_clean.csv', index=False)
print(df.head())

