'''
Created on 2013-05-16

@author: Harsha
'''
from unittest.case import TestCase
from inventory import FormattedTextGenerator, InventoryReportManager
from dao import WarehouseSnapshotDaoMemoryImpl
from models import Sku


class TestNames:
    WAREHOUSE_AGRA = "Agra"
    WAREHOUSE_BANGALORE = "Bangalore"
    SKU_APPLE = "Apple iPad"
    SKU_BOSE = "Bose Portable Dock II"


class FormattedTextGeneratorTests(TestCase):
    def setUp(self):
        self.formattedTextGenerator = FormattedTextGenerator()

    def tearDown(self):
        self.formattedTextGenerator = None

    def testShouldFormatWarehouseReportTitle(self):
        self.assertEqual("<h3>Warehouse- Agra</h3>",
                self.formattedTextGenerator.generateWarehouseReportTitle(TestNames.WAREHOUSE_AGRA))
        self.assertEqual("<h3>Warehouse- Bangalore</h3>",
                self.formattedTextGenerator.generateWarehouseReportTitle(TestNames.WAREHOUSE_BANGALORE))

    def testShouldFormatSkuReportTitle(self):
        self.assertEqual("<h3>SKU- Apple iPad</h3>",
                self.formattedTextGenerator.generateSkuReportTitle(TestNames.SKU_APPLE))
        self.assertEqual("<h3>SKU- Bose Portable Dock II</h3>",
                self.formattedTextGenerator.generateSkuReportTitle(TestNames.SKU_BOSE))

    def testShouldFormatSkuWarehouseReportTitle(self):
        self.assertEqual("<h3>SKU- Apple iPad, Warehouse- Agra</h3>",
                self.formattedTextGenerator.generateSkuWarehouseReportTitle(
                        TestNames.SKU_APPLE, TestNames.WAREHOUSE_AGRA))
        self.assertEqual("<h3>SKU- Bose Portable Dock II, Warehouse- Bangalore</h3>",
                self.formattedTextGenerator.generateSkuWarehouseReportTitle(
                        TestNames.SKU_BOSE, TestNames.WAREHOUSE_BANGALORE))
    def testShouldFormatErrorenousReportTitle(self):
        self.assertEqual("""<h3 class="text-error">Error generating your report!</h3>""",
                self.formattedTextGenerator.generateErroneousReportTitle())

    def testShouldFormatReportLine(self):
        self.assertEqual("<strong>Quantity-</strong> 100",
                self.formattedTextGenerator.generateReportLine("Quantity", "100"))
        self.assertEquals("<strong>Value-</strong> INR 1220",
                self.formattedTextGenerator.generateReportLine("Value", "INR 1220"))

class InventoryReportManagerTests(TestCase):
    CURRENT_MONTH = 5
    CURRENT_YEAR = 2013
    def _addWarehouseSnapshot(self, warehouseName, year, month,
                              appleQuantity, appleUnitValue,
                              boseQuantity, boseUnitValue):
        warehouseSnapshot = self.warehouseSnapshotDao.addWarehouseSnapshot(warehouseName, year, month)
        warehouseSnapshot.skus.append(Sku(TestNames.SKU_APPLE, appleQuantity, appleUnitValue))
        warehouseSnapshot.skus.append(Sku(TestNames.SKU_BOSE, boseQuantity, boseUnitValue))
    
    def _addCurrentMonthSnapshot(self, warehouseName):
        self._addWarehouseSnapshot(warehouseName, self.CURRENT_YEAR,
                self.CURRENT_MONTH, 20, 32000, 5, 18000)

    def _addTwoMonthsSnapshot(self, warehouseName):
        self._addWarehouseSnapshot(warehouseName, self.CURRENT_YEAR,
                self.CURRENT_MONTH - 1, 12, 35000, 5, 19000)
        self._addCurrentMonthSnapshot(warehouseName)

    def setUp(self):
        self.warehouseSnapshotDao = WarehouseSnapshotDaoMemoryImpl()
        self.inventoryReportManager = InventoryReportManager(self.warehouseSnapshotDao)

    def tearDown(self):
        self.inventoryReportManager = None

    def testShouldGenerateWarehouseReport(self):
        self._addTwoMonthsSnapshot(TestNames.WAREHOUSE_AGRA)

        warehouseReport = self.inventoryReportManager.generateWarehouseReport(
                TestNames.WAREHOUSE_AGRA, self.CURRENT_YEAR, self.CURRENT_MONTH)
        self.assertIsNotNone(warehouseReport)
        self.assertEqual(2, warehouseReport.skus)
        self.assertEqual(25, warehouseReport.units)
        self.assertEqual(730000, warehouseReport.value)
        self.assertEqual(215000, warehouseReport.changeInValue)

    def testShouldGenerateNullWarehouseReportIfMissingData(self):
        warehouseReport = self.inventoryReportManager.generateWarehouseReport(
                TestNames.WAREHOUSE_AGRA, self.CURRENT_YEAR, self.CURRENT_MONTH)
        self.assertIsNone(warehouseReport)
        
        self._addCurrentMonthSnapshot(TestNames.WAREHOUSE_AGRA)
        warehouseReport = self.inventoryReportManager.generateWarehouseReport(
                TestNames.WAREHOUSE_AGRA, self.CURRENT_YEAR, self.CURRENT_MONTH)
        self.assertIsNone(warehouseReport)
    
    def testShouldGenerateSkuReport(self):
        self._addTwoMonthsSnapshot(TestNames.WAREHOUSE_AGRA)
        self._addTwoMonthsSnapshot(TestNames.WAREHOUSE_BANGALORE)
        
        skuReport = self.inventoryReportManager.generateSkuReport(
                TestNames.SKU_APPLE, self.CURRENT_YEAR, self.CURRENT_MONTH)
        self.assertIsNotNone(skuReport)
        self.assertEqual(40, skuReport.units)
        self.assertEqual(1280000, skuReport.value)
        self.assertEqual(440000, skuReport.changeInValue)
    
    def testShouldGenerateSkuWarehouseReport(self):
        self._addTwoMonthsSnapshot(TestNames.WAREHOUSE_AGRA)
        self._addTwoMonthsSnapshot(TestNames.WAREHOUSE_BANGALORE)
        
        skuWarehouseReport = \
                self.inventoryReportManager.generateSkuWarehouseReport(
                        TestNames.SKU_APPLE, TestNames.WAREHOUSE_AGRA,
                        self.CURRENT_YEAR, self.CURRENT_MONTH)
        self.assertIsNotNone(skuWarehouseReport)
        self.assertEqual(20, skuWarehouseReport.units)
        self.assertEqual(640000, skuWarehouseReport.value)
        self.assertEqual(220000, skuWarehouseReport.changeInValue)
