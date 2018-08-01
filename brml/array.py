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
        return Array(variables=self.variables, table=np.log(self.table))


if __name__ == "__main__":
    a = Array([1], np.array([0.1, 0.2]))
    print(a)
