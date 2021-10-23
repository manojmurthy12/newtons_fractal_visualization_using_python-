add_library('gifAnimation')
import math


import random


def distance(a,b):
    return pow((a.real-b.real),2)+pow((a.imag-b.imag),2)
def nearer_root(root1,root2,root3):
    if root1 < root2 and root1 < root3:
        return 'red'
    if root2 < root1 and root2 < root3:
        return 'blue'
    if root3 < root1 and root3 <root2:
        return 'green'

xmin = -4
xmax = 4
ymin = -4
ymax = 4
rangex = xmax - xmin
rangey = ymax - ymin
all_roots=[]
def printRoots(n):
    all_roots=[]


    theta = PI*2/n;
    for k in range(n):
    
        # // calculate the real and imaginary part of root
        # actual_root=complex(cos(k*theta),sin(k*theta))
        all_roots.append(complex(cos(k*theta),sin(k*theta)))
    
    return all_roots


def setup():
    global xscl, yscl
    size(1200, 1200)
    colorMode(RGB)
    noStroke()
    xscl = float(rangex) / width
    yscl = float(rangey) / height
    global exporter
    size(800, 800)
    exporter = GifMaker(this, "forblogvoronoi.gif")
    exporter.setRepeat(0)     # infinite repeat
    exporter.setQuality(100)  # test values
    exporter.setDelay(200)

def draw():
    for n1 in range(3,4):
        nthroot=n1
        roots=printRoots(nthroot)
        # roots=[complex(1,1),complex(1,-1),complex(-2,0)] 
        root_distance=[]
        k=[]
        l=[]
        m=[]
        # for i in range(len(roots)):
        #     k.append(random.randint(0, 255))
        #     l.append(random.randint(0, 255))
        #     m.append(random.randint(0, 255))

        k=[137,68,210]
        l=[74,81,239]
        m=[94,107,252]
        for t in range(20):
            for x in range(width):
                for y in range(height):
                    root_distance=[]
                    Finitial=complex(xmin + x * xscl,ymin + y * yscl)
                    if nthroot>2:
                        for i in range(t):
                            F=((Finitial**nthroot)-1)    #should write a function for power in complex 
                            F_dash=((nthroot-1)*(Finitial**(nthroot-1)))
                            if F_dash != complex(0,0):
                                Finitial=Finitial-(F/F_dash)
            
           
                    for i in range(len(roots)):
                        root_distance.append(distance(Finitial,roots[i]))
                    nearest_root=min(root_distance)
                    fill(k[root_distance.index(nearest_root)],l[root_distance.index(nearest_root)],m[root_distance.index(nearest_root)])

            
                    rect(x,y,1,1)
            exporter.addFrame() 
            if keyPressed and key == 'e':
                exporter.finish()
                print("gif saved, exit")
                exit() 
    print('done')   
    
    
            # else:

                
                

            
                
