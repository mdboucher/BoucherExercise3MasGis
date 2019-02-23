import arcpy

dB = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb"
arcpy.env.workspace = dB
arcpy.env.overwriteOutput = True

target = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb\Tracts"
join = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb\General_Offense"
output = r"C:\Users\mdbou\OneDrive\ASU MAS-GIS\_GIS 610\Assignments\Exercise 3.gdb\OffensiveTracts"

arcpy.SpatialJoin_analysis(target,join,output)

print('Mission Accomplished!')