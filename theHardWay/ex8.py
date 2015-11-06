# exercise: 8
# Learn Python the Hard Way
# Matthew Walker
# Nov 3 2015

formatter = "%r %r %r %r"  # create a variable that is a string of formatting characters

#see the versatility of the %r formatting character
print formatter % (1, 2, 3, 4) # print the numbers 1-4
print formatter % ("one", "two", "three", "four") # print those numbers
print formatter % (True, False, False, True) # print those values 
print formatter % (formatter, formatter, formatter, formatter) # print as a string 4x
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)	# this will print each string encased in '' with a space between each


