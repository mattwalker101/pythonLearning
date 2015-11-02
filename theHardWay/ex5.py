my_name = 'Zed A. Shaw'
my_age = 88
my_height = 77
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually he's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
print "What are these: %r, %r, %r, %r." % (my_age, my_weight, my_eyes, my_hair)
# %r prints anything, whatever it is
# to round a floating point, round(), like round(1.733)
