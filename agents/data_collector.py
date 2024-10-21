from crewai import Agent

class DataCollectorAgent(Agent):
    def __init__(self):
        super().__init__(
            role="Database specialist",
            goal="Retrieve review data from the database using SQL",
            backstory='''
            As an database administrator, you are specialist in extracting information from various database systems. 
            Your expertise lies in crafting efficient queries and presenting data in a structured format for further analysis.
            '''
        )