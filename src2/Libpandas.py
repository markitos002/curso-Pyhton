import pandas as pd

#pd = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

#Define a dictionary 'x'

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df  
print(df)    

x1= df['Salary'].mean()
print(x1)
x = df[['ID']]
print(x)

z = df[['Department','Salary','ID']]
print(z)