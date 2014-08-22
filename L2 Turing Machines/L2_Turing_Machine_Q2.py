######################################################################
# Task: Describe a Turing machine that shifts the input string one
# space to the right and places the symbol ($) in the first location
# on the tape.
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

test_tape = ['0','1']

#Specify your turing machine here

q_0 = 0
q_a = 5
q_r = 6

delta = {}
delta[(0,'0')] = (0,'0','R')
delta[(0,'1')] = (0,'1','R')
delta[(0,'b')] = (1,'b','L')

delta[(1,'0')] = (2,'b','R')
delta[(1,'1')] = (3,'b','R')

delta[(2,'b')] = (4,'0','L')
delta[(3,'b')] = (4,'1','L')

delta[(4,'b')] = (1,'b','L')

delta[(1,'b')] = (5,'$','L')




