# Windowing and the need for an online algorithm
Imagine that we are using Google Maps. When we move the window, we are essentially sending a query to the server to update the screen. Thus, to optimize the process time, we need to use an online algorithm, which means it will process the queries without having to load every initial data.

# Windowing and RMQ problem
In computer science, a range minimum query (RMQ) solves the problem of finding the minimal value in a sub-array of an array of comparable objects. Range minimum queries have several use cases in computer science such as the lowest common ancestor problem or the longest common prefix problem (LCP).

Now, in computational geometry, it turns out that the windowing problem is equivalent to a RMQ problem. Indeed, we store the segment endpoints and determine whether they are in the window or not. Project the segments on two axes, we have a RMQ problem for two dimensions.

# Complexity analysis
Preprocessing time: O(n log n)
Query time: O(log n)