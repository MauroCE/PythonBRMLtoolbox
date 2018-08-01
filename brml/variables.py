class Variable:

    def __init__(self, name: str, index: int, domain: tuple):
        """
        Constructor for Variable class.

        :param name: Name of the variable.
        :type name: str
        :param index: Index of the variable
        :type index: int
        :param domain: States that Variable can be in
        :type domain: tuple
        """
        # Prefix to avoid collision with states create by _set_state_indexes()
        self.var_name = name
        self.var_ix = index
        self.var_domain = domain
        # Set each state as attribute
        self._set_state_indexes()

    def __repr__(self):
        """
        String to re-instantiate class.
        :return: String that can be used to re-create instance of the class.
        :rtype: str
        """
        s = "Variable({}, {}, {})".format(self.var_name,
                                          self.var_ix, self.var_domain)
        return s

    def _set_state_indexes(self):
        """
        This method creates attributes for each state. Each attribute is set to
        its index in the domain tuple (which is ordered!)
        :return: Nothing to return
        :rtype: None
        """
        # TODO: Take care of when state name equal to one of name, ix, domain.
        for state in self.var_domain:
            setattr(self, state, self.var_domain.index(state))


def order_variables(variable_list):
    """
    This function can be used to order Variable instances stored in some
    iterable, by index. When Variables will be implemented as a stand-alone
    class, this could just become a method.

    :param variable_list: Iterable containing Variable instances
    :type variable_list: list
    :return: Ordered list, based on Variable index
    :rtype: list
    """
    return sorted(variable_list, key=lambda x: x.var_ix)


def ix(variable: 'Variable', state: str) -> int:
    """
    This function takes a Variable instance and the name of a state in the
    domain of that variable and returns the index of that state.
    This should be implemented as a getter method in Variable class in the
    future.

    :param variable: Variable with a name, index and domain
    :type variable: Variable
    :param state: Name of the state for which we want the index
    :type state: str
    :return: Index of the state wrt the domain
    :rtype: int
    """
    return variable.domain.index(state)

