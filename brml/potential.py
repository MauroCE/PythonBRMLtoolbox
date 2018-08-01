import numpy as np


class Potential:
    """
    Class representing MATLAB potential class.
    """
    def __init__(self, variables=np.array([]), table=np.array([])):
        """
        The way I understand this class, is that a Potential instance is a
        probability table where we have the probabilities for each n-tuple of
        variables, where n is the number of variables that we are considering.
        For this reason, variables should ideally be an iterator, something
        like a list, a numpy.array, a tuple, a namedtuple or something similar.
        Table, should probably be a numpy.array. The array would have as many
        dimensions as variables. Each dimensions represents a variable, and the
        size of that dimension corresponds to the number of states of that
        variable. Below there is an example, where I couldn't bother making the
        probabilities work out.

        :Example:

        variables = [2, 0, 1]
        table = np.array([[0.1, 0.4], [0.3, 0.1]], [[0.8, 0.01], [0.4, 0.3]])

        In the example above, we have 3 variables. We know this because the
        length of the list "variables" is 3. We know that we consider these
        variables in the order [2, 0, 1]. Then, we have a table which is a np
        array and contains the probabilities. You can check that this is a 2x2
        array. Basically the first dimension will indicate variable 0 which is
        in position 1 in "variables". Similarly, the second dimension will
        indicate variable 1 which is in position [2] in "variables", and so on.

        :param variables: Contains integers denoting the order of the variables
        :type variables: iterable
        :param table: Contains probabilities for each tuple of states
        :type table: np.array
        """
        # For now, just pass variables and table in the constructor and assign
        # them as instance attributes
        self.variables = self._check_vars(variables)
        self.table = table

    def __repr__(self) -> str:
        """
        Creates a string that can be used to re-instantiate.
        :return: String that can be fed into eval() function to re-create the
                 instance of the class.
        :rtype: str
        """
        return "Potential({}, {})".format(self.variables, self.table)

    @staticmethod
    def _check_vars(variables):
        """
        This method can be used at initialization, in the __init__ constructor.
        Its purpose is to check that the variables argument in __init__ is
        of the correct type. Ideally, I would like the argument to be an
        iterable. This class will check that, but will also allow numeric
        values, which will be converted to iterable. For now, I will just check
        the data type, however to check whether it is iterable or not, go to
        https://stackoverflow.com/a/1952655/6435921

        :param variables:
        :return: variables with correct data type
        :rtype: np.array
        """
        # Allow: list, np.array
        if isinstance(variables, (np.ndarray, list)):
            # Must be a numerical iterable / vector
            variables = np.array(variables)
            if np.issubdtype(variables.dtype, np.number):
                # Handle np.array with dim (n, 1) or other dimensions
                return variables.astype(np.int8).flatten()
            else:
                raise TypeError(
                    "Variables must be a numerical vector."
                )
        # Convert int, float
        elif isinstance(variables, (int, float)):
            return np.array([variables], dtype=np.int8)
        else:
            raise TypeError(
                "Variables parameter must be a list, np.array, int or float."
            )


if __name__ == "__main__":
    p = Potential()
