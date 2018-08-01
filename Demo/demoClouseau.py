import numpy as np
from brml.potential import Potential
from brml.variables import Variable, order_variables, ix

# Define variables
butler = Variable(name='butler', index=2, domain=('murderer', 'notmurderer'))
maid = Variable(name='maid', index=1, domain=('murderer', 'notmurderer'))
knife = Variable(name='knife', index=0, domain=('used', 'notused'))

# Sort the variables by index
variables = order_variables([butler, maid, knife])

# p(butler,maid,knife)=p(knife|butler,maid)p(butler)p(maid) therefore we need
# 3 probability tables.
pot = []

# p(butler) potential table (bt stands for butler table)
bt = np.zeros(2)  # Only 2 states
bt[ix(butler, 'murderer')] = 0.6
bt[ix(butler, 'notmurderer')] = 0.4

# p(maid) potential table (mt stands for maid table)
mt = np.zeros(2)
mt[ix(maid, 'murderer')] = 0.2
mt[ix(maid, 'notmurderer')] = 0.8

# p(knife|butler,maid) potential table (kt stands for knife table)
kt = np.zeros((2, 2, 2))  # 2 states per variable, a dim per variable
kt[ix(knife, 'used'), ix(butler, 'notmurderer'), ix(maid, 'notmurderer')] = 0.3
kt[ix(knife, 'used'), ix(butler, 'notmurderer'), ix(maid, 'murderer')] = 0.2
kt[ix(knife, 'used'), ix(butler, 'murderer'), ix(maid, 'notmurderer')] = 0.6
kt[ix(knife, 'used'), ix(butler, 'murderer'), ix(maid, 'murderer')] = 0.1
# Use broadcasting, Ellipsis and normalization to complete the table
kt[ix(knife, 'notused'), ...] = 1 - kt[ix(knife, 'used'), ...]

# Put together all the potential in a list. Need to put them in the correct
# order. Currently it is hard coded.
pot = [
    Potential(variables=knife, table=kt),
    Potential(variables=maid, table=mt),
    Potential(variables=butler, table=bt)
]





