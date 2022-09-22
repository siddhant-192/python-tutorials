import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('data.csv')
print(df)

colors=['red','blue','green','black','orange','yellow','purple']

# i) scatter plot of two columns  - name and num_children, num_children and num_pets

df.plot(kind="scatter" , x='name' , y='num_children' , color=colors)

df.plot(kind="scatter" , x='num_children' , y='num_pets' , color=colors)

# ii) Bar Chart
df.plot(kind="bar" , x = "name" , y = "age")
plt.show()