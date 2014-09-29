#Consider the language A = {'John'}.  Reduce
#A to the complement of A by implementing
#the function R.

def R(x):
	#Your code here


def main():
	#A few test cases
	assert(R('John') not in ['John'])
	assert(R('110011') in ['John'])

if __name__ == '__main__':
	main()