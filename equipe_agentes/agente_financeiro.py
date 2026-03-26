from agno.agent import Agent
from ferramentas.adicionar_gasto import adicionar
from ferramentas.consultar_gasto import consultar
from datetime import datetime, timedelta, timezone


def funcao_agente_fianceiro():
    fuso = timezone(timedelta(hours=-3))
    agora = datetime.now(fuso)
    data_atual = agora.strftime("%Y-%m-%d")
    
    agente = Agent(
        name='Agente Fianceiro',
        role='Seja responsável pela fincanças do usuário e controle.',
        tools=[adicionar, consultar],
        instructions=[
            f"CONTEXTO TEMPORAL: Hoje é {data_atual}. Use essa data como base para calcular todos os períodos.",
            "Quando for usar a ferramenta de consulta de período e o usuário pedir 'hoje', envie a data de hoje tanto no início quanto no fim.",
        ])
    
    return agente