import pandas as pd
from urllib.request import urlretrieve
iris='http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
urlretrieve(iris)
df=pd.read_csv(iris,sep=',')
print(df)
print(df.head())
col_names=['sepal_lenght','sepal_width','petal_length','petal_width','class']
df.columns=col_names
print(df.head())
mask_class=df['class']=='Iris-virginica'
df.loc[mask_class,'class']='New label'
print(df.groupby('class').mean())