# Windowing and the need for an online algorithm
Imagine that we are using Google Maps. When we move the window, we are essentially sending a query to the server to update the screen. Thus, to optimize the process time, we need to use an online algorithm, which means it will process the queries without having to load every initial data.

# Windowing and interval stabbing & intersection problems
In computer science, interval stabbing problem is the task of reporting all intervals in I that are stabbed by a point q. Assume that we have integer coordinates, we can put them into an interval tree.

Defining the problem:

The performance of segment trees is summarized in the following theorem:

## Theorem
A segment tree for a set I of n intervals uses O(n log n) storage and can be built in O(nlogn) time. Using the segment tree we can report all intervals that contain a query point in O(log n + k) time, where k is the number of reported intervals. 

## Query types
* Sum query
* Update query

# Algorithm
## Construct tree
Input: the set of intervals I
Output: the tree
* Compute x_median (the median of the set of all endpoints), and store x_median with a node v
* Compute I_mid and construct two sorted list for I_mid: L_left sorted for left endpoints and L_right sorted for right endpoints. Store these at v
* Set left child as constructtree(I_left), right child as constructtree(I_right)

## Query interval tree
Input: root v of the tree and a query point q_x
Output: all intervals that contain q_x


# Complexity analysis
Preprocessing time: O(n log n)

Query time: O(log n)

Some notes about the trees: https://stackoverflow.com/questions/17466218/what-are-the-differences-between-segment-trees-interval-trees-binary-indexed-t

# Source
https://cw.fel.cvut.cz/wiki/_media/misc/projects/oppa_oi_english/courses/ae4m39vg/lectures/10-windowing.pdf
http://www.sm.luth.se/csee/courses/smd/156/05/lectures/l10.pdf
http://www.cs.uu.nl/docs/vakken/ga/slides10.pdf
https://algo.kaust.edu.sa/documents/cs372l07.pdf

## Stabbing problem
http://www.cs.nthu.edu.tw/~wkhon/algo08-tutorials/tutorial-stabbing.pdf
http://www2.tu-ilmenau.de/combinatorial-optimization/Schmidt2009a.pdf

## Segment tree
https://codereview.stackexchange.com/questions/47596/segment-tree-in-python3
https://discuss.leetcode.com/topic/45266/python-well-commented-solution-using-segment-trees