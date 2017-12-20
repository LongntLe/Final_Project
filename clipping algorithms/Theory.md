<style TYPE="text/css">
code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;}
</style>
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'] // removed 'code' entry
    }
});
MathJax.Hub.Queue(function() {
    var all = MathJax.Hub.getAllJax(), i;
    for(i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

# Introduction
Windowing algorithm is a crucial part in map algorithm. Whenever we move the map, the server immediately loads the objects that lie within our screen. But, how do computers determine whether an object is in our view or not? Also, how can we do that effectively? Our package will address that problem with the use of range tree and effective algorithm implementation.

# Windowing and the need for an online algorithm
Imagine that we are using Google Maps. When we move the window, we are essentially sending a query to the server to update the screen. Consider a naive implementation of the range check algorithm, we have to load the database and sequentially check each item to see if it has any intersection with the window. However, we can see that this algorithm is incredibly inefficient, as well as resource consuming.

Thus, to optimize the process time, we need to use an online algorithm, which means it will process the queries without having to load every initial data.

The performance of segment trees is summarized in the following theorem:

## Theorem
A segment tree for a set I of n intervals uses $O(n log n)$ storage and can be built in O(nlogn) time. Using the segment tree we can report all intervals that contain a query point in $O(log n^d + k)$ time, where k is the number of reported intervals, and is the number of dimensions. 

## Operations
a/ Window transformations
* Window translation
* Window zoom in and out (screen homothety)
b/ Query operations
* Find all objects that can be display in the window
* Update query
For each window translation query, we need to update the objects that are inside the window.

# Algorithm
## Construct tree
Input: the set of intervals I
Output: the tree
* Compute x_median (the median of the set of all endpoints), and store x_median with a node v
* Compute I_mid and construct two sorted list for I_mid: L_left sorted for left endpoints and L_right sorted for right endpoints. Store these at v
* Set left child as constructtree(I_left), right child as constructtree(I_right)

## Query interval tree
Input: root v of the tree and a query point $q_x$
Output: all intervals that contain $q_x$

# Complexity analysis
Preprocessing time: $O(n log n)$

Query time: $O(log n)$

Some notes about the trees: https://stackoverflow.com/questions/17466218/what-are-the-differences-between-segment-trees-interval-trees-binary-indexed-t

# Application
This algorithm allows us to quickly update the map, without having to load every single data point. In video games, optimizing clipping methods mean that we can maximize visual quality of the game, thus the overall player's experience.

# Installation



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