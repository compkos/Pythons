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