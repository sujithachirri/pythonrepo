def sample():
    print("hello")


sample()
name = "sujitha"
sample()
print(name)


# functions
#
# def function(arg1, arg2):
#     return arg1,arg2
#
# argument1, argument2 = function("sujitha", "rohith")
# print(argument1, argument2)

def greet(welcome):
    msg= welcome + "hcl"
    print(message)
    name=input()
    greet(welcome=name)
def greet(welcome):
    msg= welcome +"hcl"
    return msg
print(msg)


start_num=int(100)
end_num=int(200)
cnt=start_num
while cnt <= end_num:
    if cnt%7==0:
        print(cnt,"divisible by 7")
    cnt+=1

def function(n):
    if int(n)%7==0:
        print("true")
    else:
        print("false")
function(175)

#return area and perimeter of square
def function(side):
    area=side*side
    perimeter=4*side
    return area,perimeter
side=int(input())
print(function(side))

def function(n):
    if int(n)%3==0:
        print("marco")
    elif int(n)%5==0:
        print("polo")
    elif int(n)%3==0 & int(n)%5==0:
        print("marcopolo")
    else:
        print("no")
function(176)

def function(bill):
    if bill<500:
       dis=(bill*0.05)
    elif bill>=500 & bill<2500:
        dis=(bill*0.10)
    else:
        bill>=2500
        dis=(bill*0.20)
    return dis
inp=int(input())
amount=function(inp)
pay=inp-amount
print("actual amount" +str(inp))
print("discount amount" +str(amount))
print("amount after discount" +str(pay))

n=int(input())
sum_1=0
while (n>0):
    sum_1=sum_1+n
    n=n-1
print("sum of n natural numbers",sum_1)

