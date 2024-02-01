from copy import deepcopy


def print_puzzle(state):
    for row in state:
        print(row)
    print("\n")


def find_position(goal, value):
    for i in range(3):
        for j in range(3):
            if goal[i][j] == value:
                return i, j


def heuristic_manhattan(state, goal):
    """Heuristic: Distância de Manhattan para o Eight Puzzle."""

    # Fornece uma estimativa mais informada, considerando a distância real entre as peças e suas posições corretas.
    total_distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0 and value != goal[i][j]:
                _i, _j = find_position(goal, value)
                total_distance += abs(i - _i) + abs(j - _j)
    return total_distance


def find_empty_element(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def makeDescendants(state):
    descendants = []
    empty_row, empty_col = find_empty_element(
        state
    )  # used to find the row and column of the element '0'

    # Move up
    if empty_row > 0:
        new_state = deepcopy(state)
        new_state[empty_row][empty_col], new_state[empty_row - 1][empty_col] = (
            new_state[empty_row - 1][empty_col],
            new_state[empty_row][empty_col],  # 0 is here
        )
        descendants.append(new_state)

    # Move down
    if empty_row < 2:
        new_state = deepcopy(state)
        new_state[empty_row][empty_col], new_state[empty_row + 1][empty_col] = (
            new_state[empty_row + 1][empty_col],
            new_state[empty_row][empty_col],  # 0 is here
        )
        descendants.append(new_state)

    # Move left
    if empty_col > 0:
        new_state = deepcopy(state)
        new_state[empty_row][empty_col], new_state[empty_row][empty_col - 1] = (
            new_state[empty_row][empty_col - 1],
            new_state[empty_row][empty_col],  # 0 is here
        )
        descendants.append(new_state)

    # Move right
    if empty_col < 2:
        new_state = deepcopy(state)
        new_state[empty_row][empty_col], new_state[empty_row][empty_col + 1] = (
            new_state[empty_row][empty_col + 1],
            new_state[empty_row][empty_col],  # 0 is here
        )
        descendants.append(new_state)

    return descendants
