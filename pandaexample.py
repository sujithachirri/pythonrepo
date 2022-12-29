import pandas as pd

df=pd.read_csv("C:/Users/user738/PycharmProjects/pythonProject1/pokemon_data.csv")

print(df)
# # print(df.tail(5))
# df_txt=pd.read_csv('pokemon_data.txt',delimiter='\t')
# print(df_txt.head(5))
#
# df['HP']
#
# df.columns

#read each coloumn
 # print(df['Name',)

#read each row
#
# print(df.iloc[0:4])
# #
# for index, row in df.iterrows():
#     print(index,row['Name'])
# df.loc[df['Type 1'] == "Grass"]

#read a specific location (r,c)
# print(df.iloc[2,1])
#


#changes to data
# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df)
#
# #drop a coloumn from df
# df=df.drop(columns=['Total'])
# print(df)

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df)

#column operations
# cols = list(df.columns)
# print(cols)
#
#
# df=df[cols[0:4] + [cols[-1]]+ cols[4:12]]
# print(df.to_string)
# print(df)

#filter data
# print(df['Type 1'] == 'Grass')
# new_df=df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP']>70)]
# print(new_df)

#interchange(type 1 --> type 2)

