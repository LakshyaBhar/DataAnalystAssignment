import pandas as pd

# Read the data from the CSV file
df = pd.read_csv('path/to/your/SBIN_Data.csv')

df['Datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

# Group by time and date
grouped = df.groupby([df['Datetime'].dt.time, df['Datetime'].dt.date])

# Calculate rank for each time slot based on the volume of the last 5 days
def calculate_rank(group):
    # Sort group by datetime in descending order
    group = group.sort_values(by='Datetime', ascending=False)
    
    # Get the volume of the last 5 days
    last_5_days_volume = group['Volume'].head(5)
    
    # Calculate rank
    group['Rank'] = last_5_days_volume.rank(ascending=False)
    
    return group

df_with_rank = grouped.apply(calculate_rank)

df_with_rank.drop(columns='Datetime', inplace=True)

print(df_with_rank)
