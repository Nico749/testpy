import numpy as np
import urllib.request
# retrieve a file with the url and save it with a new format 
urllib.request.urlretrieve(
    'https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')
# climate_data contains temperature,rainfall,humidity for different locations
climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
# print(climate_data.shape)
# weight that every factor has on the total yield
weights = np.array([0.3, 0.2, 0.5])
yields = climate_data@weights
# concatenate the results obtained in a new file
# the argument axis=1 specifies the dimension for concatenation.
# The arrays should have the same number of dimensions, and the same length along each except the dimension used for concatenation. We use the np.reshape function to change the shape of yields from (10000,) to (10000,1)
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)
print(climate_results)
# save the results in a new file
np.savetxt('climate_results_apples.txt', 
           climate_results, 
           fmt='%.2f', 
           delimiter=',',
           header='temperature,rainfall,humidity,yeild_apples', 
           comments='')