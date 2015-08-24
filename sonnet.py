import sys
from sys import argv
from datetime import timedelta
from string import maketrans

script, you, love = argv

year = timedelta(days=365)
seconds = year.total_seconds()

def the_time():
	for i in range(int(seconds)):
	    if i <= 15768000:
	        print "new-found methods"
	    else:
	        print "compounds strange"

def ever_the_same():
    return "all one"

def every_word():
	return "you"

w0 = "sp"
w1 = "b-"
new_words = maketrans(w0, w1)

verse = "spending again" # bending again
print verse.translate(new_words)

print "and %s and %s are still my argument;" % (you, love)

noted_weed = "i %s n %s v %s e %s n %s t %s i %s o %s n"
noted_weed % ("-", "-", "-", "-", "-", "-", "-", "-")

my_verse = """

    .....

                .new.



          ..........


   ..


                ...

        .pride.
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .
        .variation or quick change.

"""

print sys.path
