class MissionariesAndCannibals:
    def __init__(self):
        # Initial state: (m_left, c_left, m_right, c_right, boat_position)
        self.initial_state = (3, 3, 0, 0, 0)
        self.goal_state = (0, 0, 3, 3, 1)
        self.actions = [(1, 0), (0, 1), (1, 1), (2, 0),
                        (0, 2)]  # Possible actions: (m, c)

    def is_valid_state(self, state):
        """Check if a state is valid and doesn't violate the problem constraints."""
        m_left, c_left, m_right, c_right, _ = state

        # Ensure no bank has more cannibals than missionaries unless no missionaries are on that bank.
        if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
            return False
        return True

    def get_successor_states(self, state):
        """Generate all possible successor states from the current state."""
        successors = []
        m_left, c_left, m_right, c_right, boat_position = state

        for action in self.actions:
            m_move, c_move = action

            if boat_position == 0:  # Boat is on the left bank
                new_state = (
                    m_left - m_move,
                    c_left - c_move,
                    m_right + m_move,
                    c_right + c_move,
                    1  # Move boat to the right bank
                )
            else:  # Boat is on the right bank
                new_state = (
                    m_left + m_move,
                    c_left + c_move,
                    m_right - m_move,
                    c_right - c_move,
                    0  # Move boat to the left bank
                )

            # Ensure the new state is within bounds and valid
            if (
                new_state[0] >= 0 and new_state[1] >= 0 and
                new_state[2] >= 0 and new_state[3] >= 0 and
                self.is_valid_state(new_state)
            ):
                successors.append((new_state, action))

        return successors

    def is_goal_state(self, state):
        """Check if the current state is the goal state."""
        return state == self.goal_state

    def print_path(self, path):
        """Print the entire path of moves from the initial state to the goal state."""
        for i, (state, action) in enumerate(path):
            if action is not None:
                print(f"Step {i}:")
                self.print_state(state, action)
            else:
                print("Initial state:")
                self.print_state(state, (0, 0))

    def print_state(self, state, action):
        """Print the current state and the action taken."""
        bank = ""
        m_left, c_left, m_right, c_right, boat_position = state
        m_move, c_move = action

        print(f"Move: {m_move} missionary(ies) and {c_move} cannibal(s)")
        print(f"Left bank: {m_left} missionaries, {c_left} cannibals")
        print(f"Right bank: {m_right} missionaries, {c_right} cannibals")
        if boat_position == 1:
            bank = 'right'
        else:
            bank = 'left'
        print(f"Boat is on the {bank} bank\n")
        #   'right' if boat_position == 1 else 'left'} bank\n") --> causes "f" error after save

    def solve(self):
        """Solve the problem using breadth-first search and trace the path."""
        from collections import deque

        # (path of (state, action), action that led to last state)
        frontier = deque([([(self.initial_state, None)], None)])
        explored = set()

        while frontier:
            path, action = frontier.popleft()
            current_state, _ = path[-1]

            if self.is_goal_state(current_state):
                print("Goal state reached. Here's the path:")
                self.print_path(path)
                return

            explored.add(current_state)

            for successor, action in self.get_successor_states(current_state):
                if successor not in explored and successor[4] != current_state[4]:
                    new_path = path + [(successor, action)]
                    frontier.append((new_path, action))

        print("No solution found")


# Example of running the code
if __name__ == "__main__":
    problem = MissionariesAndCannibals()
    problem.solve()
