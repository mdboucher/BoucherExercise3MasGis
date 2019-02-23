import arcpy

arcpy.env.workspace = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb"

field = 'CallsforService'
output = arcpy.GetCount_management(field)

print('{} has {} records contained within it!'.format(field, output[0]))
