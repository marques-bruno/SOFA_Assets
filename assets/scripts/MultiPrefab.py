""" type: SofaContent """
#encoding:utf-8

import Sofa

from splib.objectmodel import SofaPrefab

@SofaPrefab
class APrefab:
    def __init__(self, parent):
        """ Prefab en carton """
        self.node = parent.createChild("APrefab")
        self.node.addNewData("angle", "DynamicProperty", "Blah", "float", 45.0)

        self.node.createObject("MechanicalObject", name="titi")
        self.node.createObject("MechanicalObject", name="toto")
        self.node.createObject("MechanicalObject", name="tata")
        visual = self.node.createChild("Visual")
        visual.createObject("MechanicalObject", name="tata")

def foo(self, parent):
    """ Prefab en papier """
    self.node = parent.createChild("APrefab")
    self.node.addNewData("angle", "DynamicProperty", "Blah", "float", 45.0)
    
    self.node.createObject("MechanicalObject", name="titi")
    self.node.createObject("MechanicalObject", name="toto")
    self.node.createObject("MechanicalObject", name="tata")
    visual = self.node.createChild("Visual")
    visual.createObject("MechanicalObject", name="tata")

class MyController(Sofa.PythonScriptController):
    """ Controlleur en carton """
    def __init__(self, node):
        self.node = node

    def onKeyPressed(self, key):
        print (key + ' pressed')


class MyEngine(Sofa.PythonScriptDataEngine):
    """ A completely useless & empty engine """
    def __init__(self, node):
        self.node = node


def createScene(node):
    """ A stupid sofa scene """
    print "    n = node.createChild('An empty node in root')"

    n = node.createChild("An empty node in root")
    print "    APrefab(n)"
    APrefab(n)

    print '    MyEngine(node)'
    MyEngine(node)

    print "    MyController(node)"
    MyController(node)
