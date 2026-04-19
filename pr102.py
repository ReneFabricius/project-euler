import numpy.linalg
from math import atan, sin, cos, pi

def problem102():
    n = "p102_triangles.txt"
    f = open(n, 'r')
    count = 0
    for t in f:
        T = t.split(",")
        T = [int(x) for x in T]
        T = [numpy.matrix([[T[0]], [T[1]], [1]]), numpy.matrix([[T[2]], [T[3]], [1]]), numpy.matrix([[T[4]], [T[5]], [1]])]
        Tr = numpy.matrix([[1, 0, -T[0][0]],[0, 1, -T[0][1]],[0, 0, 1]])
        Tt = [Tr*p for p in T]
        Ot = Tr*numpy.matrix([[0], [0], [1]])
        
        if not (Ot[1] == 0 and Ot[0] >= 0):
            ra = 0
            if Ot[0] == 0:
                if Ot[1] > 0:
                    ra = -pi/2
                else:
                    ra = pi/2
            else:
                ra = -atan(Ot[1]/Ot[0])
                if Ot[0] < 0:
                    if Ot[1] > 0:
                        ra -= pi
                    else:
                        ra += pi
            
            Rt = numpy.matrix([[cos(ra), -sin(ra), 0], [sin(ra), cos(ra), 0], [0, 0, 1]])
            Tt = [Rt*p for p in Tt]
            Ot = Rt*Ot
        
        Ba = 0
        if Tt[1][0] == 0:
            if Tt[1][1] > 0:
                Ba = pi/2
            else:
                Ba = -pi/2
        else:
            Ba = atan(Tt[1][1]/Tt[1][0])
            if Tt[1][0] < 0:
                if Tt[1][1] > 1:
                    Ba += pi
                else:
                    Ba -= pi
                    
        Ca = 0
        if Tt[2][0] == 0:
            if Tt[2][1] > 0:
                Ca = pi/2
            else:
                Ca = -pi/2
        else:
            Ca = atan(Tt[2][1]/Tt[2][0])
            if Tt[2][0] < 0:
                if Tt[2][1] > 1:
                    Ca += pi
                else:
                    Ca -= pi
        
        if (Ca >= 0 and Ba <= 0) or (Ca <= 0 and Ba >= 0):
            its = Tt[1][0] - Tt[1][1]*(Tt[2][0] - Tt[1][0])/(Tt[2][1] - Tt[1][1])
            if its >= Ot[0]:
                count += 1
    
    f.close()
    return count
    
def problem102cross():
    n = "p102_triangles.txt"
    f = open(n, 'r')
    count = 0
    for t in f:
        T = t.split(",")
        T = [int(x) for x in T]
        T = [numpy.array([T[0], T[1], 0]), numpy.array([T[2], T[3], 0]), numpy.array([T[4], T[5], 0])]
        c1 = numpy.cross(T[1] - T[0], -T[0])
        c2 = numpy.cross(T[2] - T[1], -T[1])
        c3 = numpy.cross(T[0] - T[2], -T[2])
        if (c1[2] > 0 and c2[2] > 0 and c3[2] > 0) or (c1[2] < 0 and c2[2] < 0 and c3[2] < 0):
            count += 1
    
    f.close()
    return count
    
            
