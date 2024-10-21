from crewai import Task
from agents.review_analyst import ReviewAnalystAgent

class ReviewAnalystTask(Task):
    def __init__(self):
        super().__init__(
            description="Analyze the collected reviews and provide a detailed report",
            agent=ReviewAnalystAgent()
        )