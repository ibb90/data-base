import FieldsAreNotValid


class Type:
    TypeName = ""
    NumberOfFields = 0
    NumberOfFiles = 0
    Fields_Names = []

    def __init__(self, TypeName, NumberOfFields, Fields_Names):
        self.control()
        self.TypeName = TypeName
        self.NumberOfFields = NumberOfFields
        self.NumberOfFiles = 0
        self.Fields_Names = Fields_Names

    def control(self):
        if(self.NumberOfFields > 64) or len(self.Fields_Names) != self.NumberOfFields:
            raise FieldsAreNotValid(
                "Number of fields are not in desired interval")
