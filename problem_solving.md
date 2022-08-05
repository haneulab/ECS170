# Problem Solving

In this module, we will be exploring the ways to approach a problem and some strategies to solve it.

## Problems & Solutions, & How To Get There

### List of Content

- [ ] [**Atomic Representation Of A Problem**](#atomic-representation-of-a-problem)
- [ ] [**Problem Solving Processes**](#problem-solving-processes)
- [ ] [**Example Problems Solving**](#example-problem-solving)
- [ ] [**Moving Forward With Problem Solving**](#moving-forward-with-problem-solving)

Before we learn to solve a problem, we must see and understand problem, respectively.

Consider the following board.

```shell
# initial state of board

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | ? |
```

This board, as we can see, is a 3 x 3 square board (meaning that the # of columns and rows are equal). Although we can kind of predict what the problem is and how it should be solved (problem: missing 9 at the index [2,2], solution: replace '?' with 9), let's break this problem down into atomic forms.

### Atomic Representation Of A Problem

I am going to borrow the problem we encountered right above, and unfold it atomically.

```shell
# initial state of board

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | ? |
```

**1. Problem** : Missing numeric value of 9 at index [2,2] (or [3,3] depending on how to set the initial index value)
**2. Goal** : Make the board so that it is 3 x 3 square board & all fields are filled with a single numeric value that corresponds to a value incremented by 1 from the previous index.

```shell
# goal state of board

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
```

Here, we need to note that once we find out what the problem is, we directly try to access (or formulate) the goal state of the board. We can refer this process as **goal formulation** where once we know the problem, we then set our goal **depending on the current situation**.

### Problem Solving Processes

In the above example, we considered formulation of **goal** based on the problem we are given. We even know the solution to this problem.

**But**, we have not yet disucssed **how to solve it**. This problem above is very simple. In fact to our eyes, we can almost immediately describe the solution in one or two sentences.

In practical problem solving, however, that is not the case. We need to **break down processes** themselves in order to construct the problem more structurally. This is known as **problme formulation**.

Every problem that we encounter will need to consider the actions & change of states along with how it will transition from one state to another until it reaches the goal state (our goal).

### Example Problem Solving

In this section, I am going to describe the problem we encounter. I am going to use the concept from linear algebra called, **A transpose of a matrix M**.

> **NOTE** that transposing a square matrix is just swaping the row vector and column vector position corresponding to its position relative to the matrix. For example, for a given square matrix A, Transpose(A) should return a square matrix whose row vectors are the column vectors of A, and whose column vectors are the row vectors of A.

```python
A = [
    [1,-1],
    [2,-2]
]
T(A) = [
    [1, 2],
    [-1,-2]
]
```

#### Problem Description

Suppose that we are given a 3 x 3 square matrix `M` represented as below.

```python
# matrix M
M : SquareMatrix = [
    [1, 1, 1]
    [2, 2, 2]
    [3, 3, 3]
]

# Intrepretation of the matrix M
# M.size = (3, 3)
# M.dimension = 3
# M.isSquare = True
```

From our direct intuition assuming that we know what the transposing matrix means, we can draw the solution.

```python
M_transpose : SquareMatrix = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]
```

**But**, we now need to define its processes including states and actions. We know that the states will be referred as the representation of the board at a given time while transposing. Also, one obvious action we need to take is to transpose the matrix. We so may define state variable `M_state` for storing current state, and a function that will transition from initial state to the goal state.

```python
M_state : SquareMatrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

def transition(current_state : SquareMatrix) -> SuqareMatrix:
    ...
```

Inside our `transition` function we can define the actions & the goal state and check for every action we take will result in matching the board at current state with the board at goal state. This will be repeated until they (goal state and current state) match, so we can define our transition function as a recursive function.

```python
M_state : SquareMatrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

def transition(current_state : SquareMatrix, action_function: Callable[[SquareMatrix], SquareMatrix]) -> SuqareMatrix:
    goal : SquareMatrix = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]

    current_state = action_function(current_state)
    if current_state == goal:
        return current_state

    return transition(current_state)
```

Now the question will be 'how do we define our action?'. Well, there is not a single way to define our action. There are a lot of ways to define our action. Below is one way to transpose. First to unpack the matrix in a single-dimensional list, then constructign the row vectors based on the length of the state by jumping indices.

```python
def action_swap_row_col(state : SquareMatrix) -> SquareMatrix:
    unpack = [item[index] for index in range(len(state)) for item in state]

    new_state = []
    index_jump = 0
    while True:
        row = []
        for i in range(len(state)):
            row.append(unpack[index_jump + i])

        new_state.append(row)
        if len(new_state) == len(state):
            break
        index_jump += len(state)

    return new_state
```

Now we can combine our action definition with the rest of the transition function and the state as following to complete a problem solving program `transpose_matrix.py`. You can view this file in `/programs` directory or by clicking [here](./programs/transpose_matrix.py).

```python
def action_swap_row_col(state : SquareMatrix) -> SquareMatrix:
    unpack = [item[index] for index in range(len(state)) for item in state]

    new_state = []
    index_jump = 0
    while True:
        row = []
        for i in range(len(state)):
            row.append(unpack[index_jump + i])

        new_state.append(row)
        if len(new_state) == len(state):
            break
        index_jump += len(state)

    return new_state

def transition(current_state : SquareMatrix, action_function : Callable[[SquareMatrix], SquareMatrix]) -> SuqareMatrix:
    goal : SquareMatrix = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]

    current_state = action_function(current_state)
    if current_state == goal:
        return current_state

    return transition(current_state)

M_state : SquareMatrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

M_goal_state : SquareMatrix = transition(M_state, action_swap_row_col)

print('Initial State : ', M_state)
# [
#   [1, 1, 1]
#   [2, 2, 2]
#   [3, 3, 3]
# ]

print('Goal State : ', M_goal_state)
# [
#   [1, 2, 3]
#   [1, 2, 3]
#   [1, 2, 3]
# ]
```

### Moving Forward With Problem Solving

Once we observe the way we formulate our problem above, we may notice that our states change directly from `initial_state` to `goal_state`. To see this, we can visit our `transpose_matrix.py` where our `action_function` is defined. What we define as `new_state` will transform to the goal state once this function is called in the program.

The way we construct our action function has `no restriction` in it. However, this method is not very good because **it DOES NOT** provide any information about the paths we took to get from state A to state B. With this in mind, I will explore the [Searching Strategies](./searching_strategies.md) in `searching_strategies.md` module. We will see the impack of iteratively searching methods along with some of the most popular algorithms.
