# # for i in range(5):
# #     print("hello world")

# # i=1
# # while(i<5):
# #     print('hwllo world')
# #     i=i+1

# def insert():
#     print('hellow world')
#     print('rohith')
#     print('satyam mishra')
#     print('srija  mondal')
# insert()

# def sum(a,b):
#     print(a+b)
# sum(1,2)

# list = ['rohith','rahul',"gta","rahul das"]
# list.append("srija mondal")
# list.remove('rahul das')
# list.insert(1,'rahul das')
# print(list)

# list1 = ('rohith','rahul das','srija mondal')
# # print(list1)
# for i in range (len(list1)):
#     print(i)

# dic = {'name':"rohith",'age':20,'usn':122,'marks':90,'sem':5}
# print(dic)
# print(dic['name'])

############class and object#####################

# class student:
#     def display(self):
#         print("hellow world")
#         print("rahul das")
#         print("rohith d")
#         print('srija mondal')

# s1 = student()
# s1.display()

##################constructor##################

# class student:
#     def __init__(self ,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.marks)
# s1 = student('rohith',20,100)
# s2 = student('satyam',20,100)

# s1.display()
# s2.display()

# class student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self, marks):
#         self.__marks = marks

#     def show_marks(self):
#         print("Student marks =", self.__marks)


# s1 = student()
# s1.set_marks(90)
# s1.show_marks()

##############inheitance#################
# class father:
#     def house(self):
#         print("father has a house")
# class son(father):
#     def car(self):
#         print("son has a car")
# s = son()
# s.car()
# s.house()
###############multiple inheritance#################
# class grandfather:
#     def house(self):
#         print("grand father has the house")
# class father(grandfather):
#     def car(self):
#         print("father has a car")
# class son(father):
#     def land(self):
#         print("son has a land")
# s1 = son()
# s1.house()
# s1.car()
# s1.land()
###############polymorphism##################
# class actual:
#     def sound(self):
#         print("animal has a sound")
# class dog(actual):
#     def sound(self):
#         print("dog barks")
# class cat(actual):
#     def sound(self):
#         print('cat meow')

# animal = [dog(), cat(), actual()]
# for animals in animal:
#     animals.sound()

#################abstraction##########################

from abc import ABC, abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self):
        pass


class upi(payment):
    def pay(self):
        print("payment done in upi")


class card(payment):
    def pay(self):
        print("payment using card")


# Creating objects
p1 = upi()
p2 = card()

p1.pay()
p2.pay()