import uuid

JOB_TITLES = ["SALES_REP", "REGIONAL_MANAGER", "MANAGER", "HR", "ACCOUNTING"]


class Employee:
    def __init__(self, name: str, job_title: str):
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        self.name = name
        self.job_title = job_title
        self.employee_id = uuid.uuid4()

    def update_contact_info(self, name: str) -> str:
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        past_name = self.name
        self.name = name
        return past_name

    def promote_employee(self, job_title):
        """Method that returns the number of sales given an employee.

        Args:
            employee (Employee): The employee whose sales number we are interested in.

        Returns:
            int: The total number of sales the employee has made.
        """
        if job_title not in JOB_TITLES:
            raise ValueError(
                f"Invalid job title {job_title}, expected one of {JOB_TITLES}"
            )
        self.job_title = job_title
