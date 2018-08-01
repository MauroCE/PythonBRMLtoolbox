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
        self.name = name
        self.index = index
        self.domain = domain

    def __repr__(self):
        """
        String to re-instantiate class.
        :return: String that can be used to re-create instance of the class.
        :rtype: str
        """
        s = "Variable({}, {}, {})".format(self.name, self.index, self.domain)
        return s

    def ix(self, state: str) -> int:
        """
        This function takes a Variable instance and the name of a state in the
        domain of that variable and returns the index of that state.
        This should be implemented as a getter method in Variable class in the
        future.

        Notice that one could use both:
        butler.ix('murderer') and butler.murderer

        :param state: Name of the state for which we want the index
        :type state: str
        :return: Index of the state wrt the domain
        :rtype: int
        """
        return self.domain.index(state)

    @staticmethod
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
        return sorted(variable_list, key=lambda x: x.index)
