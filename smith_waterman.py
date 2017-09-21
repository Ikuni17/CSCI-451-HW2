'''
Carsen Ball, Bradley White
Homework #2: Smith-Waterman Algorithm
CSCI 451/551
September 21, 2017
'''

# Global variables
#Directions: 1 is left, 2 diagonal, 3 is up
global_max = [0, (0,0)]
score_array = [[]]

# Calculate the max score for a given index
def calc_v(i,j):
    pass

# Returns the correct alignment
def create_alignment(s, t):
    #Stacks to hold the characters for the alignment
    s_prime = []
    t_prime = []
    score = global_max [0]
    location = global_max[1]
    while(score != 0):
        direction = score_array[location[0]][location[1]][1]
        if direction == 2:
            s_prime.append(s[location[0]])
            t_prime.append(t[location[1]])
            location[0] = location[0] - 1
            location[1] = location[1] - 1
        elif direction == 1:
            s_prime.append("_")
            t_prime.append(t[location[1]])
            location[1] = location[1] - 1
        else:
            t_prime.append("_")
            s_prime.append(s[location[0]])
            location[0] = location[0] - 1
        score = score_array[location[0]][location[1]][0]


def main():
    global global_max
    global score_array

    s = "acaatcg"
    t = "ctcatgc"

    s_list = list(s)
    t_list = list(t)

    score_array = [[0] * len(t_list)] * len(s_list)
    create_alignment(s_list, t_list)
    print(score_array)


main()