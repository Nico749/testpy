import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
df = pd.DataFrame({'points': [25, 12, 15, 14, 19, 23, 25, 29],
                   'assists': [5, 7, 7, 9, 12, 9, 9, 4],
                   'rebounds': [11, 8, 10, 6, 6, 5, 9, 12],
                   'blocks': [4, 7, 7, 6, 5, 8, 9, 10],
                   'months':[1,2,3,4,5,6,7,8]})
df_points = df[["points"]]
df_months = df[['months']]
df_assist = df.iloc[:, [2]]


plt.figure(figsize=(10, 5)) 
# style the graph 
sns.set(rc={'axes.facecolor':'#f2564b','axes.grid' : False})


plt.plot(df_months,df_points, color="white")
plt.plot(df_months,df_assist)
plt.xlabel('Month')
plt.ylabel('Points/Assists')

plt.title("Avrage Points and assists during season")
plt.legend(['Points', 'Assist'])

plt.show()
