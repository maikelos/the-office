from collections import defaultdict
from typing import Set

from employee import Employee


class TheOffice:

    def __init__(self, regional_manager: str, employees: Set[Employee], location: str):
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        self.regional_manager = regional_manager
        self.employees = employees
        self.location = location
        self.sales = defaultdict(int)

    def __str__(self) -> str:
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        return f"Welcome to The Office! The boss here is {self.regional_manager}."

    def record_sale(self, employee: Employee) -> None:
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """

        self.sales[employee] += 1

    def get_employee_sales(self, employee: Employee) -> int:
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        return self.sales[employee]

    def _fire_employee(self, employee: Employee) -> None:
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        self.employees.remove(employee)
