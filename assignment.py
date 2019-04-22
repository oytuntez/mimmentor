# the men and their list of ordered spousal preferences
from match import Matcher

M = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('men.txt')))

# the women and their list of ordered spousal preferences
W = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('women.txt')))


# initialize Matcher with preference lists for both men and women
match = Matcher(M, W)

wives = match()

print(wives)
