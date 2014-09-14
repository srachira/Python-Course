'''
Created on 2013-05-17

@author: Harsha
'''
from abc import ABCMeta, abstractmethod
from models import WarehouseSnapshot

class WarehouseSnapshotDao:
    __metaclass__ = ABCMeta

    @abstractmethod
    def createEqualsQueryFilter(self, fieldName, equalToValue):
        return

    @abstractmethod
    def find(self, queryFilters):
        return

    @abstractmethod
    def findOne(self, queryFilters):
        return

class WarehouseSnapshotDaoMemoryImpl(WarehouseSnapshotDao):
    class EqualsQueryFilter:
        def __init__(self, fieldName, equalToValue):
            self.fieldName = fieldName
            self.equalToValue = equalToValue

        def matches(self, warehouseSnapshot):
            return getattr(warehouseSnapshot, self.fieldName) == self.equalToValue

    def __init__(self):
        self.warehouseSnapshots = []

    def createEqualsQueryFilter(self, fieldName, equalToValue):
        return self.EqualsQueryFilter(fieldName, equalToValue)

    def find(self, queryFilters):
        filteredWarehouseSnapshots = []
        for warehouseSnapshot in self.warehouseSnapshots:
            passesFilters = True
            for queryFilter in queryFilters:
                if not queryFilter.matches(warehouseSnapshot):
                    passesFilters = False
                    break
            if passesFilters:
                filteredWarehouseSnapshots.append(warehouseSnapshot)
        return filteredWarehouseSnapshots

    def findOne(self, queryFilters):
        filteredWarehouseSnapshot = None
        filteredWarehouseSnapshots = self.find(queryFilters)
        if len(filteredWarehouseSnapshots) > 0:
            filteredWarehouseSnapshot = filteredWarehouseSnapshots[0]
        return  filteredWarehouseSnapshot

    def addWarehouseSnapshot(self, warehouseName, year, month):
        warehouseSnapshot = WarehouseSnapshot(warehouseName, year, month)
        self.warehouseSnapshots.append(warehouseSnapshot)
        return warehouseSnapshot
