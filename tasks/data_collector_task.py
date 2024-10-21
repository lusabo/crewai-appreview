from crewai import Task
from agents.data_collector import DataCollectorAgent

class DataCollectorTask(Task):
    def __init__(self):
        super().__init__(
            description="Retrieve all reviews for our app from the last month",
            agent=DataCollectorAgent()
        )