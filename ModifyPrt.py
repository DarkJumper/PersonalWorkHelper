from FreeCom.FreeCom.Commands import MsrRecord, ParaData
from FreeCom.FreeCom import FreeCom


class ModifyPrt:

    def __init__(self, filepath):
        self.data = list()
        self.newfile = list()
        self.filepath = filepath

    def read(self):
        with open(self.filepath, encoding="utf-16") as file:
            for row in file:
                self.data.append(row)

    def write(self):
        with open(self.filepath, "w", encoding="utf-16-le") as new:
            new.write("\ufeff")
            for element in self.newfile:
                new.write(element)

    def modify(self, record_data, para_data):
        for row in self.data:
            if "Standart" in row:
                self.newfile.append(row.replace("Standart", record_data["MN"]))
            elif "[PARA:PARADATA]" in row:
                self.newfile.append(FreeCom(ParaData, row).modifyString(para_data))
            elif "[MSR:RECORD]" in row:
                self.newfile.append(FreeCom(MsrRecord, row).modifyString(record_data))
            elif "54321" in row:
                if "Variabel" in row:
                    row = row.replace("Variabel", record_data["LT"])
                self.newfile.append(row.replace("54321", record_data["MN"]))
            else:
                self.newfile.append(row)