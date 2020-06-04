#https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot#stacked-bar-plot-with-group-by-normalized-to-100

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

df = pd.DataFrame({
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'gender':['M','F','M','M','M','F','M'],
    'state':['california','dc','california','dc','california','texas','texas'],
    'num_children':[2,0,0,3,2,1,4],
    'num_pets':[5,1,0,5,2,2,3]
})

# a scatter plot comparing num_children and num_pets
df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
plt.show()

# a simple line plot
df.plot(kind='bar',x='name',y='age')
plt.show()


ax = plt.gca()

df.plot(kind='line',x='name',y='num_children',ax=ax)
df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

plt.show()

df.plot(kind='bar',x='name',y='age')

# the plot gets saved to 'output.png'
plt.savefig('output.png')

df.groupby('state')['name'].nunique().plot(kind='bar')
plt.show()

df.assign(dummy = 1).groupby(
  ['dummy','state']
).size().to_frame().unstack().plot(kind='bar',stacked=True,legend=False)

plt.title('Number of records by State')

# other it'll show up as 'dummy' 
plt.xlabel('state')

# disable ticks in the x axis
plt.xticks([])

# fix the legend
current_handles, _ = plt.gca().get_legend_handles_labels()
reversed_handles = reversed(current_handles)

labels = reversed(df['state'].unique())

plt.legend(reversed_handles,labels,loc='lower right')
plt.show()

df.assign(dummy = 1).groupby(
  ['dummy','state']
).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()
).to_frame().unstack().plot(kind='bar',stacked=True,legend=False)

# or it'll show up as 'dummy' 
plt.xlabel('state')

# disable ticks in the x axis
plt.xticks([])

# fix the legend or it'll include the dummy variable
current_handles, _ = plt.gca().get_legend_handles_labels()
reversed_handles = reversed(current_handles)
correct_labels = reversed(df['state'].unique())

plt.legend(reversed_handles,correct_labels)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.show()

df.groupby(['state','gender']).size().unstack().plot(kind='bar',stacked=True)
plt.show()

df.groupby(['gender','state']).size().unstack().plot(kind='bar',stacked=True)
plt.show()

df.groupby(['gender','state']).size().groupby(level=0).apply(
    lambda x: 100 * x / x.sum()
).unstack().plot(kind='bar',stacked=True)

plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
plt.show()

df[['age']].plot(kind='hist',bins=[0,20,40,60,80,100],rwidth=0.8)
plt.show()


df = pd.DataFrame({
    'name':[
        'john','lisa','peter','carl','linda','betty'
    ],
    'date_of_birth':[
        '01/21/1988','03/10/1977','07/25/1999','01/22/1977','09/30/1968','09/15/1970'
    ]
})

df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], infer_datetime_format=True)

plt.clf()
df['date_of_birth'].map(lambda d: d.month).plot(kind='hist')
plt.show()

x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)

# create figure and axes
fig, axes = plt.subplots(1,2)

ax1 = axes[0]
ax2 = axes[1]

# just plot things on each individual axes
ax1.scatter(x,y,c='red',marker='+')
ax2.bar(x,y)


x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)

# create figure and axes
fig, axes = plt.subplots(2,1)

ax1 = axes[0]
ax2 = axes[1]

# just plot things on each individual axes
ax1.scatter(x,y,c='red',marker='+')
ax2.bar(x,y)


x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)

# plt.subplots returns an array of arrays. We can
# directly assign those to variables directly
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

# just plot things on each individual axes
ax1.scatter(x,y,c='red',marker='+')
ax2.bar(x,y)
ax3.scatter(x,y,marker='x')
ax4.barh(x,y)

plt.show()


df = pd.DataFrame({
    'string_col':['foo','bar','baz','quux','bum','bam','blah'],
    'x':[10,20,30,40,20,10,30],
    'y':[1,3,1,1,4,5,8]
})

# plt.subplots returns an array of arrays. We can
# directly assign those to variables directly
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

# bar plot for column 'x'
df.plot(y='x', kind='bar', ax=ax1)

# horizontal bar plot for column 'y'
df.plot(y='y', kind='bar', ax=ax2)

# both columns in a scatter plot
df.plot('x','y', kind='scatter', ax=ax3)

# to have two lines, plot twice in the same axis
df.plot(y='x', kind='line', ax=ax4)
df.plot(y='y', kind='line', ax=ax4)

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

# sample data
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)

# plot individual subplots
ax1.bar(x,y)
ax2.bar(x,y)
ax3.scatter(x,y)
ax4.plot(x)

ax4.set_title('This is Plot 4',size=14)



# sample data
x = np.linspace(0.0,100,50)
y = np.random.uniform(low=0,high=10,size=50)

# plt.subplots returns an array of arrays. We can
# directly assign those to variables directly
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2)

# just plot things on each individual axes
ax1.scatter(x,y,c='red',marker='+')
ax2.bar(x,y)
ax3.scatter(x,y,marker='x')
ax4.barh(x,y)

# here, set the width and the height between the subplots
# the default value is 0.2 for each
plt.subplots_adjust(wspace=0.50, hspace=1.0)


fig, ((ax1,ax2)) = plt.subplots(1,2)

# sample data in different magnitudes
x = np.linspace(0.0,100,50)
y1 = np.random.normal(loc=10, scale=2, size=10)
y2 = np.random.normal(loc=20, scale=2, size=10)

# plot in each subplot
ax1.plot(y1)
ax2.plot(y2)

ax1.set_ylim(0,25)
ax2.set_ylim(0,25)


plt.clf()

# generate sample data for this example
xs = [1,2,3,4,5,6,7,8,9,10,11,12]
ys_bars = np.random.normal(loc=3.0,size=12)
ys_lines = np.random.normal(loc=5.0,size=12,scale=0.5)

# this is the axis on the left
ax1=plt.gca()

ax1.bar(xs,ys_bars,color='green')

# order is important when setting ticks.
# Ticks must be set after the plot has been drawn
ax1.set_yticks(np.arange(0,11,1))

# define the number of ticks
NUM_TICKS=11

# change the tick locator for this axis and set the desired number of ticks
ax1.yaxis.set_major_locator(plt.LinearLocator(numticks=NUM_TICKS))

# create the 'twin' axis on the right
ax2=ax1.twinx()

# plot the same numbers but multiplied by 20
ax2.plot(xs,ys_lines*20,color='red')

# set the ticks for the twin axis
ax2.set_yticks(np.arange(0,101,10))

# change the tick locator for this axis and set the desired number of ticks
ax2.yaxis.set_major_locator(plt.LinearLocator(numticks=NUM_TICKS))

# set ticks for the common x axis (bottom)
ax2.xaxis.set_ticks(xs)

