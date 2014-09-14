'''
Created on 2013-05-17

@author: Harsha
'''

class WarehouseSnapshot:
    def __init__(self, name=None, year=0, month=0):
        self.name = name
        self.year = year
        self.month = month
        self.skus= []

class Sku:
    def __init__(self, name=None, quantity=0, unitValue=0):
        self.name = name
        self.quantity = quantity
        self.unitValue = unitValue

class Report(object):
    def __init__(self, units=0, value=0, changeInValue=0):
        self.units = units
        self.value = value
        self.changeInValue = changeInValue

class WarehouseReport(Report):
    def __init__(self, skus=0, units=0, value=0, changeInValue=0):
        super(WarehouseReport,self).__init__(units, value, changeInValue)
        self.skus = skus