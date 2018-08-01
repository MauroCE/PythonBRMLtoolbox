import numpy as np
from brml.potential import Potential
from brml.variables import Variable

# Define variables
butler = Variable(name='butler', index=2, domain=('murderer', 'notmurderer'))
maid = Variable(name='maid', index=1, domain=('murderer', 'notmurderer'))
knife = Variable(name='knife', index=0, domain=('used', 'notused'))

# Define states
murderer = 0
notmurderer = 1
used = 0
notused = 1

# Sort the variables by index
variables = Variable.order_variables([butler, maid, knife])

# p(butler,maid,knife)=p(knife|butler,maid)p(butler)p(maid) therefore we need
# 3 probability tables.
pot = []

# p(butler) potential table (bt stands for butler table)
bt = np.zeros(2)  # Only 2 states
bt[butler.ix('murderer')] = 0.6
bt[butler.ix('notmurderer')] = 0.4

# p(maid) potential table (mt stands for maid table)
mt = np.zeros(2)
mt[maid.ix('murderer')] = 0.2
mt[maid.ix('notmurderer')] = 0.8

# p(knife|butler,maid) potential table (kt stands for knife table)
kt = np.zeros((2, 2, 2))  # 2 states per variable, a dim per variable
kt[knife.ix('used'), butler.ix('notmurderer'), maid.ix('notmurderer')] = 0.3
kt[knife.ix('used'), butler.ix('notmurderer'), maid.ix('murderer')] = 0.2
kt[knife.ix('used'), butler.ix('murderer'), maid.ix('notmurderer')] = 0.6
kt[knife.ix('used'), butler.ix('murderer'), maid.ix('murderer')] = 0.1
# Use broadcasting, Ellipsis and normalization to complete the table
kt[knife.ix('notused'), ...] = 1 - kt[knife.ix('used'), ...]

# Put together all the potential in a list. Need to put them in the correct
# order. Currently it is hard coded.
pot = [
    Potential(variables=knife.index, table=kt),
    Potential(variables=maid.index, table=mt),
    Potential(variables=butler.index, table=bt)
]




