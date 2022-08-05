# Searching Strategies & Iterative Search Algorithms

From the previous module [Problem Solving](./problem_solving.md), one thing that we kind of ignore was the number of steps moving one state to another in our problem solving process, specifically within our action.

In this module, I will explore deeper into understanding **solution** which is just a proper way of saying the movement from initial state to goal state. Moreover, we know that there could be more than one ways to find **solution** to a problem. If that is the case, we may infer that there will be an **optimal solution**.

## List of Content

- [ ] [**Optional Solution**](#optimal-solution)
- [ ] [**Iterative Seaching**](#iterative-searching)
- [ ] [**Iterative Search Algorithms**](#iterative-searching-algorithms-bfs-and-dfs)

### Optimal Solution

For a specific problem we formulate, we define action and its processes in order to get initial state to the goal state.

In this module I will use thef following example.

```shell
# initial state board

| 0 | A | B |
| C | D | E |
| F | G | 1 |
```

Our initial state represents the starting point of the board at index [0, 0] and the goal point at index [2, 2]. Our goal is indeed to take the element at the starting point '0' to our goal point where '1' is resting at.

If we collect all the possible solutions (a set of solutions that will take 0 to the position of 1), we can draw the following sequence

```shell
solutions = {
    [0, 'A', 'B', 'E', 1],
    [0, 'A', 'D', 'E', 1],
    [0, 'A', 'D', 'G', 1],
    [0, 'A', 'C', 'F', 'G', 1]
    .
    .
    .
    # a lot of solutions...
}
```

Our movement is restricted in that we can only move up, down, left, or right per time. Also, we restrict our move in a way that we cannot revisit the point we have already passed.

We often say that we have **path cost** for each move we make in our action. In our set of solutions, we can think of each element as one solution and the **length of solution** as the path cost for that solution.

For the first 3 solutions in our solution set, they all have path cost of 4 while the 4th solution in the set has path cost of 5. From this we can conclude for sure that any solutions between solution 1 to soltuion 3 is a better solution when compared to solution 4 **because they have less path cost** in achieving the goal state.

Now suppose that we have 100 solutions, and all the solutions in the set has path cost more than or equal to 3, except solutuon 99, which has path cost of 2.

From the above stateent, we can conclude that **solution 99 (s_99) is the optimal solution for our solution set S**

$$
 \text{A solution is optimal if given a set solutions S, O(S) = min(p(S))}\newline
 \text{where p represnet path cost function.}
$$

Basially means that given multiple solutions to a problem, if there is a solution that has minimum path cost, that solution is optimal for this problem.

Now, let's extend our move restriction and say that we are able to move diagonally. Then our solutions may look something like this.

```shell
# initial state board

| 0 | A | B |
| C | D | E |
| F | G | 1 |

solutions = {
    [0, 'A', 'B', 'E', 1],
    [0, 'A', 'D', 'E', 1],
    [0, 'A', 'D', 'G', 1],
    [0, 'A', 'C', 'F', 'G', 1]
    .
    .
    .
    [0, 'D', 1],
    .
    .
    .
    # a lot of solutions...
}
```

From this we know that once we extend our movement rule to allow diagonal movement, then the optimal solution to our problem will be `[0, 'D', 1]` which has least path cost of 3. We can also think of this as a **shortest path** when taking it from initial state to the goal state.

Now that we know what the path cost is when taking actions. We can truely focus on the step by step mechanisms of problem solving.

The first approach we will look at is what is known as **iterative searching**.

### Iterative Searching

From programming perspectives, we know that `to iterate` means to `to move step by step` or `loop one by one`. I believe that these terms are enough to help us understand what **iterative searching** means.

After we formulate a problem, we need to actually solve it. For every action we take, we can consider this as expanding a new branching tree.

#### What is a Tree

A tree is a visual representation where each node is defined relative to its level and children nodes, if any.

```shell
# tree example
----------------1--------------- root : level 0 : root node (1)
--------2              3-------- branch : level 1 : internal nodes (2)(3)
----4       5      6       7---- leaf : level 2 : leaf nodes (4)(5)(6)(7)
```

A tree consists of interpretable components including **nodes**, **level**, and other features.

Regarding our original problem, we can think of **node** as a state. Because there can be many varying states given a movement. We know that initial state is at the root node with children (in this case 2 children nodes). Our problem actually could have two or three children nodes as second level states depending on whether we can move diagonally or not.

```shell
# initial state board

| 0 | A | B |
| C | D | E |
| F | G | 1 |

# next state board (1)
| A | 0 | B |
| C | D | E |
| F | G | 1 |

# next state board (2)
| C | A | B |
| 0 | D | E |
| F | G | 1 |

# next state board (3), if able to move diagonally
| D | A | B |
| C | 0 | E |
| F | G | 1 |
```

For each options at second state, now we can recursively do the similar process as when we were at initial state. Now starting from the third state, depending on if we can revisit the path we took or not, there could be infinite set of nodes at state 4.

For obvious reasons, I'd like to restrict that rule because our goal is to find the shortest path from 0 to 1. This is important that **for computers to know the optimal solution**, it needs to explore all possible paths.

This means that we have to iteratively search each node for a path until it reaches the last level of node in that path.

The following list is the set of solutions (paths) that takes us from initial state (0) to the goal state(1).

```python
solutions_no_diagonal_movements = [
    [0, 'A', 'B', 'E', 1], # path costs : 5 (optimal)
    [0, 'A, 'D', 'E', 1], # path costs : 5 (optimal)
    [0, 'A', 'D', 'G', 1], # path costs : 5 (optimal)
    [0, 'A', 'D', 'C', 'F', 'G', 1], # path costs: 7
    [0, 'C', 'D', 'A', 'B', 'E', 1], # path costs: 7
    [0, 'C', 'D', 'E', 1], # path costs 5 (optimal)
    [0, 'C', 'D', 'G', 1], # path costs 5 (optimal)
    [0, 'C', 'F', 'G', 1], # path costs 5 (optimal)
    [0, 'C', 'F', 'G', 'D', 'E', 1], # path costs: 7
    [0, 'C', 'F', 'G', 'D', 'A', 'B', 'E', 1] # path costs: 9 (worst)
]
```

### Iterative Searching Algorithms BFS And DFS

There are two popular searching algorithms we can take a look at. They have some common features such as they can be represented in a tree form that we discussed above. Second is that they will guarantee that we will have at least one solution (finding path from the initial state to the goal state). But they do have some significant differences and that they are used in different problems.

- [ ] [**Breadth First Search**](#bfs)
- [ ] [**Depth First Search**](#dfs)

These searching algorithms are of the **uninformed** search type. This means that the actions these algorithms take will not have any information about current states beyond what is predefined within problem formulation. Another way of saying **uninformed search** is to limit the scope of search within the problem block. If we define that the state will have a value, theses search algorithms will have expectation for the existence of the value at each node, but they WILL NOT know if there is other objects or relationship between objects if any.

Moreover, when finding the solution(s) to a problem, **BFS** gurantees that the solution it finds is **optimal solution**. In the meantime, finding optimal solution is meaningless if there exists one unique solution to a problem.

#### BFS

**Breadth First Search** is an iterative search algorithm that starts at the root node, and expands to its children nodes (successors) at each level. The next expansion depends on whether every successor of the parent node have been explored or not. This algorithm can be implemented along with **Queue**. For details of implementation of queue data tructure, please review `./implementation/queue.py` or click [queue.py](./implementation/queue.ipynb)

```shell
# BFS
# order of expanding visualization

                1
        2       ->       3
    4  ->   5   ->   6  ->   7
    ...
```

#### DFS

**Depth-first Search** is also an interative search algorithm that starts at the root node. This alogrithm unlike **BFS** first expands the first expansion to the deepest level until the node at that point does not expand its child. This algorithm can be implemented along with **Stack**. Notice that although we are using tree form of search, **DFS** implementation on graph-search version will have quite distinguishable features from it.

```shell
# DFS
# order of expanding visualization

                1
        2      <->     5
    3  <->  4      6  <->   7
    ...
```

The problem? with **DFS** I find is that because it first searches expansion by expansion rather than level by level like **BFS**, it is possible that we reach the goal state even if it is NOT OPTIMAL solution. In order for us to find an optimal solution among varying solutions, this algorithm may NOT be optimal for this reason.
