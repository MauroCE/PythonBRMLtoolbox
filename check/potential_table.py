from brml.potential import Potential
import numpy as np


def initialization(variables, table):
    """
    This function is used to check the variables and table of Potential.
    This can be used to check whether a combination of variables and table will
    give raise to an error.

    :param variables:
    :param table:
    :return:
    """
    print("-" * 80)  # for decoration
    try:
        pot = Potential(variables, table)
        print("Variables: ", pot.variables)
        print("Variables shape: ", pot.variables.shape)
        print("Table: \n", pot.table)
        print("Table shape: \n", pot.table.shape)
    except ValueError as e:
        print("DID NOT WORK: ", e)
        print("Input table shape: ", table.shape)
        print("Input variables: ", variables)


if __name__ == "__main__":
    # 1 variable, 2 states (row vector) -> OK
    initialization(variables=1, table=np.array([0.4, 0.6]))
    # 1 variable, 4 states (row vector) -> OK
    initialization(variables=1, table=np.array([0.1, 0.2, 0.4, 0.1]))
    # 1 variable, 2 states (col vector 1x2)
    initialization(variables=1, table=np.array([[0.4, 0.6]]))
    # 1 variable, 2 states (col, vector 2x1)
    initialization(variables=1, table=np.array([[0.4], [0.6]]))

