#! /usr/bin/env python3
# coding = utf-8


class Person():

    def __init__(self, name):
        self.name = name


class EmailPerson(Person):

    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


class Circle():

    def __init__(self, redius):
        self.redius = redius

    @property
    def diameter(self):
        return 2 * self.redius


class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little object")

easy_a = A()
breezy_a = A()
wheezy_a = A()

A.kids()
