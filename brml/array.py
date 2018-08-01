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
        # Check number of variables is correct
        self._check_number_of_variables()

    def _check_number_of_variables(self):
        """
        This function checks whether the provided number of variables (in the
        variables parameter) is the same as the expected number of variables
        that we infer from the table parameter. For instance, if we provide 2
        variables, then the table should have 2 dimensions (one per variable!)
        :return:
        """
        # Find number of variables in variables attribute
        n_vars = len(self.variables)
        # Now calculate number of variables in the table
        n_vars_table = len(self.table.shape)
        if n_vars != n_vars_table:
            raise ValueError(
                "Number of declared variables is not equal to the number of "
                "variables in the table. \nDeclared: {} variables"
                "\nTable shape: {}".format(n_vars, n_vars_table)
            )

    def to_logarray(self):
        """
        This function converts Array to a LogArray. At the moment the LogArray
        class is not implemented.
        :return:
        """
        pass


if __name__ == "__main__":
    a = Array([1], np.array([0.1, 0.2]))
