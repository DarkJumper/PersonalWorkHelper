import os
import shutil

from ModifyPrt import ModifyPrt
from DataSet import DataSet

filepath = "/Users/peterschwarz/VS Code Projekte/PersonalWorkHelper/test.csv"

csv_read_out = DataSet(filepath).data
for row in csv_read_out.keys():
    new_filename = os.path.abspath(os.getcwd()) + "/outfiles/" + csv_read_out[row]['RECORD']["MN"] + ".prt"
    std_filename = os.path.abspath(os.getcwd()) + "/std/" + csv_read_out[row]['STD'] + "_Standart.prt"
    shutil.copyfile(std_filename, new_filename)
    mod_prt = ModifyPrt(new_filename)
    mod_prt.read()
    mod_prt.modify(csv_read_out[row]['RECORD'], csv_read_out[row]['PARADATA'])
    mod_prt.write()
