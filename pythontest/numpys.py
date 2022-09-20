import numpy as np
climate_data = np.array([[73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]])

# print(climate_data.shape)
weights = ([0.3, 0.2, 0.5])
# @ does the matrix mulitplication of the vectors
print(climate_data @ weights)
# [56.8 76.9 81.9 57.7 74.9]

import urllib.request

urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')

climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print(climate_data.shape)
