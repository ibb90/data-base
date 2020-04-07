import struct


class SystemCatalog:
    NumberOfTypes = 0
    Types = []

    def __init__(self):
        try:
            self.SystemCatalogFile = open("SystemCatalog", "rb")
            print("SystemCatalogFile is opened successsively")
            self.NumberOfTypes, = struct.unpack(
                "i", self.SystemCatalogFile.read(4))
            print("There are", self.NumberOfTypes, "kinds of Types")
        except:
            print("There is no such a file...")
            self.createCatalogFile()

    def createCatalogFile(self):
        print("Creating a new SystemCatalog File...")
        self.SystemCatalogFile = open("SystemCatalog", "wb")
        self.SystemCatalogFile.write(struct.pack("i", 0))
        self.SystemCatalogFile.close()

    def readCatalogFile(self):
        print("SystemCatalogFile is being read")

    def addNewType(self, Type):
        self.NumberOfTypes += 1
        self.Types.append(Type)

    def writeback(self):
        print("writing back on System Catalog File...")
        self.SystemCatalogFile = open("SystemCatalog", "wb")
        self.SystemCatalogFile.write(struct.pack("i", self.NumberOfTypes))
        self.SystemCatalogFile.close()
        for i in range(self.NumberOfTypes):
            self.SystemCatalogFile = open("SystemCatalog", "w")
            self.SystemCatalogFile.write(self.Types[i].TypeName)
            self.SystemCatalogFile.close()
            self.SystemCatalogFile = open("SystemCatalog", "wb")
            self.SystemCatalogFile.write(
                struct.pack("i", self.Types[i].NumberOfFiles))
            self.SystemCatalogFile.write(
                struct.pack("i", self.Types[i].NumberOfFields))
            for k in range(self.Types[i].NumberOfFields):
                self.SystemCatalogFile.write(
                    self.Types[i].Fields_Names[k])
        self.SystemCatalogFile.close()
