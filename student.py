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

# numlist=list(map(int,input("enter the list numbers seperated by space").strip().split()))[:5]
# print(numlist)

# list_a=[5,"six",[8,9,7,5],8.2]
# print(list_a[-1])
# print(list_a[2][-3])
# print(list_a[3])

# list_a=["five","six"]
# print(list_a[0][1])
#string formating


# dict_a = {
#     "name":"suji",
#     "age":22
# }
# print(dict_a["age"])
# dict_a={
#     "name":"suji",
#     "age":22,
#     "roll_no":22
# }
# result="college" in dict_a
# print(result)
#
# name="rohith"
# age="22"
# msg="hi {}. you are {} years old."
# print(msg.format(name,age))

#add key value pair
# dict_a={'name':'suji','age':22}
# dict_a['city']='goa'
# dict_a['country']='india'
# print(dict_a)
#
# dict_a={
#     "name":"suji",
#     "age":22,
#     "roll_no":22
# }
# #delete
# del dict_a['age']
# print(dict_a)
#dict_keys,values,items
# dict_a={
#     "name":"suji",
#     "age":22,
#     "roll_no":22
# }
# print(dict_a.keys())
# print(dict_a.values())
# print(dict_a.items())

#loopover dictnories
# dict_a={
#     "name":"suji",
#     "age":22,
#     "roll_no":22
# }
# for key,value in dict_a.items():
#     # print(dict_a[values])
#     pair="{}:{}".format(key,value)
#     print(pair)

#
#
# m=int(input())
# n=int(input())
# mat=[]
# for i in range(m):
#     row=input().split()
#     for j in row:
#         mat.append(j)
# mat.sort()
# k=0
# for i in range(m):
    # for j in range(n):
    #     print(mat[k],end=' ')
    #     k=k+1
    # print()

# #cannot add/remove dict keys while iterating the dictionary
# dict_a={'name':'suji','age':22}
# for k in dict_a.keys():
#     if k=='name':
#         del dict_a[k]
# print(dict_a)

# #membership of dict and clear a dict
# dict_a={
#     'name':'suji'
#     'age':22
#}

# def sample():
#     print("hello")
# sample()
# name="sujitha"
# sample()
# print(name)
#
# #functions
#
# def function(arg1,arg2):
#
# argument1,argument2= function("sujitha","rohith")
# print(argument1,argument2)

# def greet(welcome):
#     msg= welcome + "hcl"
#     print(message)
#     name=input()
#     greet(welcome=name)
# def greet(welcome):
#     msg= welcome +"hcl"
#     return msg
# print(msg)
#
# start_num=int(100)
# end_num=int(200)
# cnt=start_num
# while cnt <= end_num:
#     if cnt%7==0:
#         print(cnt,"divisible by 7")
#     cnt+=1



#
# def function(n):
#     if int(n)%7==0:
#         print("true")
#     else:
#         print("false")
# function(1744)
#
# def function(side):
#     area=side*side
#     perimeter=4*side
#     return area,perimeter
# side=int(input())
# print(function(side))

# # def function(s):
# s="sujita"
# print(s[1])
# print(function)

# def function(n):
#     if int(n)%3==0:
#         print("marco")
#     elif int(n)%5==0:
#         print("polo")
#     elif int(n)%3==0 & int(n)%5==0:
#         print("marcopolo")
#     else:
#         print("no")
# function(176)

# def function(bill):
#     if bill<500:
#        dis=(bill*0.05)
#     elif bill>=500 & bill<2500:
#         dis=(bill*0.10)
#     else:
#         bill>=2500
#         dis=(bill*0.20)
#     return dis
# inp=int(input())
# amount=function(inp)
# pay=inp-amount
# print("actual amount" +str(inp))
# print("discount amount" +str(amount))
# print("amount after discount" +str(pay))

# n=int(input())
# sum_1=0
# while (n>0):
#     sum_1=sum_1+n
#     n=n-1
#print("sum of n natural numbers",sum_1)

# class car:
#     def sample_car_instance_method(self,a):
#         print(a)
# carobj=car()
# carobj.sample_car_instance_method("hello again!")
#
# carobj2=car()
# carobj.sample_car_instance_method(2)
#
# #staticmethod
# class StaticClass:
#     @staticmethod
#     def sample_static_method_addition(x,y):
#         return x+y
#     @staticmethod
#     def sample_static_method_multiplication(x,y):
#         return x*y
# staticobj=StaticClass()
# output_add=staticobj.sample_static_method_addition(5,3)
# output_mul=staticobj.sample_static_method_multiplication(5,3)
# print(output_add,output_mul)
        # StaticClass.sample_static_method_addition(5,3)
        # StaticClass.sample_static_method_multiplication(5,3)

# class car():
#     def attributeis_engine_started(self,true):
#         print(true)
#     def attributeis_engine_stopped(self,false):
#         print(false)
# carobj=car()
# carobj.attributeis_engine_started("ON")
# carobj.attributeis_engine_stopped("OFF")

# class car():
#     def __init__(self,color,max_speed,tyre_friction,current_speed):
#         self.color=color
#         self.max_speed=max_speed
#         self.tyre_friction=tyre_friction
#         self.current_speed=current_speed
#     def start_engine(self):
#         self.is_engine_started = True
#     def stop_engine(self):
#         self.is_engine_stopped = False
#     def apply_breaks(self):
#         print("beep beep")
#
#     else:
#     print("car not started")
#
#
# carobj = car("black", "67", 70, 80)
# carobj.start_engine()
# carobj.sound_horn()
# carobj.apply_breaks()
# carobj.apply_breaks()
# carobj.stop_engine()
# carobj.sound_horn()

#inheritance
# class product:
#     def __init__(self,name,price,deal_price,rating,warrenty,expirydate,packagedate):
#         self.name=name
#         self.price=price
#         self.deal_price=deal_price
#         self.rating=rating
#         self.warrenty=warrenty
#         self.expirydate=expirydate
#         self.packagedate=packagedate
#     def display_product_details(self):
#        print(self.name)
#        print(self.price)
#        print(self.deal_price)
#        print(self.rating)
#        # print(self.warrenty)
#        # print(self.expirydate)
#        # print(self.packagedate)
# class electronicdevice(product):
#    def get_warrenty(self):
#         print(self.warrenty)
# class groceryitem(product):
#     def get_expirydate(self):
#         print(self.expirydate)
#     def get_packagedate(self):
#         print(self.packagedate)
#
# classobj=grocer("sujitha",200,150,4,1,10/12/22,22/11/23)
# classobj.display_product_details()
# # classobj.electronicdevice()
# # classobj.groceryitem()
# classobj.get_warrenty()
# # classobj.get_expirydate()
# # classobj.get_packagedate()

# class TestCar(unittest.TestCase):
#       def setUp(self):
#           self.car = Car()
#
#
# class TestInit(TestCar):
#       def test_initial_speed(self):
#           self.assertEqual(self.car.speed, 0)
#
#       def test_initial_odometer(self):
#           self.assertEqual(self.car.odometer, 0)
#
#       def test_initial_time(self):
#           self.assertEqual(self.car.time, 0)
#
#
# class TestAccelerate(TestCar):
#       def test_accelerate_from_zero(self):
#           self.car.accelerate()
#           self.assertEqual(self.car.speed, 5)
#
#       def test_multiple_accelerates(self):
#           for _ in range(3):
#             self.car.accelerate()
#           self.assertEqual(self.car.speed, 15)
#
#
# class TestBrake(TestCar):
#        def test_brake_once(self):
#            self.car.accelerate()
#            self.car.brake()
#            self.assertEqual(self.car.speed, 0)
#
#        def test_multiple_brakes(self):
#             for _ in range(5):
#                 self.car.accelerate()
#             for _ in range(3):
#                 self.car.brake()
#             self.assertEqual(self.car.speed, 10)
#
#        def test_should_not_allow_negative_speed(self):
#            self.car.brake()
#            self.assertEqual(self.car.speed, 0)
#
#        def test_multiple_brakes_at_zero(self):
#            for _ in range(3):
#                self.car.brake()
#            self.assertEqual(self.car.speed, 0)
#
#
class Student:
    marks_bonus=1.5
    none=" "
    def __init__(self,first,last,marks):
        self.first=first
        self.last=last
        self.marks=marks
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)
    @property
    def fullname(self):
        return '{}.{}'.format(self.first,self.last)
    def apply_bonus(self):
        self.marks=int(self.marks*self.marks_bonus)
    def none1_thing(self,middle):
        self.none= self.first+self.last+middle