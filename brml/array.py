import copy
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

    def sum(self, variables):
        """
        This method sums the probability table over provided variables. It is
        the marginalization operation.
        The function brml.setminus is replicated by np.setdiff1d()
        https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.setdiff1d.html
        The function brml.ismember is replicated by np.isin()
        https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.isin.html
        :param variables:
        :return:
        """
        # New Array will have variables in self that are not in variables
        # because those will be summed over
        newpot = Array(variables=np.setdiff1d(self.variables, variables))
        # Find the indexes of the variables that we will sum over. These are
        # all those in self that are in variables
        to_sumover = np.isin(self.variables, variables).nonzero()[0]
        # FIXME: Notice that nonzero() returns a tuple. Each array in the tuple
        # FIXME: contains indexes of non-zero elements for that dimension. That
        # FIXME: is there is an array for each dimension. But since variables
        # FIXME: are going to be flat, should be first element.
        # Find the table
        t = copy.deepcopy(self.table)
        for variable_index in to_sumover:
            t = t.sum(axis=variable_index)
        # Add table to Array
        # TODO: When we sum over all variables, Array will be initialized with
        # TODO: no variables, thus we need to create Const potential class,
        # TODO: having no variables, but just a table with one element.
        newpot.set_table(table=t)
        return newpot

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
