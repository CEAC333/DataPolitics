
from os import listdir
from os.path import isfile, join
import os


mypath = os.path.dirname(os.path.abspath(__file__))
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)