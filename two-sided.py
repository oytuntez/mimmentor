# the men and their list of ordered spousal preferences
from match import Matcher

MR = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('mentors.txt')))

# the women and their list of ordered spousal preferences
ME = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                for line in open('mentees.txt')))


# initialize Matcher with preference lists for both men and women
match = Matcher(MR, ME)

mentees = match()

print("Mentors:")
print(MR)
print("Mentee:")
print(ME)
print("Result:")
print(mentees)
