__author__ = 'Kalyan'

from placeholders import *

# write a class Person with attributes name, age, weight (kgs), height (ft) and takes
# them through the constructor and exposes a method get_bmi_result()
# which returns one of "underweight", "healthy", "obese"
# http://en.wikipedia.org/wiki/Body_mass_index

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.get_bmi_result()

    def get_bmi_result(self):
        height = self.height
        weight = self.weight
        height = (float(height) * 0.3)
        x=(float(height)**2)
        bmi = float(weight)/x

        if bmi < 18.5:
            return "underweight"
        elif 18.5 < bmi < 30:
            return "healthy"
        else:
            return "obese"

def test_classes_write_your_own():
    p = Person("hari", "25", "6", "30")
    assert "underweight" == p.get_bmi_result()

    p = Person("hari", "25", "6", "200")
    assert "obese" == p.get_bmi_result()

    p = Person("hari", "25", "6", "75")
    assert "healthy" == p.get_bmi_result()


three_things_i_learnt = """
-Defining a constructor in a class..
-Taking the arguments and using them in another function.
-Using the attributes of a constructor into another function by using self in a class.
-Typecasting.. :)
"""

time_taken_minutes = 20
