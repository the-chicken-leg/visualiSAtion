import argparse

from breadth_first_search.breadth_first_search_main import run_breadth_first_search
from bubble_sort.bubble_sort_main import run_bubble_sort
from depth_first_search.depth_first_search_main import run_depth_first_search
from insertion_sort.insertion_sort_main import run_insertion_sort
from merge_sort.merge_sort_main import run_merge_sort
from queue.queue_main import run_queue
from quick_sort.quick_sort_main import run_quick_sort
from red_black_tree.red_black_tree_main import run_red_black_tree
from selection_sort.selection_sort_main import run_selection_sort

def run_vis():
    DISPATCH = {
        "breadth_first_search": run_breadth_first_search,
        "bubble_sort": run_bubble_sort,
        "depth_first_search": run_depth_first_search,
        "insertion_sort": run_insertion_sort,
        "merge_sort": run_merge_sort,
        "queue": run_queue,
        "quick_sort": run_quick_sort,
        "red_black_tree": run_red_black_tree,
        "selection_sort": run_selection_sort,
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
