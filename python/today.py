
# abc={'name':'jinal'}
# k=abc.get('age')  ---- if key not present then return None
# print(k)

# abc={'name':"jinal",'age':21}
# m=abc['hello']
# print(m)  --- raise keyerror if key will not present


# f=open('stud.csv','r')
# print(f.read())

# import csv

# data=[{'fname':"jinal",'lname':"lathiya",'year':21},
#       {'fname':'diya','lname':'rathod','year':22}]

# with open('stud.csv','w',newline='') as csvfile:
#     fieldname=['fname','lname','year']
#     writer=csv.DictWriter(csvfile,delimiter='|',fieldnames=fieldname)
#     writer.writeheader()
#     writer.writerows(data)


# person_data={
#     'name':'jinal',
#     'lname':'lathiya'
# }

# person_value=person_data.get('age')
# if person_value is None:
#     print('value is none')

# value=person_data['age']
# print(value)


# if "age" in person_data:
#     print(' valid key')
# else:
#     print('not valid key')

# person_data.update({"age":'22'})
# if "age" in person_data:
#     print(' valid key')
# else:
#     print('not valid key')




# class Alphabet:
#     def __init__(self, value):
#         self._value = value


#     def getValue(self):
#         print('Getting value')
#         return self._value


#     def setValue(self, value):
#         print('Setting value to ' + value)
#         self._value = value


#     def delValue(self):
#         print('Deleting value')
#         del self._value

#     value = property(getValue, setValue, 
#                      delValue, )


# # passing the value
# x = Alphabet('hello jinal')
# print(x.value)

# x.value = 'hello'

# del x.value



class MyClass:
      __name=None
      __roll=None
      def __init__(self,name,roll):
        self.__name=name
        self.__roll=roll


      def __displayDetails(self):
        print('name',self.__name)
        print('roll',self.__roll)

      def accessPrivateFunction(self):
          self.__displayDetails()



obj=MyClass('hello',21)

print(obj._MyClass__name)
print(obj._MyClass__roll)
obj._MyClass__displayDetails()

obj.accessPrivateFunction()
   


from abc import ABC, abstractmethod

class Rectangle(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class Square(Rectangle):
    def area(self):
        print('4 sides of square')

obj_square=Square()
obj_square.area()


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

   
    def display(self):
        print('name from display : ',self.name)
        print('age from display : ', self.age)

    @classmethod
    def display_data(cls,name):
        print('name from class method',name) 

    @staticmethod
    def show(name,age):
        print('name from show',name)
        print('age from show',age)

obj_person=Person('jinal',21)
obj_person.display()
obj_person=Person.display_data('hello')

Person.show('jiya','22')

# file_path="jinal.txt"   
# file=open(file_path,'r')
# print(file.read())
# file=open('2.txt','w')
# writer='hello how are you ?'
# print(file.write(writer))