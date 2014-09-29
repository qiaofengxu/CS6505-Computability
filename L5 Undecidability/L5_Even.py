#Even.py
#Consider the language E over the binary alphabet
#consisting of strings representing even non-negative
#integers (with leading zeros allowed).  
#I.e. E = {x | x[-1] == '0'}.
#
#Reduce E to the language {'Even'} by implementing
#the function R
def R(x):
	#Your code here


def main():
	#A few test cases
	assert(R('10010') in ['Even'])
	assert(R('110011') not in ['Even'])

if __name__ == '__main__':
	main()