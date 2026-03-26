from agno.agent import Agent
from agno.tools.hackernews import HackerNewsTools


def funcao_agente_hackernews():
    agente = Agent(
        name='Agente Hacker News',
        role='Fique por dentro das últimas noticias de tecnologia do HackerNews.',
        tools=[HackerNewsTools()],
        instructions='Busque no HackerNews a quantidade de últimas noticias passadas pelo usuário, retorne: Titulo, Resumo, Link, Autor, Data'
    )
    
    return agente