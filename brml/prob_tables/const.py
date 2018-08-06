from brml.prob_tables.potential import Potential
import numpy as np


class Const(Potential):

    def __init__(self, value=np.array([]), variables=np.array([])):
        """
        Initializes Constant Potential table. The difference between a Const
        potential and an array is that Const does not need variables. It
        just contains a value (instead of a table).

        Notice that variables should never be set to anything different from []
        However, even if someone did set it to something different from [],
        _check_variables method would still set self.variables to [].
        :param value: for constant table
        :type value: float
        """
        # Constant probability table has no variables
        super().__init__(variables, value)

    def to_logconst(self):
        """
        Converts Const to a Const where the value stored in self.table is
        the logarithm of the initial value
        :return:
        """
        return Const(np.log(self.table))

    def _check_table(self, value):
        """
        This method gets overwritten because now we want value to be one of:
            1. Float
            2. Int
            3. List with length 1
            4. Array with size 1

        :param value: Value to be constant probability table
        :return:
        """
        # If numeric -> return np.array with that number
        if isinstance(value, (float, int)):
            return np.array([value])
        # If list or numpy array, check size
        elif isinstance(value, (np.ndarray, list)):
            # If only 1 element -> return flatten array
            if np.array([value]).size <= 1:
                return np.array([value]).flatten()
            # Otherwise provided more than one value
            else:
                raise ValueError(
                    "Constant potential cannot have more than one value."
                )
        else:
            raise NotImplementedError(
                "Table value can only be float, int, list or np.array."
            )

    @staticmethod
    def _check_variables(variables):
        """
        Overwrite this method so that even if they try to change variables,
        it will not be possible. This could happen in certain methods such as
        in sum()
        :return:
        """
        return np.array([])

    def evalpot(self, evvariables=0, evidence=0):
        """
        Evaluates the table of a potential. Because this is a constant
        potential, we just return the constant scalar value. Similar to
        @const/evalpot.m

        At the moment I am keeping evvariables and evidence parameters even if
        they are not used. I think this is necessary because during
        calculations with potentials, we can end up having a const or an array
        but this would simply be based on the numerical values. Therefore,
        implementing evalpot in the same way for Const and Array, then we
        don't have any problem.

        :return:
        """
        return self.table


if __name__ == "__main__":
    pot = Const(0.7)
    print("Const potential:", pot)
    print("Table: ", pot.table)
    print("Variables: ", pot.variables)
    print("Size: ", pot.size())
