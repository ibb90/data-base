import struct
from SystemCatalog import SystemCatalog
from FieldsAreNotValid import FieldsAreNotValid
from Type import Type


def Check_If_Type_Exits(TypeName, SystemCatalog):
    print(TypeName, SystemCatalog.NumberOfTypes)
    if SystemCatalog.NumberOfTypes > 0:
        for i in range(SystemCatalog.NumberOfTypes):
            if SystemCatalog.Types[i] == TypeName:
                return True

    return False


class DLL:

    def __init__(self, SystemCatalog):
        self.SystemCatalog = SystemCatalog

    def Create_Type(self, TypeName, N, Fields_Names):
        print("Creating Type...")
        if not Check_If_Type_Exits(TypeName, self.SystemCatalog):
            newType = Type(TypeName, N, Fields_Names)
            self.SystemCatalog.addNewType(newType)





r1 = SystemCatalog()

r2 = DLL(r1)

try:

    r2.Create_Type("Humans", 3, ["yas", "age", "length"])

except Exception as e:
    print(e)

r1.writeback()
