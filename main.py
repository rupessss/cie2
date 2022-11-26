import pandas as pd
df= pd.read_excel(r'cie2.xlsx')
df.head(10)
import matplotlib.pyplot as plt
plt.hist('mpg',weights=1)
plt.scatter('mpg','weight(1000)')
plt.bar('Transmisson type',color='blue',height=0.5)
plt.xlabel("Transmission type")
plt.ylabel("types")
plt.show()
plt.boxplot([1,2,3,4,5])