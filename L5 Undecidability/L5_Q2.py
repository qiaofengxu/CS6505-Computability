######################################################################
#Provide a reduction from LOOP = {<M> | M loops on the empty string} to
# {<M> | M does NOT accept the string '100010'}.
#
#You must define a function R that takes a function M as a parameter 
#and returns another function N.  The function R should must always 
#halt.
#
#In general, it is only necessary that <N> be in L if M loops and not in
#L if M otherwise.  For this exercise, N must also always halt if M does.
#
#For example, consider what the reduction from HALT to 
#{<M> | M accepts only ''} might look like
#
#def R(M):
# def N(x):
#   M('')
#   return x ==''
# return N
#
######################################################################
def R(M):
    #Your code here
