import numpy as np
from brml.prob_tables.potential import Potential


def initialization(variables):
    """
    Shows what variables are converted to, when passed at initialization.
    This function is used to check that the following are all equivalent:
        1. Potential(1)
        2. Potential(1.0)
        3. Potential([1])
        4. Potential(np.array([1]))
        5. Potential(np.array([[1]])

    And that the following are also all equivalent:
        6. Potential([1, 2])
        7. Potential(np.array([1, 2]))
        8. Potential(np.array([[1, 2]])
        9. Potential(np.array([[1], [2]])
    :param variables: Variables that you want to check
    :return: Nothing, just prints variables, type and size
    """
    print("-" * 80)  # Just for decoration
    print("Input variable: ", variables)
    pot = Potential(variables=variables)
    print("Variables: ", pot.variables)
    print("Type: ", type(pot.variables))
    print("Size: ", pot.variables.shape)


def setter(variables):
    """
    Similar to initialization function, but used to check assignment after
    initialization.
    :param variables:
    :return:
    """
    print("-" * 80)  # Just for decoration
    print("Input variable: ", variables)
    pot = Potential()
    pot.set_variables(variables)
    print("Variables: ", pot.variables)
    print("Type: ", type(pot.variables))
    print("Size: ", pot.variables.shape)


if __name__ == "__main__":
    print("=" * 80)
    print("INITIALIZATION SINGLE VARIABLE")
    print("=" * 80)
    initialization(1)
    initialization(1.0)
    initialization([1])
    initialization(np.array([1]))
    initialization(np.array([[1]]))
    print("=" * 80)
    print("INITIALIZATION MULTIPLE VARIABLES")
    print("=" * 80)
    initialization([1, 2])
    initialization(np.array([1, 2]))
    initialization(np.array([[1, 2]]))
    initialization(np.array([[1], [2]]))
    print("=" * 80)
    print("SETTER SINGLE VARIABLE")
    print("=" * 80)
    setter(1)
    setter(1.0)
    setter([1])
    setter(np.array([1]))
    setter(np.array([[1]]))
    print("=" * 80)
    print("SETTER MULTIPLE VARIABLES")
    print("=" * 80)
    setter([1, 2])
    setter(np.array([1, 2]))
    setter(np.array([[1, 2]]))
    setter(np.array([[1], [2]]))