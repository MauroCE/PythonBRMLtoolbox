import numpy as np
from brml.potential import Potential


class Array(Potential):

    def __init__(self, variables=np.array([]), table=np.array([])):
        """
        Instantiates Array class.

        :param variables:
        :param table:
        """
        # Instantiate Potential class.
        super().__init__(variables, table)

    def to_logarray(self):
        """
        This function converts Array to a LogArray. At the moment the LogArray
        class is not implemented.
        :return:
        """
        # TODO: See if LogArray class is needed or this is enough.
        return Array(variables=self.variables, table=np.log(self.table))

    def sumpot(self, axis):
        """
        This method does marginalization. It sums over a variable.
        TODO: See if this has to be moved to Potential class instead.
        :param axis:
        :return:
        """
        pass


if __name__ == "__main__":
    a = Array([1], np.array([0.1, 0.2]))
    print(a)
