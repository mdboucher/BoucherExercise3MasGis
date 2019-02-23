import arcpy

arcpy.env.workspace = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb"

in_table = 'CallsforService'
field_name = 'Crime_Explanation'

arcpy.AddField_management(in_table,field_name,'TEXT')

class_field = ['CFSType','Crime_Explanation']
 
with arcpy.da.UpdateCursor(in_table,field_name) as cursor:
    for row in cursor:
        if row[0] == 'Burlary Call':
            row[1] = 'This is a Burglary'

            cursor.updateRow(row)

print('Feature layer created!')
