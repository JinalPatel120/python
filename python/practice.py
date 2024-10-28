class MyClass:
    price = 500

myclass_obj = MyClass()
print(myclass_obj.price)

class person_data:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p_data = person_data("jinal", 21)
print(p_data.name)
print(p_data.age)

class person_details(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('name',self.name)

    def test(self):
        print('hello')
    @classmethod
    def myfunc(cls):
        print("hello my name is", cls.test)


p = person_details("jinal", 22)
p.myfunc()
# print(p.__)
class person_database:
    def __init__(self,test):
        # self.name = name
        # self.age = age
        print('loaded database')
      
    def myfunc(self):
        print("hello my name is, database", self.name)


class child(person_database):
    pass

# c = child("jinal", 21)
# c.myfunct()

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('person loaded database')


    def myfunct(self):
        print("hello my name is", self.name)


class child(person,person_database):
    def __init__(self, name, age, year):
        super().__init__(name, age)
     
        self.year = year

    def welcome(self):
        print("Welcome", self.name, self.age, self.year,self.myfunc())

c = child("jinal", 21, 2002)
c.myfunct()
c.welcome()


def square(n):
    '''take a number n and return square of n'''
    return n*2

print(square.__doc__)


def add(a,b):
    'add 2 numbers'
    return a+b

print(add.__doc__)

# temp=10
# def func():
#     global temp
#     temp=20
#     print(temp)

# print(temp)
# func()
# print(temp)

# mytuple=('apple','banana','mango')
# myit=iter(mytuple)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# fruit='banana'
# myit=iter(fruit)
# print(next(myit))
# print(next(myit))
# print(next(myit))

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class student:
#     def data(self,name,price):
#         self.name=name
#         self.price=price
#         print(f'name is{self.name},price{self.price}')

# s=student()
# s.data('jinal',22)


# import datetime
# date_time=datetime.datetime.now()
# print(date_time)


# stack=['jinal','jiya','jay']
# stack.append('ram')
# print(stack)

# a=min(5,10,250)
# b=max(5,6,7,8,32)
# print(a)
# print(b)
# x=abs(-8.90)
# print(x)

# import math

# x=math.sqrt(64)
# print(x)
# x=math.ceil(1.4)
# y=math.floor(1.4)
# print(x)
# print(y)

# import json

# x='{"name":"jinal","lname":"lathiya"}'
# y=json.loads(x)
# print(type(x))
# print(y['lname'])
# print(y)
# y=json.dumps(y)
# print(type(y))
# import json

# import re
# txt='the rain in spain'
# x=re.search("^the.*spain$",txt)
# print(x)

# import camelcase
# camel_var=camelcase.CamelCase()
# txt='hello world'
# print(camel_var.hump(txt))

# f=open('jinal.txt','r')
# print(f.read())

# f=open('jinal.txt','r')
# print(f.readline())
# f.close()

# f=open('jinal.txt','a')
# f.write('\ni will append this content')
# f.close()

# f=open('jinal.txt','r')
# print(f.read())

# f=open('jinal.txt','w')
# f.write('\ni will overwrite this content')
# f.close()


# # f=open('jinal.txt','r')
# # print(f.read())

# # f=open('myfile2.txt','x')

# # import os
# # os.remove('myfile1.txt')


# import numpy as np
# arr=np.array([1,2,3,4,5,6,70])
# print(arr)
# print(type(arr))

# import pandas as pd

# data={'name':['jianl','ekta','hina'],
#       'age':[22,23,22]}

# df=pd.DataFrame(data)
# print(df.loc[0])
# print(df)

# df=pd.DataFrame(data,index=['id-1','id-2','id-3'])
# print(df)
# print(df.loc['id-1'])

# df=pd.read_csv('student.csv')  # use to load csv file
# print(df)

# df=pd.read_csv("C:\\Users\\kishan patel\\Downloads\\olympics.csv")
# print(df.head())
# print(df.tail())

# print(df.info())
# print(df.describe())

# # import matplotlib.pyplot as plt
# # new_df=df.dropna()
# # df.plot()
# # df.plot(kind='scatter',x='gold',y='silver')
# # plt.show()

# from scipy import constants
# print('hello')
# print(constants.liter)

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([10,20,30])
# y=np.array([1,2,3])

# # plt.plot(x,y)
# # plt.plot(x,marker='*')
# # plt.plot(x,'o:r')
# # plt.plot(x,linestyle='dotted')
# # plt.title('graphical representation')
# # plt.xlabel('average')
# # plt.ylabel('percentage')
# # plt.show()

# import requests

# x=requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)

# import random

# list1=[1,2,3,4,5,6,7,6,5,44,3,33,2,4]
# print(random.choice(list1))

# # random.seed(5)
# # print(random.random())
# # print(random.random())

# r1=random.randint(10,20)
# print(r1)
# random.shuffle(list1)
# print(list1)


# # number=int(input('enter any number'))
# # try:
# #     if number %2==0:
# #         print('even number')
# #     else:
# #         print('not even number')
# # except:
# #     raise ValueError
# # finally:
# #     print('i will execute no matter what !')

# # inheritance
# class Parent:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(self.name)
#         print(self.age)

# class Child(Parent):
#     def __init__(self,name,age, fname, lname):
#         self.fname=fname
#         self.lname=lname
#         Parent.__init__(self,name,age)

#     def details(self):
#         print(self.fname)
#         print(self.lname)
#         print(self.name)
#         print(self.age)

# a=Child('jinal',22,'nita','lathiya')
# a.display()
# a.details()
     
# #polymorphism

# class Person:
#     def __init__(self,id,name):
#         self.id=id
#         self.name=name

#     def display(self):
#         print(self.id,'person')
#         print(self.name,'person')

# class Employee(Person):
#     def __init__(self, id, name,salary):
#         self.salary=salary
#         super().__init__(id, name)

#     def display(self):
#         print(self.salary,'employee')

# e=Employee(1,'jinal',50000)
# e.display()


# # encapsulation
# class Base:
#     def __init__(self):
#         self.a='hello'
#         self.__c='jinal'


# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self) # called constructor of Base class
#         print("Calling private member of base class: ")
#         print(self.__c)



# obj1 = Base()
# print(obj1.a)
# # print(obj1.__c)


# #abstraction

# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length 
#         self.__width = width    

#     def area(self):
#         return self.__length * self.__width

#     def perimeter(self):
#         return 2 * (self.__length + self.__width)


# rect = Rectangle(5, 3)
# print(f"Area: {rect.area()}")         
# print(f"Perimeter: {rect.perimeter()}")  

# # print(rect.__length)  


# my_list = [2, 3, 5, 7, 11]
# squared_dict = {x:x**2 for x in my_list if x%2 != 0} 
# print(squared_dict)


# list1={x:x+x for x in my_list}
# print(list1)

# dict1={'name':'jinal','name':'diya'}
# dict1['age']=21
# dict1.pop('name')
# dict1.clear()
# print(dict1)

# import statistics
# print(statistics.mean([40,90,21]))


# mylist = ["a", "b", "a", "c", "c"] # remove duplicates from list
# mylist = list(dict.fromkeys(mylist))
# print(mylist)

# k=dict.fromkeys(mylist)
# print(k)

# txt='hello world'[::-1]
# print(txt)

# def tellArguments(**kwargs):
#    for key, value in kwargs.items():
#        print(key + ": " + value)
# tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3")





abc={'name':'jinal'}
k=abc.get('age')
print(k)