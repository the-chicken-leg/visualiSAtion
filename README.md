# visualiSAtion

The proper spelling is obviously visuali***Z***ation, but then I couldn't vizualize the (data) ***S***tructures and ***A***lgorithms... get it?

Each subfolder is the name of a data structure or algorithm. The _main.py file in each subfolder includes "tuneables" - have fun!

## Run on Windows with uv

1. Install uv using PowerShell (full instructions here: https://docs.astral.sh/uv/getting-started/installation):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Verify uv installed correctly:

```powershell
uv --version
```

3. Clone repo (requires git):

```powershell
git clone https://github.com/the-chicken-leg/visualiSAtion
```

4. Run using uv. On the first run, uv will download the appropriate python version, create a venv, and install dependencies, which might take some time. Subsequent runs will be faster:

```powershell
Set-Location .\visualiSAtion\
uv run .\visualiSAtion.py breadth_first_search
```

## Depth-first search random

![dfs random gif](/media/dfs_random.gif)

## Depth-first search non-random

![dfs non-random gif](/media/dfs_nonrandom.gif)

## Breadth-first search

![bfs gif](/media/bfs.gif)

## Stack

![stack gif](/media/stack.gif)

## Queue

![queue gif](/media/queue.gif)

## Red-black tree

![red-black tree gif](/media/red_black_tree.gif)

## Bubble sort

![bubble sort gif](/media/bubble_sort.gif)

## Selection sort

![selection sort gif](/media/selection_sort.gif)

## Insertion sort

![insertion sort gif](/media/insertion_sort.gif)

## Merge sort

![merge sort gif](/media/merge_sort.gif)

## Quick sort

![quick sort gif](/media/quick_sort.gif)
