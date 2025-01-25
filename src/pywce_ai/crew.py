from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DirectoryReadTool, \
    FileReadTool

directory_read_tool = DirectoryReadTool(directory='./knowledge')
file_read_tool = FileReadTool()


@CrewBase
class PywceAi:
    """PywceAi crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def conversation_flow_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['conversation_flow_designer'],
            verbose=True,
            tools=[directory_read_tool, file_read_tool]
        )

    @agent
    def hook_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['hook_developer'],
            verbose=True,
            tools=[directory_read_tool, file_read_tool]
        )

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['code_reviewer'],
            verbose=True,
            tools=[directory_read_tool, file_read_tool]
        )

    @agent
    def code_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config['code_reporter'],
            verbose=True,
            tools=[directory_read_tool, file_read_tool]
        )

    @task
    def conversation_flow_designing_task(self) -> Task:
        return Task(
            config=self.tasks_config['conversation_flow_designing_task'],
        )

    @task
    def developer_task(self) -> Task:
        return Task(
            config=self.tasks_config['developer_task']
        )

    @task
    def reviewer_task(self) -> Task:
        return Task(
            config=self.tasks_config['reviewer_task']
        )

    @task
    def reporter_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporter_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PywceAi crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
