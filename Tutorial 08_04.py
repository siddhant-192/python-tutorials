import numpy as np

c=[25,30.5,35,80,25.4]
cvalues=np.array(c)

print("Celsius : ",cvalues)

print("Fahrenheit : ",np.round(9*cvalues/5+32,2))
