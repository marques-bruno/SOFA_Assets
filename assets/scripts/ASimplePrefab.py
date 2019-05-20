""" type: SofaContent """


from splib.objectmodel import SofaPrefab

@SofaPrefab
class SimplePrefab:
    def __init__(self, node):
        """ This is a documented prefab. 
        It creates a simple node called SimplePrefab,
        and creates a MechanicalObject in it
        """

        self.node = node.createChild("SimplePrefab")
        self.node.createObject('MechanicalObject', name="aSimpleMO")
