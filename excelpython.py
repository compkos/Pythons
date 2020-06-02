import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.ExcelFile('units.xlsx')
print(data.sheet_names)

sales = data.parse('Units')
# Print dimensions and glimpse
print(sales.shape)
print(sales.head(5))

print(sales.info())
print(sales.describe())

print(sales['InOut'].unique())

sales['Departure_YM'] = sales['Departure Date'].dt.strftime('%Y-%m')

sales['InOutDescr'] = sales['InOut'].replace({1: "In", 
-1: "Out", 0:""})


sales_nogroupsupplier=sales[sales['Group Supplier'].isnull()==True]

print(sales_nogroupsupplier[['Supplier','Group Supplier','Reference No']])

sales_by_month = sales[['Departure_YM','Reservations']].groupby('Departure_YM').sum().reset_index()

print(sales_by_month)



#sns.barplot(x = 'Departure_YM', y = 'Reservations', #data = sales_by_month)
#plt.xlabel("Month")
#plt.ylabel("Units")
#plt.title("Units per Month")
#plt.show()



#sns.lineplot(x = 'Departure_YM', y = 'Reservations', #data = sales_by_month)
#plt.figure(figsize=(18, 6))
#plt.xticks(rotation=45)
#plt.xlabel("Year/Month")
#plt.ylabel("Units")
#plt.title("Units over the years and months")
#plt.show()


sales_by_month_inout = sales[sales['InOutDescr']!=""][['Departure_YM','InOutDescr','Reservations']].groupby(['Departure_YM','InOutDescr']).sum().reset_index()

print(sales_by_month_inout)

sns.barplot(x = 'Departure_YM', y = 'Reservations', hue = "InOutDescr", data = sales_by_month_inout)
plt.xlabel("Year/Month")
plt.ylabel("Units")
plt.title("Year/Month & InOut Units")

plt.show()
