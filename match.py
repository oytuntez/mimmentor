from collections import defaultdict


class Matcher:

    def __init__(self, mentors, mentees):
        '''
        Constructs a Matcher instance.

        Takes a dict of mentors' spousal preferences, `mentors`,
        and a dict of mentees' spousal preferences, `mentees`.

        '''
        self.M = mentors
        self.W = mentees
        self.mentees = {}
        self.pairs = []

        # we index spousal preferences at initialization
        # to avoid expensive lookups when matching
        self.mrank = defaultdict(dict)  # `mrank[m][w]` is m's ranking of w
        self.wrank = defaultdict(dict)  # `wrank[w][m]` is w's ranking of m

        # place rank values
        for m, prefs in mentors.items():
            for i, w in enumerate(prefs):
                self.mrank[m][w] = i

        for w, prefs in mentees.items():
            for i, m in enumerate(prefs):
                self.wrank[w][m] = i

    def __call__(self):
        return self.match()

    def prefers(self, w, m, c):
        '''Test whether w prefers m over h.'''
        mentee_pref = self.wrank[w]

        if m not in mentee_pref:
            return False

        if c not in mentee_pref:
            return False

        return mentee_pref[m] < mentee_pref[c]

    def after(self, m, w):
        # print("after:", w)
        '''Return the mentee favored by m after w.'''
        i = self.mrank[m][w] + 1  # index of mentee following w in list of prefs

        # print(i)
        #
        # print(self.M[m][w])
        #
        if i >= len(self.M[m]):
            # print("not found ", i)
            return None

        return self.M[m][i]

    def match(self, mentors=None, next=None, mentees=None):
        '''
        Try to match all mentors with their next preferred spouse.

        '''
        if mentors is None:
            mentors = self.M.keys()  # get the complete list of men
        if next is None:
            # if not defined, map each mentor to their first preference
            next = dict((m, rank[0]) for m, rank in self.M.items())
        if mentees is None:
            mentees = {}  # mapping from mentees to current spouse
        if not len(mentors):
            self.pairs = [(h, w) for w, h in mentees.items()]
            self.mentees = mentees
            return mentees
        m, mentors = list(mentors)[0], list(mentors)[1:]
        # print("current mentor: ", m)
        w = next[m]  # next mentee for m to propose to
        # print("current mentee: ", w)
        if w is not None:
            next[m] = self.after(m, w)  # mentee after w in m's list of prefs
            # if next[m] is not None:
            #     print("next mentee for " + m + " to propose: " + next[m])

            if w in mentees:
                c = mentees[w]  # current mentor
                if self.prefers(w, m, c):
                    mentors.append(c)  # current mentor becomes available again
                    mentees[w] = m  # w becomes mentee of m
                # todo there may be other conditions here, such as "if this is man's only choice"
                else:
                    mentors.append(m)  # m remains unmatched
            else:
                mentees[w] = m  # w becomes mentee of m
        else:
            print("w is none.", m, mentors)

        return self.match(mentors, next, mentees)

    def is_stable(self, wives=None, verbose=False):
        if wives is None:
            wives = self.mentees
        for w, m in wives.items():
            i = self.M[m].index(w)
            preferred = self.M[m][:i]
            for p in preferred:
                h = wives[p]
                if self.W[p].index(m) < self.W[p].index(h):
                    msg = "{}'s matching to {} is unstable: " + \
                          "{} prefers {} over {} and {} prefers " + \
                          "{} over her current mentor {}"
                    if verbose:
                        print
                        msg.format(m, w, m, p, w, p, m, h)
                    return False
        return True
