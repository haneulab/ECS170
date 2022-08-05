from typing import List, Callable, Any

SquareMatrix = List[List[Any]]
ActionFunctionType = Callable[[SquareMatrix], SquareMatrix]


def action_swap_row_col(state: SquareMatrix) -> SquareMatrix:
    """
    @param: state: SquareMatrix => list[list[any]]
    @returns: SquareMatrix => list[list[any]]
    """
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


def transition(current_state: SquareMatrix, action_function: ActionFunctionType) -> SquareMatrix:
    """
    @param: state: SquareMatrix => list[list[any]]
    @param: action_function: ActionFunctionType => (list[list[any]]) => list[list[any]]
    @returns: SquareMatrix => list[list[any]] | self (recursive)
    """
    goal: SquareMatrix = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]

    current_state = action_function(current_state)
    print(current_state)
    if current_state == goal:
        return current_state

    return transition(current_state, action_function)


M_state: SquareMatrix = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

M_goal_state: SquareMatrix = transition(M_state, action_swap_row_col)
