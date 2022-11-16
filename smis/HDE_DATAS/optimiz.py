import os
import numpy as np
import pandas as pd
import pandas_access as mdb

class Optimiz:
    path_csv = {"table":[], "file": {}}
    def __init__(self, filePath):
        self.filePath = filePath
        self.path = filePath.replace('.csv', '')

    def load_csv(self, filename):
        self.data_csv = pd.read_csv(filename)
        return self.data_csv

    def load_data(self):
        return self.data_csv

    def mdb_to_csv(self):
        for tbl in mdb.list_tables(self.filePath):
            os.makedirs('%s/datasets'%(self.path), exist_ok=True) #create directory
            saveFile = "%s/datasets/data_%s.csv"%(self.path,tbl.lower())
            cmd_command = "mdb-export %s %s > %s"%(self.filePath,tbl,saveFile)
            # !{cmd_command} # Run shell by `!`
            self.path_csv['table'].append(tbl)
            self.path_csv['file'][tbl] = saveFIle
