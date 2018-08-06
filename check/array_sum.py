from brml.prob_tables.array import Array
import numpy as np


def check_sum(variables, table, to_sum_over):
    """
    This function is used to check the variables and table of Potential.
    This can be used to check whether a combination of variables and table will
    give raise to an error.

    :param variables:
    :param table:
    :param to_sum_over:
    :return:
    """
    print("-" * 80)  # for decoration
    try:
        pot = Array(variables, table)
        print("Initial variables: ", pot.variables)
        print("Initial table: \n", pot.table)
        print("Summed over variables {}: \n".format(to_sum_over),
              pot.sum(to_sum_over).table)
    except ValueError as e:
        print("DID NOT WORK: ", e)


if __name__ == "__main__":
    # 2 variables, sum over one of them
    check_sum([1, 2], np.array([[0.4, 0.6], [0.3, 0.7]]), [1])
    # 2 variables, sum over both
    check_sum([1, 2], np.array([[0.4, 0.6], [0.3, 0.7]]), [1, 2])