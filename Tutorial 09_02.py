# 2. For given data set display number of empty records, null values for each column. Identify columns that require data cleanuing and clean them as per your analysis.

import pandas as pd
import numpy as np

exam_data = {'Name' : ['Rima','Alok','Priyanka','Anandita','Priyanka'], 'Age' : [21,np.nan,19,20,18], 'Stream' : ['Maths','Commerce','Biology','Arts','Biology'], 'Per' : [58,92,90,np.nan,90],'Count':[1,2,3,4,5]}

labels = ['A','B','C','D','E']

df = pd.DataFrame(exam_data,index=labels)
print(df)

print("\nDescribe Dataframe\n")
print(df.describe())

print("\nRow where per is missing\n")
print(df[df['Per'].isnull()])

print("\nAll NaN from df\n")
print(df.isnull())

print("\nPrint all data excluding null\n")
print(df.dropna())

print("\nRemove a coulmn from the dataframe (here count)\n")
del df['Count']
print(df)

print("\nRemove duplicates\n")
df = df.drop_duplicates()
print(df)

print("\nReplace all NaN\n")
df = df.fillna(0)
print(df)

print("\nUpdate 4th record with per\n")
df.loc['D','Per']=45
print(df)
