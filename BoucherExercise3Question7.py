import arcpy

arcpy.env.workspace = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb"

feature_in = 'CallsforService'
destination = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb"
feature_out = 'FightNight'
delimitedField = arcpy.AddFieldDelimiters(arcpy.env.workspace, 'CFSType')
expression = delimitedField + " = 'Fight Call'"

arcpy.FeatureClassToFeatureClass_conversion(feature_in, destination, feature_out, expression)

print('Subset feature class created!')