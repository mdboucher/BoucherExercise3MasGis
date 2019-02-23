import arcpy

arcpy.env.workspace = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb"
arcpy.env.overwriteOutput = True

dB = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb"
fc = "Mountains_Majesty"
Prpl = 'Purple'
domain = 'Types of Purple'

arcpy.CreateFeatureclass_management (dB, fc, 'POINT')
print('Feature Class Created!')

arcpy.AddField_management(fc, Prpl, "TEXT")
print('Field Created!')

arcpy.CreateDomain_management(dB,domain,Prpl,"TEXT","CODED")

arcpy.AddCodedValueToDomain_management(dB, domain, '1','Amethyst')
arcpy.AddCodedValueToDomain_management(dB, domain, '2','Spruce')
arcpy.AddCodedValueToDomain_management(dB, domain, '3', 'Violet')
arcpy.AddCodedValueToDomain_management(dB, domain, '4', 'Lavendar')
arcpy.AddCodedValueToDomain_management(dB, domain, '5', 'Eggplant')
print('Types added!')

