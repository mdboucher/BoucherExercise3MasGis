import arcpy
import csv

dB = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb"
filter1 = "OffenseCus = 'BURGLARY FORCE' AND locationTranslation ='Residence/Home'"

fieldNames = ['primary_key', 'occ_dt', 'obfAddress', 'x_rand', 'y_rand', 'disclaimer', 'place_name', 'OffenseCustom', 'locationTranslation']
fields = ['OffenseCustom', 'locationTranslation']
with open('burglaries.csv', 'w') as csvFile:
    fileWriter = csv.writer(csvFile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    fileWriter.writerow(fieldNames)
    with arcpy.da.SearchCursor(dB, fieldNames, filter1,) as cursor:
        fileWriter.writerows(cursor)
print(uniqueValues)