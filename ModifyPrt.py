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
                if len(row.split(";")[2].split("_")) != 1:
                    new_name = dict()
                    ending = row.split(";")[2].split("_")[-1]
                    new_data = FreeCom(MsrRecord, row).modifyString(record_data)
                    new_name["MN"] = record_data["MN"] + "_" + ending
                    new_data = FreeCom(MsrRecord, new_data).modifyString(new_name)
                else:
                    new_data = FreeCom(MsrRecord, row).modifyString(record_data)
                self.newfile.append(new_data)
            elif "M54321" in row:
                self.newfile.append(row.replace("M54321", record_data["MN"]))
            elif "54321" in row:
                if "Variabel" in row:
                    row = row.replace("Variabel", record_data["LT"])
                self.newfile.append(row.replace("54321", record_data["MN"]))
            else:
                self.newfile.append(row)