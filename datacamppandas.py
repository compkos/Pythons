# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict={'country':names,'drives_right':dr,'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars=pd.DataFrame(my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index=row_labels

# Print cars again
print(cars)

# Import the cars.csv data: cars
cars=pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars.iloc[[2,3,4]])

# Print out drives_right value of Morocco
print(cars.loc['MOR','drives_right'])

# Print sub-DataFrame
print(cars.loc[['MOR','RU'],['country','drives_right']])

# Print out drives_right column as Series
print(cars.loc[:,'drives_right'])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])

list1=[

[  'East South Central',  '             Alabama',       2570.0,           864.0,    4887681],
[  '           Pacific',  '              Alaska',       1434.0,           582.0,     735139],
[  '          Mountain',  '             Arizona',       7259.0,          2606.0,    7158024],
[  'West South Central',  '            Arkansas',       2280.0,           432.0,    3009733],
[  '           Pacific',  '          California',     109008.0,         20964.0,   39461588],
[  '          Mountain',  '            Colorado',       7607.0,          3250.0,    5691287],
[  '       New England',  '         Connecticut',       2280.0,          1696.0,    3571520],
[  '    South Atlantic',  '            Delaware',        708.0,           374.0,     965479],
[  '    South Atlantic',  'District of Columbia',       3770.0,          3134.0,     701547],
[  '    South Atlantic',  '             Florida',      21443.0,          9587.0,   21244317],
[  '    South Atlantic',  '             Georgia',       6943.0,          2556.0,   10511131],
[  '           Pacific',  '              Hawaii',       4131.0,          2399.0,    1420593],
[  '          Mountain',  '               Idaho',       1297.0,           715.0,    1750536],
[  'East North Central',  '            Illinois',       6752.0,          3891.0,   12723071],
[  'East North Central',  '             Indiana',       3776.0,          1482.0,    6695497],
[  'West North Central',  '                Iowa',       1711.0,          1038.0,    3148618],
[  'West North Central',  '              Kansas',       1443.0,           773.0,    2911359],
[  'East South Central',  '            Kentucky',       2735.0,           953.0,    4461153],
[  'West South Central',  '           Louisiana',       2540.0,           519.0,    4659690],
[  '       New England',  '               Maine',       1450.0,          1066.0,    1339057],
[  '    South Atlantic',  '            Maryland',       4914.0,          2230.0,    6035802],
[  '       New England',  '       Massachusetts',       6811.0,         13257.0,    6882635],
[  'East North Central',  '            Michigan',       5209.0,          3142.0,    9984072],
[  'West North Central',  '           Minnesota',       3993.0,          3250.0,    5606249],
[  'East South Central',  '         Mississippi',       1024.0,           328.0,    2981020],
[  'West North Central',  '            Missouri',       3776.0,          2107.0,    6121623],
[  '          Mountain',  '             Montana',        983.0,           422.0,    1060665],
[  'West North Central',  '            Nebraska',       1745.0,           676.0,    1925614],
[  '          Mountain',  '              Nevada',       7058.0,           486.0,    3027341],
[  '       New England',  '       New Hampshire',        835.0,           615.0,    1353465],
[  '      Mid-Atlantic',  '          New Jersey',       6048.0,          3350.0,    8886025],
[  '          Mountain',  '          New Mexico',       1949.0,           602.0,    2092741],
[  '      Mid-Atlantic',  '            New York',      39827.0,         52070.0,   19530351],
[  '    South Atlantic',  '      North Carolina',       6451.0,          2817.0,   10381615],
[  'West North Central',  '        North Dakota',        467.0,            75.0,     758080],
[  'East North Central',  '                Ohio',       6929.0,          3320.0,   11676341],
[  'West South Central',  '            Oklahoma',       2823.0,          1048.0,    3940235],
[  '           Pacific',  '              Oregon',      11139.0,          3337.0,    4181886],
[  '      Mid-Atlantic',  '        Pennsylvania',       8163.0,          5349.0,   12800922],
[  '       New England',  '        Rhode Island',        747.0,           354.0,    1058287],
[  '    South Atlantic',  '      South Carolina',       3082.0,           851.0,    5084156],
[  'West North Central',  '        South Dakota',        836.0,           323.0,     878698],
[  'East South Central',  '           Tennessee',       6139.0,          1744.0,    6771631],
[  'West South Central',  '               Texas',      19199.0,          6111.0,   28628666],
[  '          Mountain',  '                Utah',       1904.0,           972.0,    3153550],
[  '       New England',  '             Vermont',        780.0,           511.0,     624358],
[  '    South Atlantic',  '            Virginia',       3928.0,          2047.0,    8501286],
[  '           Pacific',  '          Washington',      16424.0,          5880.0,    7523869],
[  '    South Atlantic',  '       West Virginia',       1021.0,           222.0,    1804291],
[  'East North Central',  '           Wisconsin',       2740.0,          2167.0,    5807406],
[  '          Mountain',  '             Wyoming',        434.0,           205.0,     577601]]

homelessness=pd.DataFrame(list1)
homelessness.columns = ['region','state','individuals',  'family_members','state_pop']

# Print the head of the homelessness data
print(homelessness.head())

# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

# Sort homelessness by individual
homelessness_ind = homelessness.sort_values("individuals")

# Print the top few rows
print(homelessness_ind.head())

# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members',ascending=False)

# Print the top few rows
print(homelessness_fam.head())

# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(["region","family_members"],ascending=[True,False])

# Print the top few rows
print(homelessness_reg_fam.head())

# Select the individuals column
individuals = homelessness['individuals']

# Print the head of the result
print(individuals.head())

# Select the state and family_members columns
state_fam = homelessness[['individuals','state']]

# Print the head of the result
print(state_fam.head())

# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[homelessness['individuals']>10000]

# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[homelessness['region'].str.strip()=="Mountain"]

# See the result
print(mountain_reg)

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['region'].str.strip()=="Pacific") & (homelessness['family_members']<1000)]

# See the result
print(fam_lt_1k_pac)

# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[homelessness['region'].str.strip().isin(["South Atlantic","Mid-Atlantic"])]

# See the result
print(south_mid_atlantic)


# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]

# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[homelessness['state'].str.strip().isin(canu)]

# See the result
print(mojave_homelessness)


# Add total col as sum of individuals and family_members
homelessness['total']=homelessness['individuals']+homelessness['family_members']

# Add p_individuals col as proportion of individuals
homelessness['p_individuals']=homelessness['individuals']/homelessness['total']

# See the result
print(homelessness)


# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']
# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[homelessness["indiv_per_10k"]>20]

# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k',ascending=False)

# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state','indiv_per_10k']]

# See the result
print(result)

sales_list=[[1    ,'A'           ,1 ,'2010-02-05'      ,24924.50       ,False,          5.728                 ,0.679         ,8.106],
[1    ,'A'           ,1 ,'2010-03-05'      ,21827.90       ,False,          8.056                 ,0.693         ,8.106],
[1    ,'A'           ,1 ,'2010-04-02'      ,57258.43       ,False,         16.817                 ,0.718         ,7.808],
[1    ,'A'           ,1 ,'2010-05-07'      ,17413.94       ,False,         22.528                 ,0.749         ,7.808],
[1    ,'A'           ,1 ,'2010-06-04'      ,17558.09       ,False,         27.050                 ,0.715         ,7.808],
[ 2    ,'A'           ,1 ,'2010-02-05'      ,35034.06       ,False,          4.550                 ,0.679         ,8.324],
[ 4    ,'A'           ,1 ,'2010-02-05'      ,38724.42       ,False,          6.533                 ,0.686         ,8.623],
[ 6    ,'A'           ,1 ,'2010-02-05'      ,25619.00       ,False,          4.683                 ,0.679         ,7.259],
[10    ,'B'           ,1 ,'2010-02-05'      ,40212.84       ,False,         12.411                 ,0.782         ,9.765]

]

sales=pd.DataFrame(sales_list)
sales.columns = ['store', 'type','department','date',  'weekly_sales',  'is_holiday',  'temperature_c',  'fuel_price_usd_per_l',  'unemployment']
print(sales)

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(subset=["store","type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(subset=["store","department"])
print(store_depts.head())

# Subset the rows that are holiday weeks and drop duplicate dates
holiday_dates = sales[sales['is_holiday']==True].drop_duplicates(subset="date")

# Print date col of holiday_dates
print(holiday_dates['date'])

storelist=[[ 1          ,'A'],
[ 2          ,'A'],
[ 4          ,'A'],
[ 6          ,'A'],
[10          ,'B'],
[13          ,'A'],
[14          ,'A'],
[19          ,'A'],
[20          ,'A'],
[27          ,'A'],
[31          ,'A'],
[39          ,'A']]

stores=pd.DataFrame(storelist)
stores.columns = ['store_num', 'store_type']
store_counts = stores["store_type"].value_counts()
print(store_counts)

departments_list=[[ 1             ,  1],
[ 1             ,  2],
[ 1             ,  3],
[ 1             ,  4],
[ 1             ,  5],
[39             , 95],
[39             , 96],
[39             , 97],
[39             , 98],
[39             , 99]]

departments=pd.DataFrame(departments_list)
departments.columns = ['store_num','department_num']
# Count the number of stores of each type                                                
print(departments )                                                                      
store_counts = stores["store_type"].value_counts()                                       
print(store_counts)                                                                      
                                                                                         
# Get the proportion of stores of each type                                              
store_props = stores["store_type"].value_counts(normalize=True)                          
print(store_props)                                                                       
                                                                                         
# Count the number of each department number and sort                                    
dept_counts_sorted = departments['department_num'].value_counts(sort=True)               
print(dept_counts_sorted)                                                                
                                                                                         
# Get the proportion of departments of each number and sort                              
dept_props_sorted = departments['department_num'].value_counts(sort=True, normalize=True)
                                                                                       
# Count the number of each department number and sort                                    
dept_counts_sorted = departments['department_num'].value_counts(sort=True)               
print(dept_counts_sorted)                                                                
                                                                                         
# Get the proportion of departments of each number and sort                              
dept_props_sorted = departments['department_num'].value_counts(sort=True, normalize=True)

# Calc total weekly sales
sales_all = sales['weekly_sales'].sum()

# Subset for type A stores, calc total weekly sales
sales_A = sales[sales["type"] == "A"]['weekly_sales'].sum()

# Subset for type B stores, calc total weekly sales
sales_B = sales[sales["type"] == "B"]['weekly_sales'].sum()

# Subset for type C stores, calc total weekly sales
sales_C = sales[sales["type"] == "C"]['weekly_sales'].sum()

# Get proportion for each type
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# Group by type; calc total weekly sales
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Get proportion for each type
sales_propn_by_type = sales_by_type / sum(sales_by_type)
print(sales_propn_by_type)

# From previous step
sales_by_type = sales.groupby("type")["weekly_sales"].sum()

# Group by type and is_holiday; calc total weekly sales
sales_by_type_is_holiday = sales.groupby(["type","is_holiday"])["weekly_sales"].sum()
print(sales_by_type_is_holiday)

# Import NumPy with the alias np
import numpy as np

# For each store type, aggregate weekly_sales: get min, max, mean, and median
sales_stats = sales.groupby("type")["weekly_sales"].agg([np.min, np.max, np.mean, np.median])

# Print sales_stats
print(sales_stats)

# For each store type, aggregate unemployment and fuel_price_usd_per_l: get min, max, mean, and median
unemp_fuel_stats = sales.groupby("type")[["unemployment", "fuel_price_usd_per_l"]].agg([np.min, np.max, np.mean, np.median])

# Print unemp_fuel_stats
print(unemp_fuel_stats)

# Pivot for mean weekly_sales for each store type
mean_sales_by_type = sales.pivot_table(values=
"weekly_sales", index="type")

# Print mean_sales_by_type
print(mean_sales_by_type)

# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values="weekly_sales"
, index="type", aggfunc=[np.mean, np.median])

# Print mean_med_sales_by_type
print(mean_med_sales_by_type)

# Pivot for mean weekly_sales by store type and holiday 
mean_sales_by_type_holiday = sales.pivot_table(values="weekly_sales"
, index="type", columns='is_holiday')

# Print mean_sales_by_type_holiday
print(mean_sales_by_type_holiday)

# Print mean weekly_sales by department and type; fill missing values with 0
print(sales.pivot_table(values="weekly_sales"
, index="department", columns="type",fill_value=0))

# Print the mean weekly_sales by department and type; fill missing values with 0s; sum all rows and cols
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0, margins=True))


# Create the list of DataFrames: medal_list
names = ['United States', 'Soviet Union', 'United Kingdom', 'France ', 'Germany']
bronzemet = [1052.0, 584.0, 505.0, 475.0, 454.0]
my_dict={'Country':names,'Total':bronzemet}
bronze1=pd.DataFrame(my_dict)
bronse2=bronze1.pivot_table(values="Total"
, index="Country")
print(bronse2)
silvermet = [1195.0, 627.0, 591.0, 461.0, 394.0]
my_dict={'Country':names,'Total':silvermet}
silver1=pd.DataFrame(my_dict)
silver2=silver1.pivot_table(values="Total"
, index="Country")
print(silver2)
goldmet = [2088.0, 838.0, 498.0, 460.0, 407.0]
my_dict={'Country':names,'Total':goldmet}
gold1=pd.DataFrame(my_dict)
gold2=gold1.pivot_table(values="Total"
, index="Country")
print(gold2)




temp_list=[
['2000-01-01'  ,'Abidjan'  ,'Cote D''Ivoire'      ,27.293],
['2000-02-01'  ,'Abidjan'  ,'Cote D''Ivoire'      ,27.685],
['2000-03-01'  ,'Abidjan'  ,'Cote D''Ivoire'      ,29.061],
['2000-04-01'  ,'Abidjan'  ,'Cote D''Ivoire'      ,28.162],
['2000-05-01'  ,'Abidjan'  ,'Cote D''Ivoire'      ,27.547],
['2013-05-01'  ,   'Xian'          ,'China'      ,18.979],
['2013-06-01'  ,   'Xian'          ,'China'      ,23.522],
['2013-07-01'  ,   'Xian'          ,'China'      ,25.251],
['2013-08-01'  ,   'Xian'          ,'China'      ,24.528],
['2013-09-01'  ,   'Xian'          ,'China'      ,     0]]

temperatures=pd.DataFrame(temp_list)
temperatures.columns = ['date','city','country','avg_temp_c']

# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index("city")

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))

# Make a list of cities to subset on
cities = ["Xian", "Abidjan"]

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level=['city']))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=['country','city'],ascending=[True,False]))

# Sort the index of temperatures_ind
temperatures_srt = temperatures_ind.sort_index()

# Subset rows from Pakistan to Russia
print(temperatures_srt.loc['Pakistan':'Russia'])

# Try to subset rows from Lahore to Moscow
print(temperatures_srt.loc['Lahore':'Moscow'])

# Subset rows from Pakistan, Lahore to Russia, Moscow
print(temperatures_srt.loc[('Pakistan','Lahore'):('Russia','Moscow')])

# Subset rows from India, Hyderabad to Iraq, Baghdad
print(temperatures_srt.loc[('India', 'Hyderabad' ):('Iraq','Baghdad')])

# Subset columns from date to avg_temp_c
print(temperatures_srt.loc[:,"date":"avg_temp_c"])

# Subset in both directions at once
print(temperatures_srt.loc[('India', 'Hyderabad' ):('Iraq','Baghdad'),"date":"avg_temp_c"])