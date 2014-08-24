######################################################################
# Task: Describe a two-tape Turing machine that recognizes the 
# language {x#y | x is a substring of y and x,y in {0,1}^* }
######################################################################
# Enter values below for
# q_0 : the initial state (an int)
# q_a : the accept state (an int)
# q_r : the reject state (an int)
# delta : the transition function expressed as a dictionary
#         with keys (state, symbol, symbol) and 
#		  values (state, symbol, symbol,{L,S,R},{L,S,R})
# Use the 'b' character for the blank symbol.
#
# For example, you might express the TM that turns input x into
# x#x as follows:
#
# q_0 = 0
# q_a = 4
# q_r = 5
#
# delta = {}
# #Leave a blank at the beginning of the second tape.
# delta[(0,'0','b')] = (1,'0','b','S','R')
# delta[(0,'1','b')] = (1,'1','b','S','R')
# delta[(0,'b','b')] = (4,'#','b','R','R')

# #Copy the 1st onto the 2nd tape
# delta[(1,'0','b')] = (1,'0','0','R','R')
# delta[(1,'1','b')] = (1,'1','1','R','R')
# delta[(1,'b','b')] = (2,'#','b','S','L')

# #Rewind the 2nd tape
# delta[(2,'#','0')] = (2,'#','0','S','L')
# delta[(2,'#','1')] = (2,'#','1','S','L')
# delta[(2,'#','b')] = (3,'#','b','R','R')

# #Copy from 2nd to 1st
# delta[(3,'b','0')] = (3,'0','0','R','R')
# delta[(3,'b','1')] = (3,'1','1','R','R')
# delta[(3,'b','b')] = (4,'b','b','S','S')
######################################################################

test_tape = ['0','1','#','1','0','1','0']

#Specify the Multitape machine here
q_0 = 
q_a = 
q_r = 

delta = {}