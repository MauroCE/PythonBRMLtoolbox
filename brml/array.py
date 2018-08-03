import numpy as np
from brml.utilities import isvector
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

    def size(self):
        """
        Finds the number of states of the Array potential.
        At the moment this method calculates the number of states as follows:
            1. Table 1D (vector) -> length of vector
            2. Table 2D but one dimension has length 1 (e.g. (1, 2)) -> max
               of both dimensions (e.g. max(1, 2) = 2)
            3. Table multidimensional but actually a vector - length vector
            4. Table multidimensional -> return shape of table
        TODO: Consider moving this method to Potential superclass.
        TODO: Consider adding a __len__ method.
        Notice that it returns a numpy array even if table is a 1D vector.
        :return: Number of states in the table for each variable.
        :rtype: numpy.array
        """
        if isvector(self.table):
            return np.array([len(self.table)]).astype(np.int8)
        else:
            return np.array(self.table.shape).astype(np.int8)

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
    b = Array([1, 2], np.array([[0.4, 0.6], [0.3, 0.7]]))
    print("a: ", a)
    print("b: ", b)
    print("Number of states of a: ", a.size())
    print("Number of states of b: ", b.size())
