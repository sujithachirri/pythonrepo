
dict_a = {
    "name":"suji",
    "age":22
}
print(dict_a["age"])
dict_a={
    "name":"suji",
    "age":22,
    "roll_no":22
}
result="college" in dict_a
# print(result)
#
# #add key value pair
# dict_a={'name':'suji','age':22}
# dict_a['city']='goa'
# dict_a['country']='india'
# print(dict_a)

dict_a={
    "name":"suji",
    "age":22,
    "roll_no":22
}
#update
dict_a['age']=24
print(dict_a)

dict_a={
    "name":"suji",
    "age":22,
    "roll_no":22
}
#delete
del dict_a['age']
print(dict_a)

#dict_keys,values,items
dict_a={
    "name":"suji",
    "age":22,
    "roll_no":22
}
print(dict_a.keys())
print(dict_a.values())
print(dict_a.items())

dict_a={
    "name":"suji",
    "age":22,
    "roll_no":22
}
for key,value in dict_a.items():
    # print(dict_a[values])
    pair="{}:{}".format(key,value)
    print(pair)

#converting list to dict
list=[
    ("name","suji"),
    ["age",22]
]
dict_a=dict(list)
print(dict_a)

#cannot add/remove dict keys while iterating the dictionary
dict_a={'name':'suji','age':22}
for k in dict_a.keys():
    if k=='name':
        del dict_a[k]
print(dict_a)

