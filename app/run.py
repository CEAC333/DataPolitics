#!/usr/bin/env python
# -*- coding: latin-1 -*-

from os import listdir
from os.path import isfile, join
import os


mypath = os.path.dirname(os.path.abspath(__file__))[:-4]+'/resources/' #remove /app from mypath and add /resources

print(mypath) 

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# CSV
import csv

with open('db.csv', 'w', newline='', encoding='latin-1') as csvfile:
    fields = ['NOMBRE', 'FECHA_AFILIACION', 'ENTIDAD', 'MUNICIPIO', 'PARTIDO_POLITICO']
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    for fname in onlyfiles[0:33]:#[0:1]:
    	with open(mypath+''+fname+'') as f:
    		content = f.readlines()
    		for line in content:
    			lineList = line.split('|')
    			partido_estado_municipio = fname.split('_')
    			#print(len(lineList))

    			#Date Format (mm/dd/yy)
    			try:
    				datef = lineList[1].split('/')
    				print(datef)
    				print(len(datef))
    				datefinalf = datef[1].zfill(2)+'/'+datef[0].zfill(2)+'/'+datef[2]
    			except:
    				datefinalf = lineList[1]

    			writer.writerow(
    								{
    									'NOMBRE'			: lineList[0].encode('latin-1', 'ignore').decode('latin-1', 'ignore'), 
    									'FECHA_AFILIACION'	: datefinalf, 
    									'ENTIDAD'			: lineList[2].encode('latin-1', 'ignore').decode('latin-1', 'ignore'), 
    									'MUNICIPIO'			: partido_estado_municipio[2][:-4].encode('latin-1', 'ignore').decode('latin-1', 'ignore'), 
    									'PARTIDO_POLITICO'	: partido_estado_municipio[0].encode('latin-1', 'ignore').decode('latin-1', 'ignore')
    								})
    			print({'NOMBRE': lineList[0], 'FECHA_AFILIACION': lineList[1], 'ENTIDAD': lineList[2], 'MUNICIPIO': partido_estado_municipio[2][:-4], 'PARTIDO_POLITICO': partido_estado_municipio[0]})