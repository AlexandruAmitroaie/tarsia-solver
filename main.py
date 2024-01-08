import pickle
import sys
from hexagon import Hexagon

from triangle import triangles_available




print("starting up")

hexagon = Hexagon()

hexagon.validate_matrix()

sys.setrecursionlimit(1000000000)

try:
    with open("state", "rb") as f:
        hexagon = pickle.load(f)
        # simple arrays are not serielized?
        hexagon.triangles_usage = hexagon.triangles_usage_wrapper[0]
        hexagon.placeholder_triangles_checked_forsolution = hexagon.placeholder_triangles_checked_forsolution_wrapper[0]

        is_running = hexagon.is_running()
        has_remaining_placehoder = hexagon.go_to_next_placeholder()
        # if we still have placeholders we try to fill them 
        if is_running and has_remaining_placehoder: 
            hexagon.find_placeholder_solution()
        else:
            print("Seems you have a solution or no other options to check")
except:
    print("no valid state to resume from ...")
    if hexagon.is_running():
        print("You should cp state.bak to state and resume")
    else:
        hexagon.reset_state(triangles_available)
        hexagon.resolve()


