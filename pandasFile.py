import pandas as pd
#dataframe=DataFrame
#series
dict = [1,2,3]
Series=pd.Series(dict)
print(Series)

#reading text file using pandas
#read_csv is used to read the document
df=pd.read_csv('pandastext.txt')
print(df)

print(df.info())
print(df.head(1)) #to extract the list from top
print(df.tail(1)) #to extract the list from bottom
#while converstion to numpy from pandas
#dataframe to numpy doesnot include the index,coloumnslables in the output
print(df.to_numpy)
#with multiple datatypes,conversions are expensive
print(df.describe())

#transpose

print(df)
print(df.T)

#sorting
print(df.sort_index(axis=1,ascending=False))

print(df.sort_index(axis=0,ascending=True))

#getting values
print(df.sujitha)

print(df["rohith"])

print(df[0:3])
#selection locate
# print(df.loc[dates[0]])

#multi-axis
print(df.loc[:,["sujitha","rohith"]])

#boolen indexing
print(df[df["rohith"]>19])

print(df[df>0])

#is in
df=df.copy()
df["sai"]=[12,121,13,143]
print(df)

df[df["sai"].isin(["34"])]

