import rhinoscriptsyntax as rs;



def printPoints(array):
    for i in array:
        print(str(i[0])+ ','+ str(i[1]) + "," + str(i[2]))


x = [(0,0,3),(1,0,4),(2,3,0),(3,5,0)]
# if(y != 0):
#     a = area / y
#     b = y
#     x = [(0,0,3),(1,0,4),(2,3,0),(3,5,0)]
printPoints(x)
