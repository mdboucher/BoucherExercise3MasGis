import arcpy

arcpy.env.workspace = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb\Exercise 3.gdb"
arcpy.env.overwriteOutput = True

arcpy.AddField_management('CallsforService','Crime_Explanation','TEXT')
print('New field added!')

arcpy.MakeFeatureLayer_management(r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb\Exercise 3.gdb\CallsforService","CallsforService_lyr")
print('Feature layer created!')

data = arcpy.SelectLayerByAttribute_management('CallsforService_lyr', 'NEW_SELECTION', "CFSType = 'Burglary Call'")
print('Completed select by attribute')

inTable = data
fieldName = 'Crime_Explanation'
expression = "This is a burglary"
print('All Burglary Call fields updated!')