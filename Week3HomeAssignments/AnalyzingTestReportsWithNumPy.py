import numpy as np

# a) Base class
class TestReport:
    def __init__(self, execution_times):
        self.execution_times = execution_times

    # b1) Method to calculate average time
    def average_time(self):
        return np.mean(self.execution_times)

    # b2) Method to calculate maximum time
    def max_time(self):
        return np.max(self.execution_times)


# c) Subclass inheriting from TestReport
class RegressionReport(TestReport):
    def __init__(self, execution_times):
        # Pass execution_times to the parent class
        super().__init__(execution_times)

    # Method to return slow tests above a threshold
    def slow_tests(self, threshold):
        return self.execution_times[self.execution_times > threshold]


# d) Main section
if __name__ == "__main__":
    # Create a NumPy array with 10 execution times
    times = np.array([12, 18, 25, 30, 5, 45, 22, 10, 50, 8])

    # Create RegressionReport object
    report = RegressionReport(times)

    # Display results
    print("Average execution time:", report.average_time())
    print("Maximum execution time:", report.max_time())
    print("Slow tests (threshold = 20):", report.slow_tests(20))
