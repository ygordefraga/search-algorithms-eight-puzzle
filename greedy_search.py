from collections import deque
from utils import makeDescendants, print_puzzle, heuristic_manhattan


def search(initial_state, goal_state):
    queue = deque([(initial_state, 0, heuristic_manhattan(initial_state, goal_state))])
    explored = set()
    total_nodes_generated = 0
    max_queue_size = 1

    while queue:
        current_state, depth, _ = queue.popleft()
        total_nodes_generated += 1
        max_queue_size = max(max_queue_size, len(queue))

        if current_state == goal_state:
            print_puzzle(current_state)
            print("Goal state found at depth", depth)
            print("Total nodes generated:", total_nodes_generated)
            print("Maximum queue size:", max_queue_size)
            return

        explored.add(tuple(map(tuple, current_state)))
        descendants = makeDescendants(current_state)

        for descendant in descendants:
            descendant_tuple = tuple(map(tuple, descendant))
            if descendant_tuple not in explored and descendant not in queue:
                queue.append(
                    (descendant, depth + 1, heuristic_manhattan(descendant, goal_state))
                )

        # Ordena a fila com base na heurística de Distância de Manhattan
        queue = deque(sorted(queue, key=lambda x: x[2]))

    print("\nNo result found")
