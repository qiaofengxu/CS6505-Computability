#Your task is to reduce the language {'Jane'}.
#to the halting problem {<M> | M halts on the empty string}.
#
#Since we can't very well test whether your output function
#actually loops, we ask you to raise the exception Looping
#defined below with
#
# raise Looping()
#
#We use the convention that a machine accepting corresponds
#to a procedure returning true and a machine rejecting
#corresponds to a procedure returning false.
#
#For those less familiar with python, one can define functions
#nested functions and then return these functions as objects.
#For example, 
def foo(w):
	def returns_ww():
		return w+w
	return returns_ww

bar = foo('foobar')
assert(bar() == 'foobarfoobar')

#Here is the Looping exception
class Looping(Exception):
	pass

def R(x):
	#Your code here


def main():
	#A few test cases
	N = R('Jane')

	assert(N('') == True)

	try:
		N = R('not Jane')
		N('')
		#Code should be reached
		assert(False)
	except Looping:
		pass

if __name__ == '__main__':
	main()