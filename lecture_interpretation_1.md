# Introducing Terminologies, Concepts, and Examples Of AI

**DATE** August 2, 2022 Tuesday

## List of Contents

- [ ] [**Examples**](#examples-of-artificial-intelligence)
- [ ] [**Terminologies**](#Terminologies)

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
def increment(state_value : int) -> int:
    return state_value + 1

def stop(state_value: int, stop_point_value: int) -> bool:
    return state_value == stop_point_value

sum : int = 0
stop_at: int = 10
while True:
    sum = increment(sum)
    if stop(sum, stop_at):
        break
```

First the goal of the program is to increment the variable `sum` upto 10 starting from its initial state 0. While constructing this program, we may find it useful to define its processes as **incrementing** and **stopping**.

**Incrementing** is part of the process because we initially start `sum` as 0 but want to increase it by 1 each transition until it has incremented to 10.

**Stopping** is also part of the process because we want `sum` to stop incrementing when it is reached to 10 via the incrementing process.

Better version of the above program

```python
# increment process action
def process_increment(state: int) -> int:
    return state + 1
# stop process action
def process_stop(state: int, stop_at: int) -> bool:
    return state == stop_at

# recursive transiton function
def transition(current_state: int, stop_at: int = 10) -> None:
    return current_state if process_stop(current_state, stop_at) else transition(process_increment(current_state))

sum: int = 0 # initial_state 0
sum: int = transition(sum) # goal_state 10

```
