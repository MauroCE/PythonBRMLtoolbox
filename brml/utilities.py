import numpy as np


def isvector(numpyarray):
    """
    Returns True if the numpyarray has shape:
        1. (n,)
        2. (1, n)
        3. (n, 1)
        4. (1, 1, ...., 1, n) in any order
    Returns False otherwise. Similar to isvector in MATLAB, but this takes care
    of the 1D case, which cannot happen in MATLAB.

    :Examples:

    >>> isvector(np.array([1, 2]))  # (2,)
    True
    >>> isvector(np.array([1,2]).reshape(1, 2))  # (1, 2)
    True
    >>> isvector(np.array([1, 2]).reshape(2, 1))  # (2, 1)
    True
    >>> isvector(np.array([1, 2]).reshape(1,1,2,1,1))  # (1,1,2,1,1)
    True
    >>> isvector(np.array([[1,2], [5, 6]]))  # (2,2)
    False
    >>> isvector(np.array([[1,2], [5, 6]]).reshape(1,1,1,2,1,2,1,))
    False

    :param numpyarray: Numpy array that we want to check is a vector.
    :type numpyarray: numpy.array
    :return: Whether the input numpy array is a vector or not.
    :rtype: bool
    """
    # Convert in case they passed in a list
    numpyarray = np.array(numpyarray)
    # Find number of dimensions
    ndim = numpyarray.ndim
    if ndim > 2:
        # np.array([[[1, 2, 3]]]) is a vector with shape (1,1,3)
        shape = np.array(numpyarray.shape)
        # Find number of dimensions that have length 1
        ones = (shape == 1).sum()
        # If all but 1 dimensions have length 1, it is a vector
        if ones == ndim - 1:
            return True
        else:
            return False
    elif ndim == 1:
        return True
    else:
        # ndim = 2
        if 1 in numpyarray.shape:
            # (1, n) or (n, 1)
            return True
        else:
            return False


def isnumeric(numpyarray):
    """
    This function returns True if the values of a numpy array are numeric
    otherwise it returns False. To see why this works, go to:
    https://stackoverflow.com/a/29519728/6435921

    :param numpyarray: Numpy array that we want to know if it is numeric
    :type numpyarray: numpy.array
    :return: Whether numpy array contains numeric values
    :rtype: bool
    """
    numpyarray = np.array(numpyarray)  # Could be a list
    if np.issubdtype(numpyarray.dtype, np.number):
        return True
    else:
        return False
