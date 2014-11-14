from stack import *
from newQueue import *
from recursion import *
from singleLinkedList import *

food = Stack() #this is a class (aka constructor, aka factory)
food.push('hamburder')
food.push('fries')
food.push('cake')
food.pop()  #removes cake



pets = newQueue()

pets.inqueue('dog')
pets.inqueue('cat')
pets.inqueue('fish')

pets.dequeue()  #removes dog
pets.dequeue()  #removes cat

print(fact(5))

print(fib(8))


for x in range(0, 20):
    print(fib(x))

people = SingleLinkedList()
people.insert("bob")
people.insert("sara")
people.insert("jill")



pass