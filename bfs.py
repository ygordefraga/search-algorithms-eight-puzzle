from collections import deque
from utils import makeDescendants, print_puzzle


def search(state, goal):
    queue = deque([(state, 0)])
    # Deques are useful when you need fast access to elements at both ends of the sequence.
    explored = set()
    total_nodes_generated = 0
    max_queue_size = 1

    while queue:
        current_state, depth = queue.popleft()
        total_nodes_generated += 1
        max_queue_size = max(max_queue_size, len(queue))

        if current_state == goal:
            print_puzzle(current_state)
            print("Goal state found at depth", depth)
            print("Total nodes generated:", total_nodes_generated)
            print("Maximum queue size:", max_queue_size)
            return

        explored.add(tuple(map(tuple, current_state)))

        descendants = makeDescendants(current_state)

        for descendant in descendants:
            descendant_tuple = tuple(map(tuple, descendant))  # Convert lists to tuples
            if descendant_tuple not in explored and descendant not in queue:
                queue.append((descendant, depth + 1))
    print("\nNo result found")
