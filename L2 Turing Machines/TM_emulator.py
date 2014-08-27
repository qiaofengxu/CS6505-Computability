def stateString(test_tape,headidx,currentState):

	return ''.join(test_tape[:headidx]) + 'q_' + str(currentState) + ''.join(test_tape[headidx:])

def nextState(test_tape, headidx, currentState, delta):

	data = delta[(currentState,test_tape[headidx])]

	nextState = data[0]
	writeBeforeMove = data[1]
	direction = data[2]

	test_tape[headidx] = writeBeforeMove
	if headidx is not 0 and direction is 'L':
		headidx -= 1

	if direction is 'R':
		headidx += 1
		if headidx is len(test_tape)-1 and test_tape[-1] is not 'b':
			test_tape.append('b')

	return test_tape, headidx, nextState

def turingMachine(q_0,q_a,q_r,delta,test_tape):

	currentState = q_0
	headidx = 0

	while currentState is not q_a and currentState is not q_r:
		print stateString(test_tape,headidx,currentState)

		test_tape, headidx, currentState = nextState(test_tape, headidx, currentState, delta)

	print stateString(test_tape,headidx,currentState)

	if currentState is q_a:
		print 'ACCEPTED!'
		return 0

	print 'REJECTED!'
	return 1


##############  Append 1 #################

test_tape = ['0','1']

#Specify your turing machine here
q_0 = 1
q_a = 1
q_r = 2

delta = {}

delta[(0,'0')] = (0,'0','R')
delta[(0,'1')] = (0,'1','R')
delta[(0,'b')] = (1,'1','R')

turingMachine(q_0,q_a,q_r,delta,test_tape)


