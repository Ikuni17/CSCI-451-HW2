'''
Carsen Ball, Bradley White
Homework #2: Smith-Waterman Algorithm
CSCI 451/551
September 21, 2017
'''

# Global variables
# Directions: 1 is diagonal, 2 is left, 3 is up
global_max = [0, (0, 0)]
score_array = [[[]]]
s_list = []
t_list = []


# Calculate the max score for a given index
def calc_v(i, j):
    global global_max
    global score_array
    global s_list
    global t_list

    local_max = -2
    local_max_dir = None
    have_match = False
    coord_list = [(i - 1, j - 1), (i, j - 1), (i - 1, j)]

    # Determine if we have matching letters
    if s_list[i] == t_list[j]:
        have_match = True
        # print("Have match {0} and {1}".format(s_list[i], t_list[j]))

    for k in range(len(coord_list)):
        if have_match is True and k == 0:
            score = score_array[coord_list[k][0]][coord_list[k][1]][0] + 2
        else:
            score = score_array[coord_list[k][0]][coord_list[k][1]][0] - 1

        if score > local_max:
            local_max = score
            local_max_dir = k + 1

    if local_max < 0:
        local_max = 0
        local_max_dir = None

    score_array[i][j][0] = local_max
    score_array[i][j][1] = local_max_dir

    if local_max >= global_max[0]:
        global_max[0] = local_max
        global_max[1] = (i, j)


# Returns the correct alignment
def create_alignment(s, t):
    #The finalized local alingment
    alignment_s = ''
    alignment_t = ''
    # Stacks to hold the characters for the alignment
    s_prime = []
    t_prime = []
    #Initialized the local score to the max score
    score = global_max[0]
    #The starting position that coresponds to the maximum alingment score
    i = global_max[1][0]
    j = global_max[1][1]
    #Will continue until it reaches a score of 0, indicating that the local allingment has been done
    while (score != 0):
        direction = score_array[i][j][1]
        #Diagnoal direction, copying the char at the current index into the alignment
        if direction == 1:
            s_prime.append(s[i])
            t_prime.append(t[j])
            #Moves the local position "diagonaly"
            i = i - 1
            j = j - 1
        #Direction to the left, add a space into the S string alingment
        #Copy the current char in T, to the t aligments
        elif direction == 2:
            s_prime.append("_")
            t_prime.append(t[j])
            #i'th index does not change, move "left" for the jth index
            j = j - 1
        #Direction is up, add a space into the T alingment
        #Copy the char at the curent index in S into the s aligment
        else:
            t_prime.append("_")
            s_prime.append(s[i])
            #j'th index does not change, move "up" for the ith index
            i = i - 1
        score = score_array[i][j][0]
    #Creates the alignment from the stack
    for x in range(len(s_prime)):
        alignment_s += s_prime.pop()
    for y in range(len(t_prime)):
        alignment_t += t_prime.pop()
    #Prints the alignment
    print("\n" + alignment_s)
    print(alignment_t)


def main():
    global global_max
    global score_array
    global s_list
    global t_list

    s = "acaatcg"
    t = "ctcatgc"

    s_list = list(s)
    t_list = list(t)

    s_list.insert(0, '_')
    t_list.insert(0, '_')

    score_array = [[[0, None] for i in range(len(t_list))] for j in range(len(s_list))]

    for i in range(1, len(score_array)):
        for j in range(1, len(score_array[i])):
            # print("S: {0}, T: {1}".format(s_list[i], t_list[j]))
            calc_v(i, j)

    # print(score_array)

    print_scores()
    create_alignment(s_list, t_list)


def print_scores():
    global score_array

    for i in range(len(score_array)):
        print()
        for j in range(len(score_array[i])):
            print(score_array[i][j][0], end=" ")


main()
