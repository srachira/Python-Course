__author__ = 'Kalyan'

import random

class Person(object):
    def __init__(self, ssn, name):
        self.ssn = ssn
        self.name = name

    def __hash__(self):
        return

    def __eq__(self, other):
        return self.ssn == other.ssn


if __name__ == "__main__":
    p1 = Person("0124", "Kalyan",35 )
    p2 = Person("0124", "Kalyan",36 )

    p3 = Person("0124", "Hari",40)

    friends = {}
    friends[p1] = p3

    print friends[p3]
