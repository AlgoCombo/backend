class baseAlgorithm(object):
    def __init__(self, inputs,  *args, **kwargs):
        self.name = "Base Algorithm"
        self.description = "Base algorithm class to extend for all algorithms"
        self.inputs = inputs

    def run(self, *args, **kwargs):
        raise NotImplementedError

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
