from collections import deque
from utils import makeDescendants, print_puzzle


def search(state, goal):
    stack = deque([(state, 0)])
    # Stacks are used for DFS. The last-in, first-out (LIFO) order is suitable for DFS.
    explored = set()
    total_nodes_generated = 0
    max_stack_size = 1

    while stack:
        current_state, depth = stack.pop()  # pop from the right
        total_nodes_generated += 1
        max_stack_size = max(max_stack_size, len(stack))

        if current_state == goal:
            print_puzzle(current_state)
            print("Goal state found at depth", depth)
            print("Total nodes generated:", total_nodes_generated)
            print("Maximum stack size:", max_stack_size)
            return

        explored.add(tuple(map(tuple, current_state)))

        descendants = makeDescendants(current_state)

        for descendant in descendants:
            descendant_tuple = tuple(map(tuple, descendant))  # Convert lists to tuples
            if descendant_tuple not in explored and descendant not in stack:
                stack.append((descendant, depth + 1))
    print("\nNo result found")
