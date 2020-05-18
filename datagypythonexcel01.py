import pandas as pd
sales = pd.read_excel('pythonexcel.xlsx', sheet_name = 'sales')
states = pd.read_excel('pythonexcel.xlsx', sheet_name = 'states')
print(sales.head())
print(states.head())
sales['MoreThan500'] = ['Yes' if x > 500 else 'No' for x in sales['Sales']]
print(sales.head())
sales = pd.merge(sales, states, how='left', on='City')
print(sales.head())
print(sales.pivot_table(index = 'City', values = 'Sales', aggfunc = 'sum'))
