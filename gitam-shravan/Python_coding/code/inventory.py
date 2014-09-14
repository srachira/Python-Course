__author__ = 'SuSh'
from models import*
class FormattedTextGenerator:
    def __init__(self):
        self.tag="<{0}{1}{2}>"
        self.symbol="-"
        self.start_tag=self.tag.format("","h3","")
        self.end_tag=self.tag.format("/","h3","")
        self.strong_start=self.tag.format("","strong","")
        self.strong_end=self.tag.format("/","strong","")

    # def tag_format(self,tag):
    #     self.start_tag=self.tag.format("",tag,"")
    #     self.end_tag=self.tag.format("/",tag,"")

    def formatting(self,warehouseName):
        return self.start_tag+"{0}"+self.symbol+" "+warehouseName+self.end_tag

    def generateWarehouseReportTitle(self, warehouseName):
        return self.formatting(warehouseName).format("Warehouse")

    def generateSkuReportTitle(self,warehouseName):
        return self.formatting(warehouseName).format("SKU")

    def generateSkuWarehouseReportTitle(self,SKUname,Warehousename):
        return self.start_tag+"SKU"+self.symbol+" "+SKUname+", "+"Warehouse"+self.symbol+" "+Warehousename+self.end_tag

    def generateReportLine(self,description,amount):
        return self.strong_start+description +self.symbol+self.strong_end+" "+amount

    def generateErroneousReportTitle(self):
        return self.tag.format("","h3",' class="text-error"')+'Error generating your report!'+self.end_tag

class InventoryReportManager:
    def __init__(self, warehouseSnapshotDao):
        self.warehouseSnapshotDao = warehouseSnapshotDao

    def generateWarehouseReport(self, warehouseName, year, month):
        prev_month = month - 1
        prev_year = year
        if prev_month < 0:
            prev_year-= 1
            prev_month += 12

        currentWarehouseSnapshot = self.warehouseSnapshotDao.findOne((
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "name", warehouseName),
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "year", year),
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "month", month)))
        previousWarehouseSnapshot = self.warehouseSnapshotDao.findOne((
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "name", warehouseName),
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "year", prev_year),
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "month", prev_month)))

        if currentWarehouseSnapshot == None or previousWarehouseSnapshot == None:
            return None
        previousValue=0
        warehouseReport = WarehouseReport()
        warehouseReport.skus = len(currentWarehouseSnapshot.skus)
        for  x in currentWarehouseSnapshot.skus:
            warehouseReport.units += x.quantity
        for  x in currentWarehouseSnapshot.skus:
            warehouseReport.value +=x.quantity*x.unitValue
        for  x in previousWarehouseSnapshot.skus:
            previousValue +=x.quantity*x.unitValue

        warehouseReport.changeInValue = warehouseReport.value - previousValue

        return warehouseReport

    def generateSkuReport(self, skuName, year, month):
        previousMonth = month - 1
        previousYear = year
        if previousMonth < 0:
            previousYear -= 1
            previousMonth += 12

        currentWarehouseSnapshots = self.warehouseSnapshotDao.find((
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "year", year),
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "month", month)))
        previousWarehouseSnapshots = self.warehouseSnapshotDao.find((
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "year", previousYear),
                self.warehouseSnapshotDao.createEqualsQueryFilter(
                        "month", previousMonth)))

        skuReport = Report()
        for warehouseSnapshot in currentWarehouseSnapshots:
            for sku in warehouseSnapshot.skus:
                if sku.name == skuName:
                    skuReport.units += sku.quantity
                    skuReport.value += sku.quantity * sku.unitValue
        previousValue = 0
        for warehouseSnapshot in previousWarehouseSnapshots:
            for sku in warehouseSnapshot.skus:
                if sku.name == skuName:
                    previousValue += sku.quantity * sku.unitValue
        skuReport.changeInValue= skuReport.value - previousValue
        return skuReport

    def generateSkuWarehouseReport(self, skuName, warehouseName, year, month):
        previousMonth = month - 1
        previousYear = year
        if previousMonth < 0:
            previousYear -= 1
            previousMonth += 12

        currentWarehouseSnapshot = self._getWarehouseSnapshot(warehouseName,
                year, month)
        previousWarehouseSnapshot = self._getWarehouseSnapshot(warehouseName,
                previousYear, previousMonth)

        if currentWarehouseSnapshot == None or previousWarehouseSnapshot == None:
            return None

        skuReport = Report()
        for sku in currentWarehouseSnapshot.skus:
            if sku.name == skuName:
                skuReport.units += sku.quantity
                skuReport.value += sku.quantity * sku.unitValue
        previousValue = 0
        for sku in previousWarehouseSnapshot.skus:
            if sku.name == skuName:
                previousValue += sku.quantity * sku.unitValue
        skuReport.changeInValue= skuReport.value - previousValue
        return skuReport
