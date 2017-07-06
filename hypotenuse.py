import maya.cmds as cmds
import math

p1=(cmds.getAttr('locator1.translateX'),cmds.getAttr('locator1.translateY'),cmds.getAttr('locator1.translateZ'))
p2=(cmds.getAttr('locator2.translateX'),cmds.getAttr('locator2.translateY'),cmds.getAttr('locator2.translateZ'))
p3=(cmds.getAttr('locator3.translateX'),cmds.getAttr('locator3.translateY'),cmds.getAttr('locator3.translateZ'))

def length(e1,e2):
	return math.sqrt(math.pow(e1[0]-e2[0],2)+math.pow(e1[1]-e2[1],2)+math.pow(e1[2]-e2[2],2))
	
a=length(p1,p3)
b=length(p2,p3)
c=length(p1,p2)

clipDistance=c*((b**2+c**2-a**2)/(2*b*c))

cmds.setAttr('pPlane1.translateZ',clipDistance)