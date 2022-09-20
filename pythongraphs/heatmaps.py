import matplotlib.pyplot as plt
import seaborn as sns
# flights_df is a matrix with one row for each month and one column for each year. 
# The values show the number of passengers (in thousands) that visited the airport in a specific month of a year.
flights_df = sns.load_dataset("flights").pivot("month", "year", "passengers")

plt.title("No. of Passengers (1000s)")
sns.heatmap(flights_df ,cmap='Blues')
plt.show()

# GENERATE A SUMMARY OF ALL THE GRAPHS AVAILABLE
# sns.pairplot(flowers_df, hue='species');