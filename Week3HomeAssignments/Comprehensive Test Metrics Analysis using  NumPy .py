import numpy as np

# a) Generate synthetic data (5 cycles × 50 tests)
np.random.seed(42)  # for reproducibility
data = np.random.randint(5, 51, size=(5, 50))
print("Execution Times (5x50):\n", data, "\n")


# b1) Statistical Analysis
print("=== Statistical Analysis ===")
avg_per_cycle = np.mean(data, axis=1)
print("Average execution time per cycle:", avg_per_cycle)

max_test = np.max(data)
max_index = np.unravel_index(np.argmax(data), data.shape)
print(f"Max execution time: {max_test} (Cycle {max_index[0]+1}, Test {max_index[1]+1})")

std_per_cycle = np.std(data, axis=1)
print("Standard deviation per cycle:", std_per_cycle, "\n")


# b2) Slicing Operations
print("=== Slicing Operations ===")
print("First 10 tests from Cycle 1:", data[0, :10])
print("Last 5 tests from Cycle 5:", data[4, -5:])
print("Every alternate test from Cycle 3:", data[2, ::2], "\n")


# b3) Arithmetic Operations
print("=== Arithmetic Operations ===")
print("Cycle1 + Cycle2:\n", data[0] + data[1])
print("Cycle1 - Cycle2:\n", data[0] - data[1])
print("Cycle4 * Cycle5:\n", data[3] * data[4])
print("Cycle4 / Cycle5:\n", data[3] / data[4], "\n")


# b4) Power Functions
print("=== Power Functions ===")
print("Square:\n", np.power(data, 2))
print("Cube:\n", np.power(data, 3))
print("Square Root:\n", np.sqrt(data))
print("Log Transform:\n", np.log(data + 1), "\n")


# b5) Copy Operations
print("=== Copy Operations ===")
shallow_copy = data.view()
shallow_copy[0, 0] = 999
print("Original after shallow copy change:", data[0, 0])  # Will reflect change

deep_copy = data.copy()
deep_copy[0, 1] = 888
print("Original after deep copy change:", data[0, 1])  # Will remain unchanged
print()


# b6) Filtering with Conditions
print("=== Filtering with Conditions ===")
print("Cycle 2 tests > 30:", data[1][data[1] > 30])

# Tests that consistently take >25 across ALL cycles
consistent_tests = np.all(data > 25, axis=0)
print("Tests consistently >25:", data[:, consistent_tests])

# Replace all execution times < 10 with 10
thresholded_data = data.copy()
thresholded_data[thresholded_data < 10] = 10
print("Thresholded dataset:\n", thresholded_data)
