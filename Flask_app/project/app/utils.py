import xlrd
import sqlite3
from datetime import datetime
import os

directory='/work/www/cmd/Flask_app/project/app/static/'

for filename in os.listdir(directory):
    f=os.path.join(directory,filename)

    if os.path.isfile(f):
        f=str(f)
        f1=f.replace(" ","_")
        os.rename(f,f1)


