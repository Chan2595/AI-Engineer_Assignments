import numpy as np

# a) Three tester classes
class ManualTester:
    def analyze(self, data):
        print("ManualTester → First 5 test execution times:", data[:5])


class AutomationTester:
    def analyze(self, data):
        print("AutomationTester → Fastest test case:", np.min(data))


class PerformanceTester:
    def analyze(self, data):
        print("PerformanceTester → 95th percentile execution time:", np.percentile(data, 95))


# c) Function to demonstrate polymorphism
def show_analysis(tester, data):
    tester.analyze(data)


# d) Main section
if __name__ == "__main__":
    # Create a NumPy array with at least 12 execution times
    execution_times = np.array([12, 8, 25, 30, 15, 5, 40, 20, 18, 35, 50, 28])

    # Create tester objects
    manual = ManualTester()
    automation = AutomationTester()
    performance = PerformanceTester()

    # Call show_analysis for each tester
    testers = [manual, automation, performance]

    for tester in testers:
        show_analysis(tester, execution_times)