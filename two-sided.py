# the men and their list of ordered spousal preferences
from match import Matcher


def do_match():
    print("Mentors:")
    print(MR)
    print("Mentee:")
    print(ME)

    # initialize Matcher with preference lists for both men and women
    match = Matcher(MR, ME)

    return match()


def print_result(d):
    print("{:<8} {:<15}".format('Mentee', 'Mentor'))
    for k, v in d.items():
        print("{:<8} {:<15}".format(k, v))


MR = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                                    for line in open('mentors.txt')))

# the women and their list of ordered spousal preferences
ME = dict((m, prefs.split(', ')) for [m, prefs] in (line.rstrip().split(': ')
                                                    for line in open('mentees.txt')))

previous_mentee_size = None
final_mentee_mentors = dict()
i = 0
while len(ME) > 0:
    i += 1
    previous_mentee_size = len(ME)
    match = Matcher(MR, ME)
    matches = match()

    final_mentee_mentors.update(matches)

    for mentee, mentor in matches.items():
        # This mentee already found a mentor for themselves. Delete from matching.
        ME.pop(mentee, True)

        # Delete this mentee from all mentor selections, so that mentors can fall back to their other
        # selections.
        # todo what to do with mentees that were not selected by any mentor?
        new_MR = MR.copy()
        for mrk, mrv in MR.items():
            if mentee in mrv:
                new_MR.get(mrk).remove(mentee)

            # This mentor doesn't have any further mentee preference. So delete them from the matching.
            if len(new_MR.get(mrk)) < 1:
                new_MR.pop(mrk, True)

        # Mentor list at this point should not have the mentee whom we already assigned.
        MR = new_MR

print("\n\n")
print_result(final_mentee_mentors)
print("\n\n")
print("In " + str(i) + " iterations.")
print("\n\n")
