import argparse

from breadth_first_search.breadth_first_search_main import run_breadth_first_search
from bubble_sort.bubble_sort_main import run_bubble_sort
from depth_first_search.depth_first_search_main import run_depth_first_search

def run_vis():
    DISPATCH = {
        "breadth_first_search": run_breadth_first_search,
        "bubble_sort": run_bubble_sort,
        "depth_first_search": run_depth_first_search,
    }

    parser = argparse.ArgumentParser(
        prog="vis.py",
        description="visualiSAtion of (data) Structures and Algorithms",
    )
    parser.add_argument(
        "dsa",
        choices=DISPATCH.keys(),
        help="data structure or algorithm to run"
    )
    args = parser.parse_args()

    handler = DISPATCH[args.dsa]
    handler()

if __name__ == "__main__":
    run_vis()
