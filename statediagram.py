def get_next_state(rule, current, left, right):
  """
  Calculates the next state based on the rule and neighborhood.

  Args:
      rule (int): The ECA rule number.
      current (int): Current state of the cell (0 or 1).
      left (int): State of the left neighbor (periodic boundary).
      right (int): State of the right neighbor (periodic boundary).

  Returns:
      int: The next state of the cell.
  """
  # Convert neighborhood and current state to a binary string
  neighborhood = str(left) + str(current) + str(right)

  # Convert binary string to integer for rule lookup
  index = int(neighborhood, 2)

  # Apply the rule to get the next state
  next_state = (rule >> index) & 1
  return next_state

def evolve(rule, n, initial_config):
  """
  Evolves the ECA for a given number of generations.

  Args:
      rule (int): The ECA rule number.
      n (int): The lattice size (number of cells).
      initial_config (list): The initial configuration of the lattice (0s and 1s).

  Returns:
      list: A list of lists, where each sublist represents a generation.
  """
  generations = []
  generations.append(initial_config)
  for _ in range(1,5):  # Adjust 'generations_to_simulate' for desired number of steps
    next_gen = []
    for i in range(n):
      left_neighbor = generations[-1][(i - 1) % n]  # Periodic boundary for left neighbor
      right_neighbor = generations[-1][(i + 1) % n]  # Periodic boundary for right neighbor
      next_state = get_next_state(rule, generations[-1][i], left_neighbor, right_neighbor)
      next_gen.append(next_state)
    generations.append(next_gen)
  return generations

# Get user input
rule = int(input("Enter ECA rule number (0-255): "))
n = int(input("Enter lattice size: "))
initial_config = [int(x) for x in input("Enter initial configuration (0s and 1s): ").split()]

# Simulate and print transitions
generations = evolve(rule, n, initial_config)
for i, generation in enumerate(generations):
  print(f"Generation {i}: {generation}")
