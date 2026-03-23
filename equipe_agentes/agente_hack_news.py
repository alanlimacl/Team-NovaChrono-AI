from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools


def agente_hnew():
    agente = Agent(
        name='Agente Hacker News',
        role='Fique por dentro das últimas noticias de tecnologia do HackerNews.',
        tools=[HackerNewsTools()]
    )
    
    return agente