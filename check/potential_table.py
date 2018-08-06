from brml.prob_tables.potential import Potential
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
    print("="*80)
    print("1 SCALAR VARIABLE, TABLE 2 STATES")
    print("="*80)
    # variable: 1, table (2,) 2 states -> OK
    initialization(variables=1, table=np.array([0.4, 0.6]))
    # variable: 1, table (1,2) 2 states -> OK
    initialization(variables=1, table=np.array([[0.4, 0.6]]))
    # variable: 1, table (2,1) 2 states -> OK
    initialization(variables=1, table=np.array([[0.4], [0.6]]))

    print("="*80)
    print("[1] LIST VARIABLE, TABLE 2 STATES")
    print("="*80)
    # variable: [1], table (2,) 2 states
    initialization(variables=[1], table=np.array([0.4, 0.6]))
    # variable: [1], table (1,2) 2 states
    initialization(variables=[1], table=np.array([[0.4, 0.6]]))
    # variable: [1], table (2,1) 2 states
    initialization(variables=[1], table=np.array([[0.4], [0.6]]))

    print("="*80)
    print("MULTIPLE VARIABLES, TABLE 2 STATES")
    print("="*80)
    # variables [1, 2], table (4,) -> NOT OK (wrong shape)
    initialization(variables=[1, 2], table=np.array([0.4, 0.6, 0.7, 0.3]))
    # variables [1, 2], table (2, 2) -> OK
    initialization(variables=[1, 2], table=np.array([[0.4, 0.6], [0.7, 0.3]]))
    # variables [1, 2], table (1,4) -> OK
    initialization(variables=[1, 2], table=np.array([[0.4, 0.6, 0.7, 0.3]]))
