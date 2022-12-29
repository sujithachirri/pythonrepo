# import pandas as pd
#
# df=pd.read_csv("C:/Users/user738/PycharmProjects/pythonProject1/pokemon_data.csv")

# print(df)

#interchanging
# df['Type 1'],df['Type 2'] = df['Type 2'],df['Type 1']
# print(df.to_string())
#print(df.head(50))


#date
# date_index=pd.date_range('1/1/2000',periods=800)
# print(date_index)
# df['#']=date_index
# print(df.to_string())

# #groupby
# df2=df.groupby('Type 1').sum()
# print(df2)

#new dataframe
# search='A'
# s=df[df.Name.str.startswith(search)]
# print(s)




import os
with open("ip_list.txt") as file:
    park=file.read()
    park=park.splitlines()
    print("{park} \n")
    #ping for each ip in the file
for ip in park:
    response=os.popen(f"ping {ip} ").read()
    if("request timed out." or "unreachable") in response:
        print(response)
        f=open("info_output.txt","a")
        f.write(str(ip)+'link is down '+'\n')
        f.close()
    else:
        print(response)
        f=open("info_output.txt","a")
        f.write(str(ip)+'is up '+'\n')
        f.close()
with open("ip_output.txt")as file:
    output=file.read()
    f.close()
    print(output)
with open("info_output.txt","w")as file:
    pass

