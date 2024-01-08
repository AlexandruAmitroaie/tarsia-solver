NUMERIC = 'n'
EQUATION = 'e'

POS_1 = 0
POS_2 = 1
POS_3 = 2


# triangles given by the school
# best solution:
# 21 (5073693)-> 0/10/0, 1/9/0, 2/12/1, 3/21/2, 4/11/0, 5/18/2, 6/19/1, 7/15/0, 8/1/1, 9/8/2, 10/0/2, 11/4/2, 12/14/1, 13/13/2, 14/2/0, 15/6/2, 16/3/2, 17/7/2, 18/5/0, 19/22/0, 20/20/0, 

triangles_available_school = [
    [   5,      1/3,    1.5,    NUMERIC,    EQUATION,   NUMERIC], # 0 *
    [   5,      6,      5,      NUMERIC,    EQUATION,   NUMERIC], # 1 *
    [   5,      4.5,    6,      NUMERIC,    EQUATION,   EQUATION], # 2 *
    [   0.5,    4,      8,      NUMERIC,    EQUATION,   NUMERIC], # 3 *      
    [   6,      5,      0.33,   EQUATION,   EQUATION,   NUMERIC], # 4 *
    [   0.4,    6,      3.5,    EQUATION,   NUMERIC,    EQUATION], # 5 *
    [   4/9,    6,      4,      NUMERIC,    NUMERIC,    NUMERIC], # 6 *
    [   9/4,    0.5,    2/5,    NUMERIC,    EQUATION,   NUMERIC], # 7 *
    [   8,      6,      1/3,    EQUATION,   NUMERIC,    NUMERIC], # 8 *
    [   1.5,    6,      4,      NUMERIC,    NUMERIC,    EQUATION], # 9 *
    [   5,      1.5,    3,      NUMERIC,    EQUATION,   EQUATION], # 10 *
    [   5/4,    0.5,    1.5,    NUMERIC,    NUMERIC,    EQUATION], # 11 *
    [   0.75,   5,      4,      NUMERIC,    EQUATION,   NUMERIC], # 12 *
    [   3,      5,      5,      NUMERIC,    NUMERIC,    EQUATION], # 13 *
    [   3,      5,      1,      EQUATION,   EQUATION,   NUMERIC], # 14 *
    [   5,      5,      4.5,    NUMERIC,    EQUATION,   NUMERIC], # 15 *
    [   2.25,   4.5,    12,     EQUATION,   NUMERIC,    EQUATION], # 16 *
    [   1,      24,     2.25,   NUMERIC,    NUMERIC,    EQUATION], # 17 *
    [   3,      3,      1,      NUMERIC,    NUMERIC,    EQUATION], # 18 *
    [   3,      5,      1,      NUMERIC,    EQUATION,   NUMERIC], # 19 *
    [   7,      24,     4,      NUMERIC,    EQUATION,   NUMERIC], # 20 *
    [   1.25,   0.75,   0.75,   EQUATION,   EQUATION,   NUMERIC], # 21 *
    [   3/2,    3,      7,      NUMERIC,    EQUATION,   EQUATION], # 22 *
    [   1,      1,      12,     NUMERIC,    EQUATION,   NUMERIC] # 23 *
]


# triangles given by the school CORRECTED
# 24 (3553054)-> 0/4/1, 1/5/2, 2/7/1, 3/16/0, 4/23/1, 5/11/2, 6/0/1, 7/8/1, 8/3/1, 9/6/1, 10/17/1, 11/20/2, 12/21/1, 13/12/0, 14/1/0, 15/15/2, 16/2/2, 17/13/1, 18/22/2, 19/9/2, 20/10/2, 21/19/0, 22/18/1, 23/14/0,

triangles_available_corrected = [
    [   5,      1/3,    1.5,    NUMERIC,    EQUATION,   NUMERIC], # 0 *
    [   5,      6,      5,      NUMERIC,    EQUATION,   NUMERIC], # 1 *
    [   5,      4.5,    6,      NUMERIC,    EQUATION,   EQUATION], # 2 *
    [   0.5,    4,      8,      NUMERIC,    EQUATION,   NUMERIC], # 3 *      
    [   6,      5,      0.33,   EQUATION,   EQUATION,   NUMERIC], # 4 *
    [   0.4,    6,      3.5,    EQUATION,   NUMERIC,    EQUATION], # 5 *
    [   9/4,    6,      4,      NUMERIC,    NUMERIC,    NUMERIC], # 6 *
    [   9/4,    0.5,    2/5,    NUMERIC,    EQUATION,   NUMERIC], # 7 *
    [   8,      6,      1/3,    EQUATION,   NUMERIC,    NUMERIC], # 8 *
    [   1.5,    6,      4,      NUMERIC,    NUMERIC,    EQUATION], # 9 *
    [   5,      1.5,    3,      NUMERIC,    EQUATION,   EQUATION], # 10 *
    [   5/4,    0.5,    1.5,    NUMERIC,    NUMERIC,    EQUATION], # 11 *
    [   0.75,   5,      4,      NUMERIC,    EQUATION,   NUMERIC], # 12 *
    [   3,      5,      5,      NUMERIC,    NUMERIC,    EQUATION], # 13 *
    [   3,      5,      1,      EQUATION,   EQUATION,   NUMERIC], # 14 *
    [   5,      5,      4.5,    NUMERIC,    EQUATION,   NUMERIC], # 15 *
    [   2.25,   4.5,    12,     EQUATION,   NUMERIC,    EQUATION], # 16 *
    [   1,      24,     2.25,   NUMERIC,    NUMERIC,    EQUATION], # 17 *
    [   3,      3,      1,      NUMERIC,    NUMERIC,    EQUATION], # 18 *
    [   3,      5,      1,      NUMERIC,    EQUATION,   NUMERIC], # 19 *
    [   7,      24,     4,      NUMERIC,    EQUATION,   NUMERIC], # 20 *
    [   1.25,   0.75,   0.75,   EQUATION,   EQUATION,   NUMERIC], # 21 *
    [   3/2,    3,      7,      NUMERIC,    EQUATION,   EQUATION], # 22 *
    [   1,      1,      12,     NUMERIC,    EQUATION,   NUMERIC] # 23 *
]


triangles_available_33s = [
    [   5,      0.33,    1.5,    NUMERIC,    EQUATION,   NUMERIC], # 0 * !!!!
    [   5,      6,      5,      NUMERIC,    EQUATION,   NUMERIC], # 1 *
    [   5,      4.5,    6,      NUMERIC,    EQUATION,   EQUATION], # 2 *
    [   0.5,    4,      8,      NUMERIC,    EQUATION,   NUMERIC], # 3 *      
    [   6,      5,      0.33,   EQUATION,   EQUATION,   NUMERIC], # 4 *
    [   0.4,    6,      3.5,    EQUATION,   NUMERIC,    EQUATION], # 5 *
    [   4/9,    6,      4,      NUMERIC,    NUMERIC,    NUMERIC], # 6 *
    [   9/4,    0.5,    2/5,    NUMERIC,    EQUATION,   NUMERIC], # 7 *
    [   8,      6,      0.33,    EQUATION,   NUMERIC,    NUMERIC], # 8 * !!!
    [   1.5,    6,      4,      NUMERIC,    NUMERIC,    EQUATION], # 9 *
    [   5,      1.5,    3,      NUMERIC,    EQUATION,   EQUATION], # 10 *
    [   5/4,    0.5,    1.5,    NUMERIC,    NUMERIC,    EQUATION], # 11 *
    [   0.75,   5,      4,      NUMERIC,    EQUATION,   NUMERIC], # 12 *
    [   3,      5,      5,      NUMERIC,    NUMERIC,    EQUATION], # 13 *
    [   3,      5,      1,      EQUATION,   EQUATION,   NUMERIC], # 14 *
    [   5,      5,      4.5,    NUMERIC,    EQUATION,   NUMERIC], # 15 *
    [   2.25,   4.5,    12,     EQUATION,   NUMERIC,    EQUATION], # 16 *
    [   1,      24,     2.25,   NUMERIC,    NUMERIC,    EQUATION], # 17 *
    [   3,      3,      1,      NUMERIC,    NUMERIC,    EQUATION], # 18 *
    [   3,      5,      1,      NUMERIC,    EQUATION,   NUMERIC], # 19 *
    [   7,      24,     4,      NUMERIC,    EQUATION,   NUMERIC], # 20 *
    [   1.25,   0.75,   0.75,   EQUATION,   EQUATION,   NUMERIC], # 21 *
    [   3/2,    3,      7,      NUMERIC,    EQUATION,   EQUATION], # 22 *
    [   1,      1,      12,     NUMERIC,    EQUATION,   NUMERIC] # 23 *
]


# original triangles before beeing corected by the math teacher
# 16 (4880274)-> 0/9/2, 1/6/1, 2/2/1, 3/4/2, 4/8/2, 5/19/0, 6/10/0, 7/13/0, 8/15/2, 9/12/2, 10/3/2, 11/7/2, 12/18/2, 13/14/0, 14/1/1, 15/5/2, 
# 16 (9080619)-> 0/14/1, 1/18/0, 2/23/0, 3/19/1, 4/0/0, 5/10/2, 6/13/0, 7/2/0, 8/16/2, 9/7/0, 10/11/2, 11/21/0, 12/12/0, 13/3/2, 14/8/0, 15/22/2, 
# 16 (10106507)-> 0/15/1, 1/14/2, 2/13/0, 3/4/2, 4/8/2, 5/18/0, 6/10/1, 7/9/0, 8/1/2, 9/12/2, 10/3/2, 11/7/2, 12/23/1, 13/17/0, 14/20/2, 15/22/1, 
triangles_available_original = [
    [   5,      1/3,    1.5,    NUMERIC,    EQUATION,   NUMERIC], # 0 *
    [   5,      6,      5,      NUMERIC,    EQUATION,   NUMERIC], # 1 *
    [   5,      4.5,    6,      NUMERIC,    EQUATION,   EQUATION], # 2 *
    [   0.5,    4,      8,      NUMERIC,    EQUATION,   NUMERIC], # 3 *      
    [   6,      5,      0.33,   EQUATION,   EQUATION,   NUMERIC], # 4 *
    [   0.4,    6,      3.5,    EQUATION,   NUMERIC,    EQUATION], # 5 *
    [   4/9,    6,      4,      NUMERIC,    NUMERIC,    NUMERIC], # 6 *
    [   9/4,    0.5,    2/5,    NUMERIC,    EQUATION,   NUMERIC], # 7 *
    [   8,      6,      3,    EQUATION,   NUMERIC,    NUMERIC], # 8 *
    [   1.5,    6,      4,      NUMERIC,    NUMERIC,    EQUATION], # 9 *
    [   5,      1.5,    3,      NUMERIC,    EQUATION,   EQUATION], # 10 *
    [   5/4,    0.5,    1.5,    NUMERIC,    NUMERIC,    EQUATION], # 11 *
    [   0.75,   5,      4,      NUMERIC,    EQUATION,   NUMERIC], # 12 *
    [   3,      5,      5,      NUMERIC,    NUMERIC,    EQUATION], # 13 *
    [   3,      5,      1,      EQUATION,   EQUATION,   NUMERIC], # 14 *
    [   5,      5,      4.5,    NUMERIC,    EQUATION,   NUMERIC], # 15 *
    [   2.25,   4.5,    12,     EQUATION,   NUMERIC,    EQUATION], # 16 *
    [   1,      24,     2.25,   NUMERIC,    NUMERIC,    EQUATION], # 17 *
    [   3,      3,      1,      NUMERIC,    NUMERIC,    EQUATION], # 18 *
    [   3,      5,      1,      NUMERIC,    EQUATION,   NUMERIC], # 19 *
    [   7,      24,     4,      NUMERIC,    EQUATION,   NUMERIC], # 20 *
    [   1.25,   0.75,   0.75,   EQUATION,   EQUATION,   NUMERIC], # 21 *
    [   3/2,    3,      7,      NUMERIC,    EQUATION,   EQUATION], # 22 *
    [   1,      1,      12,     NUMERIC,    EQUATION,   NUMERIC] # 23 *
]

def get_triangle(triangles, triangle_no, position):
    if(position == POS_1):
        return [triangles[triangle_no][0], triangles[triangle_no][1], triangles[triangle_no][2], triangles[triangle_no][3], triangles[triangle_no][4], triangles[triangle_no][5]]
    elif(position == POS_2):
        return [triangles[triangle_no][2], triangles[triangle_no][0], triangles[triangle_no][1], triangles[triangle_no][5], triangles[triangle_no][3], triangles[triangle_no][4]]
    elif(position == POS_3):
        return [triangles[triangle_no][1], triangles[triangle_no][2], triangles[triangle_no][0], triangles[triangle_no][4], triangles[triangle_no][5], triangles[triangle_no][3]]
    



triangles_available = triangles_available_corrected