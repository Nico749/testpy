# TIME SERIES GRAPH 
import matplotlib.pyplot as plt
import seaborn as sns
# plt.show shows the graph
years = range(2000,2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
# we can call the plot function multiple time to draw multiple graphs BUT all the dimensions 
# we want to plot need to have the same number of values
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.figure(figsize=(12, 6)) #NEED TO GO AT THE BEGINNING
sns.set_style("whitegrid")#PERSONALIZE THE GRID
plt.plot(years,apples, marker='o')
# with or, we only have the dots

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])

plt.plot(years,oranges, "or")
plt.show()

# SOME OF THE POSSIBLE CUSTOM OPTIONS 
# color or c: Set the color of the line (supported colors)
# linestyle or ls: Choose between a solid or dashed line
# linewidth or lw: Set the width of a line
# markersize or ms: Set the size of markers
# markeredgecolor or mec: Set the edge color for markers
# markeredgewidth or mew: Set the edge width for markers
# markerfacecolor or mfc: Set the fill color for markers
# alpha: Opacity of the plot
