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

    def n_states(self):
        """
        Finds the number of states of the Array potential.
        TODO: Think about which implementation is better: returning (2,2) or 4
        TODO: for a table with shape (2, 2).
        At the moment this method calculates the number of states as follows:
            1. Table 1D (vector) -> length of vector
            2. Table 2D but one dimension has length 1 (e.g. (1, 2)) -> max
               of both dimensions (e.g. max(1, 2) = 2)
            3. Table multidimensional but has 1 or 0 elements -> return 1 or 0
            4. Table multidimensional -> return shape of table
        This might or might not be the intended behaviour. However, I tried to
        replicate the behavior of @array\size as much as possible. Notice that
        self.table.shape.prod() is equivalent to self.table.size.
        TODO: Consider moving this method to Potential superclass.
        TODO: Consider adding a __len__ method.
        TODO: Consider returning a tuple for every case (also 1D)
        :return: Number of states in the table for each variable.
        """
        # Find number of dimensions of the table (= n variables)
        n_dim = len(self.table.shape)
        # 1D vector (1 variable) -> length of vector
        if n_dim == 1:
            return len(self.table)
        # 2D vector with one dimension having length 1 -> max length
        elif n_dim == 2 and sum(np.array(self.table.shape) == 1) == 1:
            return max(self.table.shape)
        # matrix with 1 or 0 elements -> number of elements (1 or 0)
        elif self.table.size <= 1:  # self.table.shape.prod()
            return self.table.size
        # Otherwise just return numpy shape
        else:
            return self.table.shape

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
    print("Number of states of a: ", a.n_states())
    print("Number of states of b: ", b.n_states())
