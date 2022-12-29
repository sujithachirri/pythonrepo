# a=2
# set_a={5,"six",a,8.2}
# print(type(set_a))
# print(set_a)
#
# set_a={"a","b","c","a","b"}
# print(set_a)

set_a={"a",["c","a"]}
print(set_a)

# import math
# a=[1,2,3,4]
# print(type(a))
#
# a=23
# b=22
# print(a+b)
#
# a="sujitha"
# #b=878
# print(a)
#
# print("python is amazing")
#
# print("python\tis\tamazing")
#
# #a=[1,2,7,8]
# #print(type(a))
#
# #a={3,4,5,0}
# #print(type(a)
#
# a="abcdefgh"
# print(list(a))
# print(tuple(a))
# print(set(a))
#
# thisdict= {
#     "name" : "sujitha",
#     "class": "python",
#     "year" : 2022
# }
# print(thisdict["year"])
#
# list_a=34
# list_b=list_a
# print(list_a,7+6)
#
# list_a="python is a programming language"
# x=list_a.split("a")
# print(x)
#
# text="apple","banana","orange"
# x="rohi".join(text)
# print(x)
#
# list_a=list(range(7))
# print(list_a)
#
# list_a=[1,2,3,4]
# list_b=list_a
# print(id(list_a));
# print(id(list_b));
#
# list_b[3]=4
# print(list_a)
# print(list_b)
#
# list_a=[5,4,3,2,1]
# list_b=list_a[4:0:-2]
# print(list_b)
#
# s="sujitha"
# print(s[-7])
#
# m=[45]
# n=19
#
# mylist_a=m * n
# print(mylist_a)
#
# list_a=[1,2,3,4,5,6,7,8,9]
#
# s="sujitha"
# print(s[-7])
# list_b=list_a[::-1]
# print(list_b)
#
# list_a=[1,2,3,4,5,6,7,8,9]
# a=list_a[0:3]
# b=list_a[6:9]
# print(a+b)
# #
# # #list_a=[1,45,778,6,7,89]
# # #n=7
# # #print(list_a>n)
# #
# # a_1="orange"
# # b_1="orAgami"
# # print(a_1[0:3]==b_1[0:3])
# #
# # a=[1,3,5]
# # b=[7,8,9]
# # print(a[0]<b[2])
# #
# # m=80
# # p=90
# # c=90
# # print((m>=70)or(p>=60)or(c>=60))
# # print((m+p+c>=180))
# # print(false or false)
# # print(not(false))
#
# # def myfun(n):
# #     return len(n)
# # x=map(myfun,('apple','banana'))
#
# a="SuJiThA"
# x=a.swapcase()
# print(x)
#
# a="dd-mm-yy"
# a=a.replace("-","/")
# print(a)
#
# def ispalindrome(string):
#     return string == string[::-1]
#     #     return("string is palindrome")
#     # else:
#     #     return("string is not palintrome")
# string="madam"
# x= ispalindrome(string)
# if x:
#     print("yes")
# else:
#     print("no")
#
# p="Su@"
# print(p==p[0].upper() and p==p[1].lower() and p==p[2].integer())
# print(not(false))
#
# a=2
# set_a={5,"six",a,8.2}
# print(type(set_a))
# print(set_a)
#
# set_a={"a","b","c","a","b"}
# print(set_a)
#
# set_a={"a",["c","a"]}
# print(set_a)
#
# set_a=set("rrrooohith")
# print(type(set_a))
# print(set_a)
#
# set_a=set("apple")
# print(set_a)
#
# set_a=set([1,2,1])
# print(type(set_a))
# print(set_a)
# #tuppletoset
# set_a=set((1,2,1))
# print(set_a)
# #as items are not ordered
# set_a={1,2,3}
# print(set_a[1])
# print(set_a[1:3])
# set_a={1,3,5,6,7,9}
# set_a.remove(3)
# print(len(set_a))

# set_a={4,2,8}
# set_b={1,2}
# symmetric_diff=set_a^set_b
# print(symmetric_diff)
#
# set_1={1,2}
# set_2={3,4}
# is_disjoint=set_1.isdisjoint(set_2)
# print(is_disjoint)

n = int(input())
numlist=list(map(int,input("enter the list numbers seperated by space").strip().split()))[:n]
print(numlist)

#string formating

name="sujitha"
age="22"
msg="hi {}. you are {} years old."
print(msg.format(name,age))