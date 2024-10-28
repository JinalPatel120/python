# import sys

# print(sys.version)

# if 5 > 2:
#     print("yes")
# else:
#     print("not")

# # this is comment
# """ this is multiline comment"""

# x = 5
# print(x)
# print(type(x))
# a = 1
# A = 2
# print(a, A)


# def add(a, b):
#     return a + b


# print(add(2, 3))
# x, y, z = "j", "b", "z"
# print(x)
# print(y)
# print(z)
# fruits = ["banana", "apple", "cherry"]
# x, y, z = fruits
# print(x)
# print(y)
# print(z)


# z = "awesome"


# def myfunc():
#     global z
#     z = "fantastic"
#     print("python is" + z)


# myfunc()
# print(z)
# x = 1j
# print(type(x))
# k = {"name": "jinal"}
# print(k.keys())
# print(k.values())

# for i in k:
#     print(i)
#     print(k[i])


# def add_number(a: int, b: int) -> int:
#     return a + b


# print(add_number(1, 20))
# print(add_number(1.24, 20.90))
# print(add_number("jinal", "20"))


# x = 9
# print(type(x))
# x = float(x)
# print(type(x))
# print(x)

# a = """hello 
# how are
# you"""

# print(a)
# print("hello")
# print(len(a))
# print("jinal" in a)

# for x in "banana":
#     print(x)

# b = "helllo world"
# print(b[1:5])
# print(b[:5])
# print(b[-5:-2])
# print(b.upper())
# print(b.lower())
# print(a.strip())
# a = "hello world!"
# print(a.replace("h", "s"))
# print(a.split(","))

# a = "Hello World!"
# print(a.split(","))

# age = 21
# txt = f"my age is {age}"
# print(txt)

# txt = 'we are so called "vikings" from the north'
# print(txt)
# txt = 'We are the so-called "Vikings" from the north.'
# print(txt)


# mylist = ["apple", "banana", "cherry"]
# print(mylist)
# # for i in mylist:
# #     print(i)

# print(mylist[0])
# print(len(mylist))
# print(type(mylist))
# mylist[1] = "mango"
# print(mylist)
# mylist.append("helo")
# print(mylist)
# mylist.insert(1, "jinal")
# print(mylist)

# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thislist.extend(tropical)
# print(thislist)

# tropical = ("kiwi", "orange")
# thislist.extend(tropical)
# print(thislist)
# thislist.remove("apple")
# print(thislist)
# thislist.pop(1)
# print(thislist)
# thislist.pop()
# print(thislist)
# del thislist[0]
# print(thislist)
# # del thislist
# # print(thislist)
# # thislist.clear()
# # print(thislist)

# for x in thislist:
#     print(x)

# for i in range(len(thislist)):
#     print(thislist[i])

# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1

# [print(i) for i in thislist]

# new = []
# for x in thislist:
#     if "a" in x:
#         new.append(x)

# print(new)

# new = [x for x in thislist if "a" in x]
# print(new)
# new = [x for x in thislist if x != "apple"]
# print(new)

# new = [x for x in thislist]
# print(new)

# new = [i for i in range(10)]
# print(new)

# new = [x.upper() for x in thislist]
# print(new)
# thislist.sort()
# print(thislist)

# k = [12, 54, 65, 87, 9, 54, 23, 65, 32]
# k.sort()
# print(k)

# k.sort(reverse=True)
# print(k)

# thislist = ["banana", "Apple", "Orange", "Kiwi", "cherry"]
# thislist.sort(key=str.lower)
# print(thislist)
# thislist.reverse()
# print(thislist)

# mylist = thislist.copy()
# mylist.append("hello")
# print(mylist)

# print(thislist)

# l1 = ["jinal", "poorvi", "komal", "hina", "ekta"]
# l2 = l1

# l2.append("hello")
# l1.append("kiara")
# print(l1)
# print(l2)

# mylist = list(l1)
# l1.append("rutvik")
# print(l1)
# print(mylist)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)

# for x in list2:
#     list1.append(x)

# print(list1)


# tp = ("hello", "jinal", "lathiya")
# print(len(tp))
# print(tp[1])
# print(tp[-1])

# tp = "hello"
# print(type(tp))

# tp = ("hello",)
# tp = list(tp)
# tp[0] = "jinal"
# print(tp)
# print(type(tp))

# tp = [12, 32, 43, 56, 76]
# print(type(tp))


# m = (1, 2, 3)
# m = list(m)
# m[0] = 11
# print(m)
# print(type(m))

# m = (1, 2, 3)
# n = (4,)
# m += n
# print(m)

# m = (1, 2, 3)
# (a, b, c) = m
# print(a)
# print(b)
# print(c)

# for i in m:
#     print(i)

# for i in range(len(m)):
#     print(m[i])

# i = 0
# while i < len(m):
#     print(m[i])
#     i += 1


# tp = ("a", "b", "c")
# tp1 = (1, 2, 3)
# t3 = tp + tp1
# k = tp1 * 2
# print(k)
# print(t3)

# s = {"apple", "mango", "banana", 54, "apple"}
# print(s)
# print(type(s))
# s = {"apple", "mango", "banana", True, 1}
# print(s)

# x = 200.0
# print(isinstance(x, int))

# this = set(("apple", "mango", "cherry"))
# print(this)

# print(type(this))

# j = {"apple", "banana", "mango"}
# h = {"pineapple", "papaya", "tomato"}
# j.update(h)
# # j.add('orange')
# print(j)

# j.remove("banana")  # if item not present it will raise error
# print(j)

# j.discard("banana")  # it item not present it will not raise error
# print(j)

# h.pop()
# print(h)


# dict1 = {"name": "jinal", "lname": "lathiya", "city": "bhavanagar"}

# print(dict1["name"])
# print(dict1.get("lname"))
# print(dict1.keys())
# print(dict1.values())
# for i in dict1:
#     print(dict1[i])

# dict1["color"] = "white"
# print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())

# dict2 = {"brand": "ford", "model": "mustang", "year": 1964}
# # dict2.pop('brand')
# dict2.popitem()
# print(dict2)

# dict2.pop("brand")
# dict2.clear()
# print(dict2)

# student = {"name": "jinal", "course": "BCA", "grade": "A"}

# for i in student.values():
#     print(i)

# for i in student.keys():
#     print(i)

# for i, j in student.items():
#     print(i, j)


# stud = {
#     "stud1": {"name": "jianl", "lname": "lathiya"},
#     "stud2": {"name": "poorvi", "lname": "kakadiya"},
# }

# print(stud)
# print(stud["stud1"]["name"])

# def myFunc(*args):
#     print('the name is',args)

# myFunc('jinal','lathiya')

# def myfunc(**kwargs):
#     print('the name is',kwargs['fname'])

# myfunc(fname='jinal',lname='lathiya')


# a = 200
# b = 33
# c = 500

# if a > b and c < a:
#     print("both true")
# else:
#     print("false")

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i += 1


# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
