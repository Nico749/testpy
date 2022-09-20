import matplotlib.pyplot as plt
import seaborn as sns
flowers_df = sns.load_dataset("iris") #default dataset on wikipedia irishflowers dataset
# print(flowers_df)
# print(flowers_df.species.unique())
plt.figure(figsize=(12, 6))
plt.title('Sepal Dimensions')

# # generates a scatterplot
# sns.scatterplot(x=flowers_df.sepal_length, 
#                 y=flowers_df.sepal_width, 
#                 hue=flowers_df.species,
#                 s=100);
# plt.show()
# histogram
import numpy as np

# Specifying the boundaries of each bin
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25));
plt.title("Distribution of Sepal Width")

# plt.show()
# plt.bar IS FOR THE BARCHART

# COMPLEX HISTOGRAM

setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
         bins=np.arange(2, 5, 0.25), 
         stacked=True);

plt.legend(['Setosa', 'Versicolor', 'Virginica']);
plt.show()
# BARCHART COMBINING DIFFERENT DATASETS AND SPECIFYING WHICH ONE GOES AT THE BOTTOM 
# plt.bar(years, apples)
# plt.bar(years, oranges, bottom=apples);