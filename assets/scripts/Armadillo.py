""" type: SofaContent """

import Sofa
from splib.objectmodel import SofaPrefab


def BasicCollisionStuff(node):
    node.createObject('CollisionPipeline', verbose="0", draw="0")
    node.createObject('BruteForceDetection', name="N2")
    node.createObject('MinProximityIntersection', name="Proximity", alarmDistance="0.8", contactDistance="0.5")
    node.createObject('CollisionResponse', name="Response", response="default")


@SofaPrefab
class ArmadilloPrefab:
    def __init__(self, node):
        """ Creates a simple node called Armadillo,
            Containing some basic stuff to load an Armadillo with its physics and visual model
        """

        self.node = node.createChild("ArmadilloPrefab")

        armadillo = self.node.createChild('Armadillo')
        armadillo.createObject('EulerImplicit', name="cg_odesolver", printLog="false",
                               rayleighStiffness="0.1", rayleighMass="0.1")
        armadillo.createObject('CGLinearSolver', iterations="25", name="linear solver", tolerance="1.0e-9", threshold="1.0e-9")
        armadillo.createObject('SparseGrid', n="8 6 7", fileTopology="mesh/Armadillo_verysimplified.obj")
        armadillo.createObject('MechanicalObject', dx="70", ry="25")
        armadillo.createObject('HexahedronFEMForceFieldAndMass', youngModulus="20000", poissonRatio="0.3",
                               method="large", density="10", updateStiffnessMatrix="false", printLog="0")
        visu = armadillo.createChild("Visu")
        visu.createObject('OglModel', name="Visual", fileMesh="mesh/Armadillo_simplified.obj", color="1 .4 0 1")
        visu.createObject('BarycentricMapping', input="@..", output="@Visual")
        collision = armadillo.createChild("Collision")
        collision.createObject('MeshObjLoader', name="loader", filename="mesh/Armadillo_verysimplified.obj")
        collision.createObject('Mesh', src="@loader")
        collision.createObject('MechanicalObject', src="@loader")
        collision.createObject('Triangle', contactStiffness="1")
        collision.createObject('Line', contactStiffness="1")
        collision.createObject('Point', contactStiffness="1")
        collision.createObject('BarycentricMapping')

        
@SofaPrefab
class SaladBowl:
    def __init__(self, node):
        """ Creates a node called SaladBowl,
            Containing the stuff to load build a Salad Bowl with its physics and visual model
        """

        self.node = node.createChild("SaladBowl")
        self.node.createObject('MeshObjLoader', name="meshLoader", filename="mesh/SaladBowl.obj")
	self.node.createObject('Mesh', src="@meshLoader" )
	self.node.createObject('MechanicalObject', scale="1",  dx="0", dy="0", dz="0", rx="0", ry="0", rz="0")
	self.node.createObject('Triangle', name="Floor", moving="false", simulated="false", contactStiffness="10")
	self.node.createObject('Line', name="Floor" ,moving="false", simulated="false", contactStiffness="10")
	self.node.createObject('Point', name="Floor", moving="false", simulated="false", contactStiffness="10" )
	self.node.createObject('OglModel', name="FloorV", fileMesh="mesh/SaladBowl.obj",
                               texturename="textures/floor.bmp", color="1 1 1 1", scale="1",
                               dx="0", dy="0", dz="0", rx="0", ry="0", rz="0" )
