import copy
import numpy as np
from brml.prob_tables.potential import Potential
from brml.prob_tables.const import Const


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
        return self.__class__(self.variables, np.log(self.table))

    def sum(self, variables=None):
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
        # Allow for default "None" to sum over all variables
        if variables is None:
            variables = self.variables
        # New Array will have variables in self that are not in variables
        # because those will be summed over
        remaining_vars = np.setdiff1d(self.variables, variables)
        if remaining_vars.size == 0:
            newpot = Const()
        else:
            newpot = Array(variables=remaining_vars)
        # Find the indexes of the variables that we will sum over. These are
        # all those in self that are in variables. Notice that nonzero()
        # returns a tuple. Each array in the tuple contains indexes of non-zero
        # elements for that dimension. That is there is an array for each
        # dimension. But since variables are going to be flat, should be first
        # element.
        to_sumover = np.isin(self.variables, variables).nonzero()[0]
        # Find the table
        t = copy.deepcopy(self.table)
        for variable_index in to_sumover[::-1]:
            # FIXME: Notice that at the moment I am summing over in opposite
            # FIXME: order, this is so indexes don't disappear before they are
            # FIXME: Used
            t = t.sum(axis=variable_index)
        # Add table to Array
        newpot.set_table(table=t)
        return newpot

    def sumpot(self, variables=None, sumover=True):
        """
        This method does marginalization. It sums over a variable.
        TODO: See if this has to be moved to Potential class instead.
        :param variables: Variables to consider.
        :type variables: list or numpy.array
        :param sumover: Whether variables specified with "variables" argument
                        are to be summed over, or if they are the ones to keep
                        at the end.
        :type sumover: bool
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
    # Sum
    pot = Array([1, 2], np.array([[0.4, 0.6], [0.3, 0.7]]))
    print("Potential Array: \n", pot)
    print("Marginalize var 1: \n", pot.sum(1))
    print("Marginalize var 2: \n", pot.sum(2))
    print("Marginalize var [1,2]: \n", pot.sum([1, 2]))
