# Dijkstra's Algorithm & A\* Heuristic Algorithm

When it comes to searching-typed algorithms. There are generalized components of the algorithm. We can take the set of all the components for a searching algorithm to be **infrastructure** for this algorithm.

## List of Content

- [ ] [**Infrastructure of Search Algorithms**](#infrastructure-of-search-algorithm)
- [ ] [**Peformance of An Algorithm**](#performance-of-an-algorithm)
- [ ] [**Dijkstra's Algorithm**](#dijkstras-algorithm)
- [ ] [**A\* & Its Heuristics**](#a--heuristics)

### Infrastructure of Search Algorithm

1. State
2. Parent
3. Action
4. Path Cost

Suppose that we have a board with 9 cells as initia state.

```shell
1 2 3
4 5 6
7 8 9
```

Then, this board represent the node at the root with initial state of the details of the board itself.

```python
root_node : Node = Node(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
)
```

But because this is the `root` node of the tree it DOES NOT have a parent node.

```python
print(root_node.parent) # None
```

Now suppose that at the root node are able to change the board representation so that it may look something like

```shell
2 1 3
4 5 6
7 8 9
```

At the next state, the only change made was `swap '1' with '2'`. In other words, the item 1 of the table moved to right after pushing '2' back to its position.

In this case, the action was 'to move right' and 'to move left' for different items.

And, because there were 2 moves, there was a path cost of 2 at on this action period.

Analyzing and constructing such system of an algorithm is called **infrastructure for the algorithm**. For search algorithms, it is generally the case that we deal with these four components at minimum (state, parent, action, and path cost) for each node in the tree.

### Performance of an Algorithm

By now we know what there are many different search algorithms (we will discuss more of them in the below sections). Now the questions may arise along with what is suitable or what is better for the case A, B, and C, ...and so on.

These types of questions are ultimately asking for the algorithm's performance (measuring performance).

There are a few aspects to discuss when discussing the measurement of performance.

1. Completeness
2. Optimality
3. Time Complexity
4. Space Complexity

**Completeness** of an algorithm is defined to be the change of finding a solution if any exists to a problem.

Suppose that we are here to solve a problem as below

```shell
1 2 3
4 5 6
7 8 9
```

**Problem 1.** Find at least one solution (path) from 1 to 9 without passing cells that have odd numbers. No diagonal move is allowed.

This problem we can start at the initial state of the current board representation. The next state may be something like

```shell
2 1 3
4 5 6
7 8 9

# or

4 2 3
1 5 6
7 8 9
```

From this state, we have NO WAY to further expand because of the restriction that we CANNOT move diagonally and we CANNOT pass via odd numbers.

So, we may say that our algorithm's performance for this problem cannot determine its completeness. In fact it might not even be a factor because we have no solution to this problem.

**Problem 2.** Now suppose that our board consists of 9 cells where only two cells are filled with pointers

```shell
i ~ ~
~ ~ ~
~ ~ f
```

and our goal is **to get from i to f**. Also, we do not have any restriction on our movement of action except that we can only move one by one (CANNOT jump 2 cells in the neighborhood).

In this specific problem, depending on which strategies we use, meaning which algorithms we use, we MAY END UP with looping infinitely, thus cannot gurantee to find a solution. This can happen becasue we do not have any restriction on move except path cost is just one per move. This means that we can revisit the cell we already passed previously.

Depending on the algorithms we use to solve this problem, we may be able to say either, the algorithms `[A, B, C, ...]` is complete or incomplete.

**Optimality** is defined as the optimal solution of all the possible solutions to a problem.

If there is just one solution to a problem, we do not even need to consider the optimality of an algorithm to measure its performance (optimality is not a factor).

However, just like the **Problem 2** above, if we could have more than one solutions, this means that we may find a better solution, and even the best solution of all. From the `./searching_strategies.md` we found out that optimality can be measured using the path cost comparisons between possible solutions.

Suppose that we need 1 to get to where 0 is in the table below. We can only spend one path cost per move, and we can move diagonally this time.

```shell
1 x x
x x x
x x 0
```

We can already visualize many paths (solutions) of this problem. Moreover, we can already tell which one takes the LEAST path cost (meaing the least # of movement to reach the goal).

```shell
# state1
1 x x
x x x
x x 0

# state2
x x x
x 1 x
x x 0

# state3
x x x
x x x
x x 1,0
```

With just about the total path cost of 2, we are able to get to the cell where 0 is. The reason for this solution is the only optimal solution is because for any other solutions `S_n`, their totla path costs `P(S_n)` is greater than 2.

**Time Complexity**

...

**Space complexity**

...

### Dijkstra's Algorithm

If we revisit back to where we discussed one of the first search algorithms **Breadth First Search** or **BFS**, we know that each path cost was sort of assumed to be uniform. Meaning that each move cost 1 regardless of its direction, level, or any other factors.

**BFS** is using the abstract data structure called `Queue` which you can see a simple implementation `./implementation/queue.ipynb` or [here](./implementation/queue.ipynb).

We can think of **Dijkstra's Algorithm** as the same with **BFS** when it deals with uniform cost, but differs when each node will represent different path cost, thus having 'Not Uniform Cost'. This means the following.

```shell
# uniform cost paths
1 a b
c d e

path_cost(1, a) == path_cost(1, c) == path_cost(a, b) == path_cost(a, d) ...
```

The example for non-uniform-cost structure will look something like this

```shell
A B C
  D E F
    G H I

# total path cost 4 from A to D
path_cost(A->B) = 1
path_cost(B->D) = 3

# totla path cost 5 from A to D
path_cost(A->D) = 5
```

So in this particular non-uniform-cost path finding proble, from 'A' to 'D', we may find it more optimal if we choose to go to 'B' first, then to 'D', rather than from 'A' directly to 'D'

This is where **Dijkstra's Algorithm** will be efficient in finding optimal path solution.

**Dikjstra's Algorithm** uses a special type of Queue called `Priority Queue` or `PQueue` for short, I implement a simple `PQueue` at `./implementation/priority_queue.ipynb` or click [here](./implementation/priority_queue.ipynb)

### A\* & Heuristics

**A\* Search** is a search algorithm most known for its ability to minimize the path cost WITHOUT overestimation.

Suppose that we are dealing with a problem that is non-uniform-cost based.

```shell
A (1) - B (3) - C
        | (3)   | (1)
        D (5) - E
```

From the node _A_ to node _E_, there are two paths we can see right away.

Path 1. `A -> B -> C -> E` : `Cost(Path 1) == 1 + 3 + 1 = 5`
Path 2. `A -> B -> D -> E` : `Cost(Path 2) == 1 + 3 + 5 = 9`

We know that Path 1 is the optimal solution here but we can further dissect this problem in a more computational logic.

Notice that for both paths, upto the node _B_ the path cost are summed to the same amount `A -> B` : `Cost(A -> B) = 1`, this means that at the node _B_ we need to make an informed decision to get to the goal more efficiently (essentially paying less path cost).

Thus, we can define the function for estimation of the cheapest cost `f(n)`

$$
    f(n) = g(n) + h(n)
$$

where `g(n)` represents the path cost from the start path point up to the current path point and `h(n)` represnets the estimated cheapest path cost from the current point to the goal point.
