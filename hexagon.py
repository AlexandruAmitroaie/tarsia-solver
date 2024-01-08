
import pickle
import shutil
import os
from pathlib import Path
from triangle import POS_1, POS_2, POS_3, get_triangle


NEIGHBOUR = 'N'
FREE = 'F'
NOTHING = '-'

# this is the format of the matrix 
# first three values specify if the current placeholder has placeholders as neighbours or not 
# next three values specify which are the neighbours 
# next three values specify which are the edges to check on the neighbours 
EDGE_0_TYPE = 0 # on which position in the vector is specified the edge type. Type can be NEIGHBOUR or FREE or NOTHING
EDGE_0_NEIGHBOUR = 3 # in which position in the vector is the neighbour specified 
EDGE_1_TYPE = 1
EDGE_1_NEIGHBOUR = 4
EDGE_2_TYPE = 2
EDGE_2_NEIGHBOUR = 5
EDGE_0_NEIGHBOUR_EDGE = 6
EDGE_1_NEIGHBOUR_EDGE = 7
EDGE_2_NEIGHBOUR_EDGE = 8

EDGE_0 = 0
EDGE_1 = 1
EDGE_2 = 2 

# information that we store about the solution
TRIANGLE_NO = 0 
TRIANGLE_POSITION = 1 

class Hexagon:

    

    matrix = [
        # line 1
        [ FREE,         NEIGHBOUR,  NEIGHBOUR,  -1,  1,  6,     -1,         EDGE_0,     EDGE_1   ],
        [ NEIGHBOUR,    FREE,       NEIGHBOUR,  0,  -1,  2,     EDGE_1,     -1,         EDGE_0   ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  1,  3,  8,      EDGE_2,     EDGE_0,     EDGE_1   ],
        [ NEIGHBOUR,    FREE,       NEIGHBOUR,  2,  -1,  4,     EDGE_1,     -1,         EDGE_0   ],
        [ NEIGHBOUR,    FREE,       NEIGHBOUR,  3,  -1,  10,    EDGE_2,     -1,         EDGE_1   ],
        # # line 2
        [ FREE,         NEIGHBOUR,  NEIGHBOUR,  -1,  6,  12,    -1,         EDGE_0,     EDGE_1  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  5,  0,  7,      EDGE_1,    EDGE_2,    EDGE_0  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  6,  8,  14,     EDGE_2,    EDGE_0,    EDGE_1  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  7,  2,  9,      EDGE_1,    EDGE_2,    EDGE_0    ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  8,  10, 16,     EDGE_2,    EDGE_0,    EDGE_1  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  9,  4,  11,     EDGE_1,    EDGE_2,    EDGE_0 ],
        [ NEIGHBOUR,    FREE,       NEIGHBOUR,  10, -1,  18,    EDGE_2,    -1,        EDGE_1  ],
        # line 3
        [ FREE,         NEIGHBOUR,  NEIGHBOUR,  -1,  5,  13,    -1,         EDGE_2,   EDGE_0  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  12, 14, 19,     EDGE_2,     EDGE_0,   EDGE_1  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  13, 7,  15,     EDGE_1,     EDGE_2,   EDGE_0  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  14, 16, 21,     EDGE_2,     EDGE_0,   EDGE_1  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  15, 9,  17,     EDGE_1,     EDGE_2,   EDGE_0  ],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  16, 18, 23,     EDGE_2,     EDGE_0,   EDGE_1  ],
        [ NEIGHBOUR,    NEIGHBOUR,  FREE,       17, 11, -1,     EDGE_1,     EDGE_2,   -1],
        # line 4
        [ FREE,         NEIGHBOUR,  NEIGHBOUR,  -1,  13, 20,    -1,         EDGE_2,     EDGE_0],
        [ NEIGHBOUR,    NEIGHBOUR,  FREE,       19, 21, -1,     EDGE_2,     EDGE_0,     -1],
        [ NEIGHBOUR,    NEIGHBOUR,  NEIGHBOUR,  20, 15, 22,     EDGE_1,     EDGE_2,     EDGE_0],
        [ NEIGHBOUR,    NEIGHBOUR,  FREE,       21, 23, -1,     EDGE_2,     EDGE_0,     -1   ],
        [ NEIGHBOUR,    NEIGHBOUR,  FREE,       22, 17, -1,     EDGE_1,     EDGE_2,     -1]
    ]


    # those are the triangles we will work  with 
    triangles = []
    
    # will store the triangles in the final solution 
    # it has 2 elements:
    # TRIANGLE_NO - which is the triangle included in the solution 
    # TRIANGLE_POSITION - which is the position of the triangle . A triangle can have 3 positions: POS_1, POS_2, POS_3
    solution = []
    # here we store for each placeholder the last triangle no checked 
    placeholder_triangles_checked_forsolution = [] 
    placeholder_triangles_checked_forsolution_wrapper = []
    # here we stored which triangle matched for the solution
    # solution_triangle_no = []
    # solution_triangle_position = []

    # will specify which triangles are used 
    triangles_usage = []
    triangles_usage_wrapper = []
    

    # current placeholder we are working on
    placeholder = 0

    # the maximum placeholder that we ever had
    max_placeholder = 0

    # here we are storing the information about the current triangle we are working on 
    working_triangle = None
    working_position = None #this is the position of the triangle can be POS_0, POS_1 of POS_2 
    working_triangle_no = None # this is the number of the tirangle that we work with  


    recursion = 0

    def validate_matrix(self):
        current_placeholder = 0
        for placeholder in self.matrix:
            if(current_placeholder != 0):
                placeholder_valid = True
                # we check all the cases when placeholdes are not valid
                # edge 1  
                if(placeholder_valid 
                   and placeholder[EDGE_0_TYPE] == FREE 
                   and placeholder[EDGE_0_NEIGHBOUR] != -1): placeholder_valid = False
                if(placeholder_valid 
                   and placeholder[EDGE_0_TYPE] == NEIGHBOUR 
                   and placeholder[EDGE_0_NEIGHBOUR] == -1): placeholder_valid = False
                # repeat for all edges... we can optimize this
                if(placeholder_valid 
                   and placeholder[EDGE_1_TYPE] == FREE 
                   and placeholder[EDGE_1_NEIGHBOUR] != -1): placeholder_valid = False
                if(placeholder_valid 
                   and placeholder[EDGE_1_TYPE] == NEIGHBOUR 
                   and placeholder[EDGE_1_NEIGHBOUR] == -1): placeholder_valid = False
                # and edge 3
                if(placeholder_valid 
                   and placeholder[EDGE_2_TYPE] == FREE 
                   and placeholder[EDGE_2_NEIGHBOUR] != -1): placeholder_valid = False
                if(placeholder_valid 
                   and placeholder[EDGE_2_TYPE] == NEIGHBOUR 
                   and placeholder[EDGE_2_NEIGHBOUR] == -1): placeholder_valid = False

                if(not placeholder_valid): 
                    print("Validation of placeholder in position ",current_placeholder, " : ", placeholder_valid)
                    raise Exception("Wrong configuration for placeholder in position:  ", current_placeholder)
            current_placeholder = current_placeholder +1 

        print("Validation of placeholders configuration passed!")

    def is_there_a_working_triangle(self):
        if(self.working_triangle != None):
            return True
        else:
            return False

    def get_next_triangle(self):

        found = False 
        
        # we first try all current triangle positions
        if(self.is_there_a_working_triangle()):
            
            if not found and self.working_position == POS_1:
                self.working_position = POS_2
                self.working_triangle = get_triangle(self.triangles, self.working_triangle_no, self.working_position)
                found = True

            if not found and self.working_position == POS_2:
                self.working_position = POS_3
                self.working_triangle = get_triangle(self.triangles, self.working_triangle_no, self.working_position)
                found = True 

        if not found:
            # if no more positions are available we go to the next triangle 
            i = 0
            for triangle in self.triangles:
                # if triangle was not used for other placeholder or checked for our own 
                if not found and not self.triangles_usage[i] and i > self.placeholder_triangles_checked_forsolution[self.placeholder]:
                    self.working_position = POS_1
                    self.working_triangle = get_triangle(self.triangles, i, self.working_position)
                    self.working_triangle_no = i
                    # we marked this as beeing used for this placeholder
                    if self.placeholder >= len(self.placeholder_triangles_checked_forsolution):
                        raise Exception("Cannot mark placeholder as checked. Placeholder number not valid")
                    self.placeholder_triangles_checked_forsolution[self.placeholder] = i
                    found = True
                    break 
                    
                i = i + 1

        return found 


    def check_matching(self, placeholder_requierments, triangle, EDGE_NO, EDGE_NO_TYPE, EDGE_NO_NEIGHBOUR, EDGE_NO_NEIGHBOUR_EDGE):
        matching = True
        if placeholder_requierments[EDGE_NO_TYPE] == NEIGHBOUR:
            neighbour_to_check = placeholder_requierments[EDGE_NO_NEIGHBOUR]
            if neighbour_to_check < len(self.solution):
                # means we already fill the neighbour placeholder ( if it is empty we have no consraints)
                neighbour_triangle_no = self.solution[neighbour_to_check][TRIANGLE_NO]
                neighbour_triangle_position = self.solution[neighbour_to_check][TRIANGLE_POSITION]
                neighbour_triangle = get_triangle(self.triangles, neighbour_triangle_no, neighbour_triangle_position)
                neighbour_edge_to_check =  placeholder_requierments[EDGE_NO_NEIGHBOUR_EDGE]
                placeholder_triangle_edge_value = triangle[EDGE_NO]
                placeholder_triangle_edge_type = triangle[EDGE_NO + 3]
                neighbour_triangle_edge_value = neighbour_triangle[neighbour_edge_to_check]
                neighbour_triangle_edge_type = neighbour_triangle[neighbour_edge_to_check + 3]
                if(placeholder_triangle_edge_value != neighbour_triangle_edge_value) or (placeholder_triangle_edge_type == neighbour_triangle_edge_type): 
                    matching = False

        return matching   


    # checks if the provided triangle matches the current placeholder 
    def is_triangle_matching(self, triangle):
        # sample triangle:     [   3,      3,      1,      NUMERIC,    NUMERIC,    EQUATION]
        # sample requierment:  [ NEIGHBOUR,    FREE,       NEIGHBOUR,  2,  -1,  4   ]
        
        triangle_matching = True
        placeholder_requierments = self.matrix[self.placeholder]
        edge_0_match = self.check_matching(placeholder_requierments, triangle, EDGE_0, EDGE_0_TYPE, EDGE_0_NEIGHBOUR, EDGE_0_NEIGHBOUR_EDGE)
        edge_1_match = self.check_matching(placeholder_requierments, triangle, EDGE_1, EDGE_1_TYPE, EDGE_1_NEIGHBOUR, EDGE_1_NEIGHBOUR_EDGE)
        edge_2_match = self.check_matching(placeholder_requierments, triangle, EDGE_2, EDGE_2_TYPE, EDGE_2_NEIGHBOUR, EDGE_2_NEIGHBOUR_EDGE)

        triangle_matching = edge_0_match and edge_1_match and edge_2_match

        return triangle_matching
    

    

    def print_solution(self):
        # print("size -> placeholder / triangle_no / triangle_position")
        state = "{} ({})-> ".format(len(self.solution), self.recursion)
        for i in range(len(self.solution)):
            # placeholder number / triangle number / triangle position
            state = state + "{}/{}/{},".format(i, self.solution[i][TRIANGLE_NO], self.solution[i][TRIANGLE_POSITION])

        print(state)
    

    def write_solution_to_file(self):
        if self.placeholder < self.max_placeholder:
            return

        with open("solution.txt", "a") as f:
            f.write("{} ({})-> ".format(len(self.solution), self.recursion))
            for i in range(len(self.solution)):
                # placeholder number / triangle number / triangle position
                f.write("{}/{}/{}, ".format(i, self.solution[i][TRIANGLE_NO], self.solution[i][TRIANGLE_POSITION]))
            f.write("\n")

        self.max_placeholder = self.placeholder
  

    # marks working triangle as solution for current placeholder
    def mark_solution(self):

        # confirm that solution has the correct size 
        if len(self.solution) != self.placeholder:
            raise Exception("Number of elements in solution not matching current placeholder position")

        # we save the solution
        self.solution.append([self.working_triangle_no, self.working_position]) 
        # we mark the triangle as used
        if(self.working_triangle_no >= len(self.triangles_usage)):
            raise Exception("Cannot mark triangle as used. Triangle number not valid")

        self.triangles_usage[self.working_triangle_no] = True 

         # reset the working triangle 
        self.working_position = None
        self.working_triangle = None
        self.working_triangle_no  = None

        self.print_solution()

        self.save_state()

        self.write_solution_to_file()


    # def placeholder_get_triangle(self):
    #     return self.solution[self.placeholder][TRIANGLE_NO]
    
    # def placeholder_get_triangle_position(self):
    #     return self.solution[self.placeholder][TRIANGLE_POSITION]

    
    def go_to_next_placeholder(self):
        if self.placeholder + 1 < len(self.matrix):
                # we go to the next position 
                self.placeholder = self.placeholder + 1
                return True
        else:
            return False
        
    def go_back(self):
        if(self.placeholder > 0):
            self.placeholder = self.placeholder - 1 
            if len(self.solution) == 0:
                raise Exception("Cannot go back. No more elements in solution")
            [self.working_triangle_no, self.working_position] = self.solution.pop()
            # we reinitiate the working triangle so we coudl advance with the search
            
            if self.working_triangle_no >= len(self.triangles):
                raise Exception("Cannot go back. Triangle number not valid")
            self.working_triangle = self.triangles[self.working_triangle_no]

            if self.working_triangle_no >= len(self.triangles_usage):
                raise Exception("Cannot go back. Triangle usage not valid")
            self.triangles_usage[self.working_triangle_no] = False
            
            # we reset triangles checked as well
            if self.placeholder >= len(self.placeholder_triangles_checked_forsolution):
                raise Exception("Cannot go back. Placeholder checked not valid")
            self.placeholder_triangles_checked_forsolution[self.placeholder] = self.working_triangle_no

            if self.placeholder + 1  >= len(self.placeholder_triangles_checked_forsolution):
                raise Exception("Cannot go back. Previous placeholder checked not valid")
            self.placeholder_triangles_checked_forsolution[self.placeholder + 1] = -1
            return True
        else: 
            print("No more placeholders to fill.")
            self.set_state_finished()
            return False



    def find_placeholder_solution(self):
        self.recursion = self.recursion + 1
        # if self.recursion == 15366: 
        #     print("we are here") 

        found = self.get_next_triangle()
        
        if not found:
            # if the leght of solution is equal with placeholders it means we have a compleated solution
            if(len(self.solution) == len(self.matrix)):
                print("FOUND A SOLUTION")
                self.set_state_finished()
                return False;
            else:
                # we go back one placeholder
                viable = self.go_back()
                # here we should try to get back
                if viable: 
                    return self.find_placeholder_solution()
                else:
                    print("Cannot go back")
                    self.set_state_finished()
                    return False

        matching = self.is_triangle_matching(self.working_triangle)
        if(matching):
            self.mark_solution() 
            has_remaining_placehoder = self.go_to_next_placeholder()
            # if we still have placeholders we try to fill them 
            if has_remaining_placehoder: 
                return self.find_placeholder_solution()
            else: 
                print("No remaining placeholders.")
                self.set_state_finished()
                return False
        else: 
            # we try another triangle  
            return self.find_placeholder_solution()
            
            
        
        
    def reset_state(self, triangles: []):
        # we've got our triangles, let's work out a solution 
        self.triangles = triangles

        # we ensure we start on blank 
        self.solution = []

        for plc in self.matrix: self.placeholder_triangles_checked_forsolution.append(-1)
        
        # no triangles are used yet
        for trinalge in triangles: self.triangles_usage.append(False)

        # let's fill in the placeholders
        # we start with first placeholder
        self.placeholder = 0

        self.recursion = 0

        self.set_state_running()

    def save_state(self):
        self.triangles_usage_wrapper = [self.triangles_usage]
        self.placeholder_triangles_checked_forsolution_wrapper = [self.placeholder_triangles_checked_forsolution]
        if os.path.exists("state"):
            shutil.copyfile("state", "state.bak")
        with open("state", "wb") as f:
            pickle.dump(self, f)


    def is_running(self):
        return os.path.exists("state.running")
        
    def set_state_running(self):
        if not os.path.exists("state.running"):
            Path('state.running').touch()

    def set_state_finished(self):
        if os.path.exists("state.running"):
            os.remove("state.running")

    def resolve(self):
        self.find_placeholder_solution()

