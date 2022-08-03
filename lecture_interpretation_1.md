# Introducing AI Examples, Terminologies, Iterative Search Process, and First Search Algorithms

**DATE** August 2, 2022 Tuesday

## List of Contents

- [ ] [**Examples**](#examples-of-artificial-intelligence)
- [ ] [**Terminologies**](#Terminologies)
  - [ ] [List of Terminologies](#list-of-terminologies)
  - [ ] [What is State](#what-is-state)
  - [ ] [What is Action](#what-is-action)
  - [ ] [What is Processing](#what-is-processing)
- [ ] [**Iterative Search Proccess**](#iterative-search-process)
  - [ ] [Sudoku Game](#playing-sudoku)
    - [ ] [Sudoku Rules](#rules)
    - [ ] [Sudoku Examples](#examples)
- [ ] [**First Search Algorithms**](#first-search-algorithms)
  - [ ] [Introduction to BFS & DFS](#introduction-to-bfs-and-dfs)
  - [ ] [Visualizations](#bfs--dfs-visualization)
  - [ ] [Differences Between BFS and DFS](#differences-between-bfs-and-dfs)

---

### Examples Of Aritifical Intelligence

When talking about **artificial intelligence**, we know the definite meaning of the term. But it is perhaps too braod for us to accept in our mind. So we can take a look at some of the specific example of real world products where AI is applied.

- Self Driving Cars
- Voice Assistants
- Recommender System (Shppoing & E-Commerce apps)
- Health Care Imaging Technologies (fMRIs, Scanners, ...)
- Google Maps

So we might wonder **what they have in common**. We can think of them as tools (or programs) that performs actions in certain environments and those actions themselves are programs that they have goals to achieve.

Each tool (or program) that we saw from the above example list can be viewed as three-parted objects in computation perspectives, **State**, **Action**, and **Processing**, which I will describe in the [next section](#Terminologies).

### Terminologies

#### List of Terminologies

- [ ] [State](#what-is-state)
- [ ] [Action](#what-is-action)
- [ ] [Processing](#what-is-processing)

##### What is State

We can think of 'state' similar to our 'mood' at a given time of the day or situation. We have a certain moods like 'excited', 'gloomy', 'not motivated', 'motivated' depending on the environment we are currently in.

As such, each program has its own state at a given point of running time. Every program has initial state that is the state at the starting point of the program. It also has the goal for running.

Below is the example of 'state' and 'goal' of a simple python program.

```python
def increment_sum(current_sum: int, increment_value: int) -> int:
    return current_sum + increment_value

# initial state (sum == 1)
sum : int = 0
# first proceeding state (sum == 2)
sum = increment_sum(sum, 1)
# second proceeding state (sum == 3)
sum = increment_sum(sum, 1)
# ...

```

First, the goal of our python program example above is to increment variable `sum` by defining a increment function.

While running this program, we can think of the state of the variable `sum` simply as the value of `sum` at a given the runtime (running code line of the program).

The initial state of the variable `sum` is `0` when it is first declared. Then the next state of `sum` is the value of `sum` is re-assigned by returning value of the function `increment_sum()`. As we can intuitively observe, the state of the variable `sum` in this program changes.

##### What is Action

Now using the example program above, the action is actually the function that returns a value which is assigned to the original `sum` variable. As you see, without this action (function), we cannot process the state change of the variable `sum` thus we CANNOT achieve our goal, which is to increase the variable `sum` value.

We may refer this function that we declared as a **transition** function. This transition functions receives original (previous) state of the variable sum, then it performs the predefined action (which is to increment current state by second parameter value received) to change the state of the variable `sum`.

In the above program, we can visualize two instances of calling `icrement_sum()` transition function, which means that the state of `sum` changed 2 times from the initial state. Both of the transition calls incremented the previous `sum` by 1 where the initial `sum` was 0. This means that before ending the program the state `sum` has value of 2.

When we talk about predefined action, in this case incrementing parameter 1 by value of the paramter 2, we can think of this as a transition process from one state to another.

##### What is Processing

Processing is basically the overall steps of the perspective of the program starting from initial state to the final state (where our goal is achieved)

Take a look at the following example with loop.

```python
def increment(current_state : int, increment_by: int) -> int:
    return current_state + increment_by

def stop(current_state: int, stop_at: int) -> bool:
    return state_value == stop_at

state : int = 0
goal_state: int = 10
while True:
    if stop(state, goal_state):
        break
    state = increment(state, increment_by=1)

print("Reached To The Goal State!")
```

First the goal of the program is to increment the variable `sum` upto 10 starting from its initial state 0. While constructing this program, we may find it useful to define its processes as **incrementing** and **stopping**.

**Incrementing** is part of the process because we initially start `sum` as 0 but want to increase it by 1 each transition until it has incremented to 10.

**Stopping** is also part of the process because we want `sum` to stop incrementing when it is reached to 10 via the incrementing process.

Consturcting the above program in a clenaer & more structural way is the following.

```python
from typing import Callable, Union

# increment process as function
def process_increment(state: int, increment_by: int) -> int:
    return state + increment_by

# stop process as function
def process_stop(state: int, stop_at: int) -> bool:
    return state == stop_at

# transition function declaration (recursive)
def transition_increment(current_state: int, stop_at: int, increment_by: int = 1) -> Union[int, Callable[[int, int, int], int]]:
    # NOTE that commented below in this function are
    # some of the possible bugs which is handled
    # by conditional statements.

    # if stop_at < current_state:
    #     raise ValueError(
    #         "argument 2 must be greater than or equal to argument 1.")
    # if increment_by < 0:
    #     raise ValueError("argument 3 must be greater than or equal to 0.")

    if process_stop(current_state, stop_at):
        return 1

    return transition_increment(process_increment(
        current_state, increment_by), stop_at, increment_by)


if __name__ == "__main__":
    initial_state: int = 0
    goal_state: int = 10

    if transition_increment(initial_state, goal_state) == 1:
        print("Reached To The Goal State!")
    else:
        print("Something went wrong...!")

```

### Iterative Search Process

For the further analysis of states, actions, and processing, I am going to use the game known as **Sudoku**. If you know how to play this game, you can skip the below [Playing Sudoku](#playing-sudoku) section.

#### Playing Sudoku

We are given a (nxn) board with some boxes containg actual value while the rest is empty.

Our goal is to take actions to take the initial state to reach the goal state, meaing that we have to fill in the empty boxes following the rules. The rules will be explained in the next section (you can try to figure it out on your own too.)

```shell
# initial state (4x4) sudoku board
| 1 | 2 | 4 | ~ |
| ~ | ~ | ~ | 1 |
| ~ | 1 | ~ | 4 |
| 4 | 3 | ~ | 2 |

# where sub-boxes are (2x2) from the board
# sum-box-1
| 1 | 2 |   |   |
| ~ | ~ |   |   |
|   |   |   |   |
|   |   |   |   |
# sub-box-2
|   |   | 4 | ~ |
|   |   | ~ | 1 |
|   |   |   |   |
|   |   |   |   |
# sub-box-3
|   |   |   |   |
|   |   |   |   |
| ~ | 1 |   |   |
| 4 | 3 |   |   |
# sub-box-4
|   |   |   |   |
|   |   |   |   |
|   |   | ~ | 4 |
|   |   | ~ | 2 |

# final state (goal state) (4x4) sudoku board
| 1 | 2 | 4 | 3 |
| 3 | 4 | 2 | 1 |
| 2 | 1 | 3 | 4 |
| 4 | 3 | 1 | 2 |
```

##### Rules

In playing sudoku board, we need to keep in mind of the three rules that must all be satisfied simultaneously.

- 1. Fill each column so that this column DOES NOT have repeated number in it.
- 2. Fill each row so that this row DOES NOT have repeated number in it.
- 3. Fill a box so that the (sqrt(n) x sqrt(n)) sub-box it belongs to DOES NOT have a repeated number within it.

##### Examples

```shell
# initial board
| 1 | 2 | 4 | ~ |
| ~ | ~ | ~ | 1 |
| ~ | 1 | ~ | 4 |
| 4 | 3 | ~ | 2 |
# next move : insert 3 at index [2, 1]
# this move is ok since it abided by all three rules.
| 1 | 2 | 4 | ~ |
| ~ | ~ | 3 | 1 |
| ~ | 1 | ~ | 4 |
| 4 | 3 | ~ | 2 |
# next move : insert 2 at index [3, 0]
# this move is NOT OK since it is against rule 1 and rule 2.
| 1 | !2 | 4 | !2 |
| ~ | ~ | 3 | 1 |
| ~ | 1 | ~ | 4 |
| 4 | 3 | ~ | !2 |
# next move swap 2 at index [3, 0] with 3 at index [2, 1]
# this move is perfectly valid since it abides by all three rules
# AND, we know the sub-box-2 has been completed
# so we can now try to fill in other sub-box,
# until all sub-boxes are validly filled.
| 1 | 2 | 4 | 3 |
| ~ | ~ | 2 | 1 |
| ~ | 1 | ~ | 4 |
| 4 | 3 | ~ | 2 |
# after all
# we get the final state (goal state) board.
| 1 | 2 | 4 | 3 |
| 3 | 4 | 2 | 1 |
| 2 | 1 | 3 | 4 |
| 4 | 3 | 1 | 2 |
```

As we saw, the way we proceed playing this game is a **step-by-step** proccess iteratively. We may not have been aware of the specific type of algorithm ran by our head when playing the game, but we know for sure that it was both **step-by-step** using iterative processes.

### First Search Algorithms

There are two common **Iterative Search** type of algorithms that we explored, **Breadth First Search (BFS)** and **Depth First Search (DFS)**. They may seem similar but keep in mind that you and me looking similar does not imply that we have similar intentions for our actions. These algorithms also differ in its intentions and are used in different problems.

#### Introduction to BFS and DFS

They are both first search algorithms used to find reach from initial state to goal state. They both use iterative apporach to find solution to the problems.

Some of the differences between **BFS** and **DFS** will be discussed with some examples below.

#### BFS & DFS Visualization

Imagine a tree looking structure with a value in each node. We know that a tree structure has traits of the following.

- 1. There is a root node which is the top level node that DOES NOT have parant node. (You can think of root node as the oldest person in your family root)
- 2. Each node has children unless it is **leaf node** maning it is at the bottom level of the tree. (You can think of leaf node as the youngest generation of the family root)

**BFS** & **DFS** can be visualized in a tree structure where at each level, each node expands to another either at the same branch (level) or child node depending on whether we use **BFS** or **DFS** strategies.

```shell
# Each node value in the tree represents the order of exploration

# BFS order of exploration
            1       ------ root: level 0
         2     3    ------ branch: level 1
       4   5 6   7  ------ branch: level 2
     8   @   ...    ------ leaf: level 3
     destination (@) will be explored at last

# DFS order of exploration
            1       ------ root: level 0
         2     7    ------ branch: level 1
       3   6 8   9  ------ branch: level 2
     4   @   ...    ------ leaf: level 3
     destination (@) will be explored at 5th search
```

#### Differences Between BFS and DFS

1. **Order of Iteration**
   For **BFS**, starting from the root node, every children node is explored before moving on the next branch, while for **DFS**, every child nodes is explored until hitting leaf child then explores upward to find the next child node to explore.

2. **Time & Space Complexity Analysis**
   Let's first explore what we want to tell the world about our algorithms and why or how it should be used. Because these algorithms are being used in computer machines, we need to tell the computer to allocate memory spaces along with expecting it to do the number of computations on a givne program. This means that given one algorithm we developer, the only ways we can confirm the algorithm is efficient, _in computational aspects_ for the given computational task are

   - **1. Predicting How Many Computations The Program Will Require For The Algorithm** (Time Complexity)

   - **2. Predicting How Much of Memory Space In Our Computer Will Need To Be Allocated For This Program** (Space Complexity)

   Now, before we write down the time/space complexity, we first need to know what a branching factor _`b`_ of a tree is. Please visit [here](https://en.wikipedia.org/wiki/Branching_factor#:~:text=The%20branching%20factor%20can%20be,number%20of%20nodes%20with%20children) to learn about calculating branching factor of a givne tree.

   | Analysis | **BFS**      | **DFS**      |
   | -------- | ------------ | ------------ |
   | Time     | `O(b^depth)` | `O(b^depth)` |
   | Space    | `O(b&depth)` | `O(d)`       |

3. **Other Differences**
   There are many other differences which we can explore [here](https://www.geeksforgeeks.org/difference-between-bfs-and-dfs/)
