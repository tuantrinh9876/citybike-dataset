import pandas as pd
# Read file csv
df_bikedata = pd.read_csv('raw_data.csv')

# Drop column, 
df_bikedata = df_bikedata.drop('Trip Duration', 1)
df_bikedata = df_bikedata.drop('Birth Year', 1)
df_bikedata = df_bikedata.drop('Start Time', 1)
df_bikedata = df_bikedata.drop('Stop Time', 1)

# Remove duplicates
df_bikedata.drop_duplicates()
df_bikedata_duplicates = df_bikedata[df_bikedata.duplicated()]

# Check null values
print(df_bikedata.isnull().sum())
df_bikedata.dropna()

# Write to new file
df_bikedata.to_csv('bikedata_cleaned.csv')



