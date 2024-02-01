import bfs
import dfs
import iterative_dfs
import greedy_search
import a_star
import time


def choose_algorithm():
    print("\nSelect an algorithm:")
    print("1. Breadth-First Search (BFS)")
    print("2. Depth-First Search (DFS)")
    print("3. Iterative Depth-First Search (IDFS)")
    print("4. Greedy Search")
    print("5. A*")
    choice = input("\nEnter the number corresponding to your choice: ")
    return choice


def choose_initial_state():
    predefined_states = {
        "1": [[3, 4, 2], [5, 1, 7], [6, 0, 8]],
        "2": [[6, 2, 7], [5, 0, 3], [8, 1, 4]],
    }

    print("\nSelect initial state:")
    for key, value in predefined_states.items():
        print(f"{key}. {value}")

    print("3. Custom Input")
    choice = input("\nEnter the number corresponding to your choice: ")

    if choice == "3":
        state = [
            [
                int(x)
                for x in input(
                    f"\nRow {i + 1} (Space to separate the columns): "
                ).split()
            ]
            for i in range(3)
        ]
        if len(state) != 3 or any(len(row) != 3 for row in state):
            raise ValueError("Custom input must be a 3x3 matrix.")
    else:
        state = predefined_states.get(choice, None)

    if state is None:
        raise ValueError("Invalid choice. State not found.")

    print(f"\n{state}\n")

    return state


def main():
    goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    algorithm_choice = choose_algorithm()
    initial_state = choose_initial_state()

    start_time = time.time()

    if algorithm_choice == "1":
        bfs.search(initial_state, goal_state)
    elif algorithm_choice == "2":
        dfs.search(initial_state, goal_state)
    elif algorithm_choice == "3":
        depth = input("\nEnter the depth limit (press Enter for default 50): ")
        iterative_dfs.search(initial_state, goal_state, int(depth) if depth else 50)
    elif algorithm_choice == "4":
        greedy_search.search(initial_state, goal_state)
    elif algorithm_choice == "5":
        a_star.search(initial_state, goal_state)
    else:
        print("Invalid choice. Please enter 1 , 2, 3 or 4.")

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
