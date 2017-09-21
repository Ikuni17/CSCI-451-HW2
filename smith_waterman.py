'''
Carsen Ball, Bradley White
Homework #2: Smith-Waterman Algorithm
CSCI 451/551
September 21, 2017
'''

# Global variables
# Directions: 1 is diagonal, 2 is left, 3 is up
# @param global_max: the score and index for the current highest scoring sub string
# @param score_array: 3D array which has a score and the direction from which thatscore was calculated in the final list
# @param x_list: the input strings converted to lists so the letters can indexed easier
global_max = [0, (0, 0)]
score_array = [[[]]]
s_list = []
t_list = []


# Calculate the max score for a given index based on its coordinate (i, j)
def calc_v(i, j):
    global global_max
    global score_array
    global s_list
    global t_list

    # @param local_max: the maximum score for the current index
    # @param local_max_dir: the direction which local_max was computed from
    # @param have_match: Boolean determining if the letters at the i and j indices are the same letter
    # @param coord_list: the coordinates for each index which can compute the current index
    local_max = 0
    local_max_dir = None
    have_match = False
    coord_list = [(i - 1, j - 1), (i, j - 1), (i - 1, j)]

    # Determine if we have matching letters
    if s_list[i] == t_list[j]:
        have_match = True

    # Iterate through all coordinates
    for k in range(len(coord_list)):
        # If we have a match score it based on the diagonal coordinate
        if have_match is True and k == 0:
            score = score_array[coord_list[k][0]][coord_list[k][1]][0] + 2
        # Otherwise compute the score based on which coordinate we're using
        else:
            score = score_array[coord_list[k][0]][coord_list[k][1]][0] - 1

        # Check if we have a new local max from this coordinate
        if score > local_max:
            local_max = score
            local_max_dir = k + 1

    # Update the score and direction for this index
    score_array[i][j][0] = local_max
    score_array[i][j][1] = local_max_dir

    # Check if we have a new global max, if so record the score and index
    if local_max >= global_max[0]:
        global_max[0] = local_max
        global_max[1] = (i, j)


# Returns the correct alignment
def create_alignment(s, t):
    # Stacks to hold the characters for the alignment
    alignment_s = ''
    alignment_t = ''
    s_prime = []
    t_prime = []
    score = global_max[0]
    i = global_max[1][0]
    j = global_max[1][1]
    while (score != 0):
        direction = score_array[i][j][1]
        if direction == 1:
            s_prime.append(s[i])
            t_prime.append(t[j])
            i = i - 1
            j = j - 1
        elif direction == 2:
            s_prime.append("_")
            t_prime.append(t[j])
            j = j - 1
        else:
            t_prime.append("_")
            s_prime.append(s[i])
            i = i - 1
        score = score_array[i][j][0]
    for x in range(len(s_prime)):
        alignment_s += s_prime.pop()
    for y in range(len(t_prime)):
        alignment_t += t_prime.pop()
    print("\n" + alignment_s)
    print(alignment_t)


def main():
    global global_max
    global score_array
    global s_list
    global t_list

    # Input strings, examples used in the book
    s = "acaatcg"
    t = "ctcatgc"

    s_list = list(s)
    t_list = list(t)

    # Insert a "blank" before the string
    s_list.insert(0, '_')
    t_list.insert(0, '_')

    # Initial all indices with a score of zero and no direction
    score_array = [[[0, None] for i in range(len(t_list))] for j in range(len(s_list))]

    for i in range(1, len(score_array)):
        for j in range(1, len(score_array[i])):
            calc_v(i, j)

    print_scores()
    create_alignment(s_list, t_list)


# Prints the scores in a matrix for easier viewing
def print_scores():
    global score_array

    for i in range(len(score_array)):
        print()
        for j in range(len(score_array[i])):
            print(score_array[i][j][0], end=" ")


# Start
main()
