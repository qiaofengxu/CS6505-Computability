#!/usr/bin/env python
from turing import TuringMachine

# Reverse a string in place

test_tape = "10110011110000"

#Specify your turing machine here
q_0 = 0
q_a = 1
q_r = 2

delta = {}
delta[(0,'b','b')] = (1,'b','b','S','S')
delta[(0,'0','b')] = (3,'0','$','S','R')
delta[(0,'1','b')] = (3,'1','$','S','R')

delta[(3,'b','b')] = (4,'b','b','S','L')
delta[(3,'0','b')] = (3,'0','0','R','R')
delta[(3,'1','b')] = (3,'1','1','R','R')

delta[(4,'b','$')] = (5,'b','$','L','R')
delta[(4,'b','0')] = (4,'b','0','S','L')
delta[(4,'b','1')] = (4,'b','1','S','L')

delta[(5,'b','0')] = (6,'0','0','S','R')
delta[(5,'b','1')] = (6,'1','1','S','R')
delta[(5,'0','0')] = (6,'0','0','S','R')
delta[(5,'0','1')] = (6,'1','1','S','R')
delta[(5,'1','0')] = (6,'0','0','S','R')
delta[(5,'1','1')] = (6,'1','1','S','R')

delta[(6,'0','b')] = (1,'0','0','S','S')
delta[(6,'1','b')] = (1,'1','0','S','S')
delta[(6,'0','0')] = (5,'0','0','L','S')
delta[(6,'1','0')] = (5,'1','0','L','S')
delta[(6,'0','1')] = (5,'0','1','L','S')
delta[(6,'1','1')] = (5,'1','1','L','S')

alphabet = TuringMachine.BINARY
alphabet.add("$")

tm = TuringMachine(num_states=7,
                   transitions=delta,
                   start=q_0,
                   accept=q_a,
                   reject=q_r,
                   alphabet=alphabet)

tm.run(test_tape)