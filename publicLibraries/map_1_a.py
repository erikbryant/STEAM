import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Load your CSV data
csv_file = 'your_data.csv'
df = pd.read_csv(csv_file)

# Print the first few rows of the DataFrame to understand its structure
print(df.head())

# Ensure you have a column in your CSV that matches the county names in the shapefile
# For simplicity, let's assume the column is named 'county'

# Load the US counties shapefile
# You can download it from: https://www2.census.gov/geo/tiger/GENZ2019/shp/cb_2019_us_county_20m.zip
shapefile = 'path_to_your_shapefile/cb_2019_us_county_20m.shp'
gdf = gpd.read_file(shapefile)

# Print the first few rows of the GeoDataFrame to understand its structure
print(gdf.head())

# Merge the GeoDataFrame with your DataFrame on the county column
merged = gdf.merge(df, left_on='NAME', right_on='county', how='left')

# Plot the merged data
fig, ax = plt.subplots(1, 1, figsize=(15, 15))
merged.boundary.plot(ax=ax, linewidth=1)
merged.plot(column='your_data_column', ax=ax, legend=True,
            legend_kwds={'label': "Your Data Label",
                         'orientation': "horizontal"})
plt.title('Your Title Here')
plt.show()