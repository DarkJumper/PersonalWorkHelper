import csv


class DataSet:

    def __init__(self, filepath):
        self.file_data = dict()
        with open(filepath, newline="") as file:
            csv_read_out = csv.reader(
                file,
                delimiter=";",
                )
            next(csv_read_out, None)
            for count, row in enumerate(csv_read_out):
                csv_data = {
                    "STD": row[0],
                    "RECORD": {
                        "MN": row[1],
                        "KT": row[2].ljust(12)[:12],
                        "LT": row[3].ljust(30)[:30]
                        },
                    "PARADATA": {
                        "Bt0": ["Bt0", "5", "MTEXT",
                                str(len(row[5].ljust(7)[:7])), row[5].ljust(7)[:7]],
                        "Bt1": ["Bt1", "5", "MTEXT",
                                str(len(row[6].ljust(7)[:7])), row[6].ljust(7)[:7]],
                        "Mp": ["Mp", "5", "MPRIO", str(len(row[7])), str(row[7])],
                        "Mt": ["Mt", "5", "MTEXT",
                               str(len(row[6].ljust(7)[:7])), row[6].ljust(7)[:7]],
                        "Mba": ["Mba", "5", "FLOAT", str(len(row[8])),
                                str(row[8])],
                        "Mbe": ["Mbe", "5", "FLOAT", str(len(row[9])),
                                str(row[9])],
                        "Dim": ["Dim", "3", "DIM",
                                str(len(row[10].ljust(7)[:7])), row[10].ljust(7)[:7]],
                        "Gw1": ["Gw1", "5", "FLOAT", str(len(row[11])),
                                str(row[11])],
                        "Gt1": ["Gt1", "13", "CUSTELLIST_1",
                                str(len(row[12])), str(row[12])],
                        "Lf1": ["Lf1", "5", "CHECK", str(len(row[13])),
                                str(row[13])],
                        "Mp1": ["Mp1", "5", "MPRIO", str(len(row[14])),
                                str(row[14])],
                        "Mt1": ["Mt1", "5", "MTEXT",
                                str(len(row[15].ljust(7)[:7])), row[15].ljust(7)[:7]],
                        "Gw2": ["Gw2", "5", "FLOAT", str(len(row[16])),
                                str(row[16])],
                        "Gt2": ["Gt2", "13", "CUSTELLIST_1",
                                str(len(row[17])), str(row[17])],
                        "Lf2": ["Lf2", "5", "CHECK", str(len(row[18])),
                                str(row[18])],
                        "Mp2": ["Mp2", "5", "MPRIO", str(len(row[19])),
                                str(row[19])],
                        "Mt2": ["Mt2", "5", "MTEXT",
                                str(len(row[20].ljust(7)[:7])), row[20].ljust(7)[:7]],
                        "Gw3": ["Gw3", "5", "FLOAT", str(len(row[21])),
                                str(row[21])],
                        "Gt3": ["Gt3", "13", "CUSTELLIST_1",
                                str(len(row[22])), str(row[22])],
                        "Lf3": ["Lf3", "5", "CHECK", str(len(row[23])),
                                str(row[23])],
                        "Mp3": ["Mp3", "5", "MPRIO", str(len(row[24])),
                                str(row[24])],
                        "Mt3": ["Mt3", "5", "MTEXT",
                                str(len(row[25].ljust(7)[:7])), row[25].ljust(7)[:7]],
                        "Gw4": ["Gw4", "5", "FLOAT", str(len(row[26])),
                                str(row[26])],
                        "Gt4": ["Gt4", "13", "CUSTELLIST_1",
                                str(len(row[27])), str(row[27])],
                        "Lf4": ["Lf4", "5", "CHECK", str(len(row[28])),
                                str(row[28])],
                        "Mp4": ["Mp4", "5", "MPRIO", str(len(row[29])),
                                str(row[29])],
                        "Mt4": ["Mt4", "5", "MTEXT",
                                str(len(row[30].ljust(7)[:7])), row[30].ljust(7)[:7]]
                        }
                    }
                self.file_data[count] = csv_data

    @property
    def data(self):
        return self.file_data