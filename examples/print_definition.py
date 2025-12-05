import sys
import os

from pose_skeletons import get_skeleton_def

def main():
    """
    A minimal example demonstrating how to fetch a skeleton definition
    and print its hierarchy.
    """
    # Get the definition from the registry by name
    optitrack_def = get_skeleton_def("optitrack")
    
    # The __repr__ of the SkeletonDefinition is overloaded to print the tree
    print(optitrack_def)

if __name__ == "__main__":
    main()
