from crewai import Task
from agents.report_creator import ReportCreatorAgent

class ReportCreatorTask(Task):
    def __init__(self):
        super().__init__(
            description="Generate a comprehensive report based on the analysis results",
            agent=ReportCreatorAgent()
        )