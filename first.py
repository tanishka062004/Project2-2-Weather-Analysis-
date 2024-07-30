import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv('climate_data.csv')

# Check for missing values
print(df.isnull().sum())

# Drop rows with any missing values
df.dropna(inplace=True)

# Forward fill missing values
df.ffill(inplace=True)

# Check for duplicates
print(df.duplicated().sum())

# Drop duplicates
df.drop_duplicates(inplace=True)


# Save to a new CSV file
df.to_csv('cleaned_climate_data.csv', index=False)

df = pd.read_csv('cleaned_climate_data.csv')
#Calculate correlation matrix:

# Calculate the correlation matrix
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Drop the date column for correlation matrix calculation
df_numeric = df.drop(columns=['Date'])
# Calculate the correlation matrix
unwanted_columns = [
        'Maximum rain per minute',
        'Maximum temperature (Â°F)',
        'Minimum temperature (Â°F)',
        'Maximum humidity (%)',
        'Minimum humidity (%)',
        'Maximum pressure',
        'Minimum pressure',
        'Maximum windspeed (mph)',
        'Maximum gust speed (mph)',
        'Maximum heat index (Â°F)'
    ]
df_numeric_monthly = df.drop(columns=unwanted_columns, errors='ignore')

# Calculate the correlation matrix
correlation_matrix = df_numeric_monthly.corr()

# Plot the correlation heatmap
plt.figure(figsize=(15, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Monthly Aggregated Correlation Heatmap')
plt.show()


