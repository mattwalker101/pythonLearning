# exercise: 15
# Learn Python the Hard Way
# Matthew Walker
# Nov 16 2015

# READING FILES

# import the argv module from the sys library
from sys import argv

#assign variables to the command line arguments
script, filename = argv

txt = open(filename)	# open file specified in argument

print "Here is your file %r:" % filename # prints name of the file
print txt.read()		# print contents of file using .read()

print "Type the filename again:"
file_again = raw_input("> ")	# prompts user for name of file to read

txt_again = open(file_again)	# opens the file specified

print txt_again.read()			# prints the file contents

txt.close()
txt_again.close()				# these close the files we opened
