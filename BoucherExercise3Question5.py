import arcpy

folderName = r'C:\Users\mdbou\OneDrive\Python Projects\Exercise3'
fgdbName = 'Exercise3Question5.gdb'

try:
    arcpy.CreateFileGDB_management(folderName,fgdbName)
    print('Successfully created a gdb')
except Exception as err:
    print('Sorry the folder does not exist. Please try again.')

    print(err.args[0])
current_workspace = r'C:\Users\mdbou\OneDrive\Python Projects\Exercise3\Exercise3Question5.gdb'

geometry_type = "POLYGON"

spatial_reference = arcpy.SpatialReference(102100)

featureClassNamesList = ['CapitalCities', 'Landmarks', 'HistoricPlaces', 'StateNames', 'Nationalities', 'Rivers']

arcpy.env.workspace = current_workspace

arcpy.env.overwriteOutput = True

def createFeatureClass(in_fc_name):

    arcpy.CreateFeatureclass_management(current_workspace,in_fc_name, geometry_type,"","Disabled","Disabled",spatial_reference)
    print('Feature Class ' + in_fc_name + ' was successfully created.')

createFC = [createFeatureClass(fc) for fc in featureClassNamesList]

print('All Done')
