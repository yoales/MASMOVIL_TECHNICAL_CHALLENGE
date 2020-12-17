from airflow.models.baseoperator import BaseOperator
from datetime import datetime

class TimeDiff(BaseOperator):

    def __init__(
            self,
            diff_date: str,
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.diff_date = diff_date

    def days_between(self, current_date):
        d1 = datetime.strptime(self.diff_date, '%Y-%m-%d')
        return abs((current_date - d1).days)

    def execute(self, context):
        current_date = datetime.now()
        num_days = self.days_between(current_date)
        message = f"Number of days between {self.diff_date} and {current_date.strftime('%Y-%m-%d')} is {num_days}"
        print(message)
        return message
