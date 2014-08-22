######################################################################
# Describe a Turing Machine that decides the language
# {w | w has an equal number of 0s and 1}
######################################################################
# Enter values below for
# q_0 : the initial state (an int)
# q_a : the accept state (an int)
# q_r : the reject state (an int)
# delta : the transition function expressed as a dictionary
#         with keys (state, symbol) and values (state, symbol, 'L' or 'R')
# Use the 'b' character for the blank symbol.
#
# For example, you might express the TM that appends a 1 as follows:
#
# q_0 = 0
# q_a = 1
# q_r = 2
# delta = {}
# delta[(0,'0')] = (0,'0','R')
# delta[(0,'1')] = (0,'1','R')
# delta[(0,'b')] = (1,'1','R')
######################################################################

test_tape = ['0','0','1', '0', '1', '1']

#Specify your turing machine here
q_0 = 0
q_a = 1
q_r = 6

delta = {}
delta[(0,'b')] = (1,'b','L')

delta[(0,'0')] = (2,'b','R')
delta[(0,'1')] = (3,'b','R')
delta[(0,'x')] = (0,'x','R')

delta[(2,'0')] = (2,'0','R')
delta[(2,'x')] = (2,'x','R')
delta[(2,'1')] = (4,'x','L')
delta[(2,'b')] = (6,'b','R')

delta[(3,'0')] = (4,'x','L')
delta[(3,'1')] = (3,'1','R')
delta[(3,'x')] = (3,'x','R')
delta[(3,'b')] = (6,'b','R')

delta[(4,'0')] = (4,'0','L')
delta[(4,'1')] = (4,'1','L')
delta[(4,'x')] = (4,'x','L')
delta[(4,'b')] = (0,'x','R')





