import pandas as pd
import numpy as np

exam_data = {'Name' : ['Rima','Alok','Anandita','Priyanka'], 'Age' : [21,19,20,18], 'Stream' : ['Maths','Commerse','Arts','Biology'], 'Per' : [58,92,85,30]}

#Labeling each row later in the dataframe
labels = ['A','B','C','D']

df = pd.DataFrame(exam_data,index=labels)
print(df)

# i)Print all coumns where name of the student begins with letter 'A' and percentage is greater than 85 using index attribute

print("/nName begins with A and per > 85\n")
print(df[(df['Name'].str[0]=='A') & (df['Per']>85)])

# & is for 'and' 
# | if for 'or'

print("\nPer >= 85\n")
print(df[(df['Per']>=85)])

print("\nDisplay age ans percentage of first and second row using loc\n")
result=df.loc['A' : 'B' , ['Age' , 'Per']]
print(result)

print("\nDisplay age ans percentage of first and second row using iloc\n")
result=df.iloc[0:2,[1,3]]
print(result)

# ii) Print the age column using loc and print the average age
result = df.loc[ : , 'Age']
print("\nPrint the age column using loc\n")
print(result)
print("\nAverage of age : ",df['Age'].mean())

result = df.iloc[ : , 1]
print("\nPrint the age column using iloc\n")
print(result)

# iii) Print 0th and 2th index column using iloc function
result = df.iloc[ : , [0,2]]
print("\nPrinting the 1st and 3rd column using iloc\n")
print(result)

# iv) Update the percentage column between 0 and 1
print("\nUpdate per of row 0 and 1\n")
print(df)
def.loc[['A','B'],'Per']=[56,78]
print("\nAfter Updating\n")
print(df)
