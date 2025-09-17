# a) Base class Employee
class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    # b) Method to display employee details
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Department: {self.department}")


# c) Subclass Manager
class Manager(Employee):
    def __init__(self, name, emp_id, department, team_size):
        # Call parent constructor
        super().__init__(name, emp_id, department)
        self.team_size = team_size

    # Override display_info
    def display_info(self):
        super().display_info()
        print(f"Team Size: {self.team_size}")


# d) Subclass Developer
class Developer(Employee):
    def __init__(self, name, emp_id, department, programming_language):
        # Call parent constructor
        super().__init__(name, emp_id, department)
        self.programming_language = programming_language

    # Override display_info
    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# e) Main section
if __name__ == "__main__":
    # Create Manager object
    mgr = Manager("Alice Johnson", "M101", "IT Operations", 8)

    # Create Developer object
    dev = Developer("Bob Smith", "D205", "Software Development", "Python")

    # Display info
    print("=== Manager Details ===")
    mgr.display_info()
    print("\n=== Developer Details ===")
    dev.display_info()
