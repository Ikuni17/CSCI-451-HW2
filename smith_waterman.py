'''
Carsen Ball, Bradley White
Homework #2: Smith-Waterman Algorithm
CSCI 451/551
September 21, 2017
'''

# Global variables
global_max = [0, (0,0)]
score_array = [[]]

# Calculate the max score for a given index
def calc_v(i,j):
    pass

# Returns the correct alignment
def create_alignment():
    pass

def main():
    global global_max
    global score_array

    s = "acaatcg"
    t = "ctcatgc"

    s_list = list(s)
    t_list = list(t)

    score_array = [[0] * len(t_list)] * len(s_list)

    print(score_array)


main()