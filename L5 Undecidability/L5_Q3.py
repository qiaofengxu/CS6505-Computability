######################################################################
#Provide a reduction from HALT = {<M> | M halts on the empty string} 
#to ZO = {<M> | M accepts strings of the form 0^n1^n for n >= 0 and
#no others}.
#
#You must define a function R that takes a function M as a parameter 
#and returns another function N.  The function R should must always 
#halt.
#
#In general, it is only necessary that <N> be in ZO if M halts and not in
#ZO if M does not halt (or vice-versa). 
#
#For this exercise, it must also be the case that <N> is in ZO if M halts 
#and not in ZO otherwise.  Also, N must always halt if M does.
#
#For example, consider what the reduction from HALT to 
#{<M> | M accepts only ''} might look like
#
#def R(M):
#	def N(x):
#		M('')
#		return x ==''
#	return N
#
# assert( OnlyEmptyString( R(accepts) ))
# assert( OnlyEmptyString( R(rejects) ))
# assert( not OnlyEmptyString ( R(loops) ))
######################################################################
def R(M):
	#Your code here
	
