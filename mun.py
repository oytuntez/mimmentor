from random import randint, shuffle

from munkres import Munkres, print_matrix

# mentors: [a,b,c,d]
# mentees: [z,q,w,y]
# votes: [mentorId,mentorId,mentorId,mentorId,mentorId] <<< per mentee

nMentee = i = 20
nMentor = nMentee
maxSelectedMentors = 3
matrix = []

while i > -1:
    i -= 1

    entry = [1, 2, 3]

    if nMentor > maxSelectedMentors:
        rand = [5] * (nMentor - maxSelectedMentors)
        entry.extend(rand)

    shuffle(entry)

    print(f'Current mentee entry: {entry}')
    matrix.append(entry)

# matrix = [[1,4,5,2,5, 5, 1, 2], # this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           #1,4,5,2, this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           #1,4,5,2, this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
# [5, 5, 1, 21,4,5,2,], # this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           #1,4,5,2, this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           #1,4,5,2, this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
# [5, 5, 1, 21,4,5,2,], # this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           #1,4,5,2, this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2],
#           #1,4,5,2, this means mentee#1 selected c and d. fill the rest of the set with 5 for other possible mentors. this makes our matrix nx4
#           [1,4,5,2,5, 5, 1, 2],
#           [1,4,5,2,5, 5, 1, 2]
#           ]

print(matrix)


def calc(input_matrix):
    m = Munkres()
    indexes = m.compute(input_matrix)
    print_matrix(input_matrix, msg='Lowest cost through this matrix:')
    total = 0
    print_matrix(indexes, msg='indexes:')
    for row, column in indexes:
        value = input_matrix[row][column]
        total += value
        print(f'({row}, {column}) -> {value}')
    print(f'total cost: {total}')

    return indexes


def diff(in1, in2):
    # found = in1[in2[:, 1], :]
    diff = remove_keys(in1, in2[:, 1])
    print("found for:")
    print(matrix)
    # print(found)


def remove_keys(d, keys):
    to_remove = set(keys)
    filtered_keys = d.keys() - to_remove
    filtered_values = map(d.get, filtered_keys)
    return dict(zip(filtered_keys, filtered_values))


k = 1
while k > 0:
    current_matrix = matrix[k, :]
    result = calc(matrix)

diff(matrix, result)
