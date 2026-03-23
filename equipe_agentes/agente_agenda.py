import os
from datetime import datetime
from agno.agent import Agent
from agno.tools.google.calendar import GoogleCalendarTools


DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)
CAMINHO_CREDENCIAIS = os.path.join(DIRETORIO_RAIZ, 'credentials.json')
CAMINHO_TOKEN = os.path.join(DIRETORIO_RAIZ, 'token.json')

ferramenta_agenda = GoogleCalendarTools(credentials_path=CAMINHO_CREDENCIAIS, token_path=CAMINHO_TOKEN)

def agente_agnd():
    agora = datetime.now()
    data_completa = agora.strftime("%d/%m/%Y às %H:%M:%S")
    ano_atual = agora.year
    
    agente = Agent(
        name='Agente Agenda',
        role='Você é um assistente pessoal produtivo especializado em gestão de tempo e agendas.',
        tools=[ferramenta_agenda],
        instructions=[
            f"CONTEXTO TEMPORAL CRÍTICO: Hoje é exatamente {data_completa}. O ano atual é {ano_atual}.",
            f"REGRAS DE AGENDAMENTO ABSOLUTAS:",
            f"1. É ESTRITAMENTE PROIBIDO criar eventos no ano de 2024 ou em qualquer ano no passado.",
            f"2. Todos os eventos solicitados como 'amanhã', 'hoje' ou 'próxima semana' têm de usar obrigatoriamente o ano de {ano_atual}.",
            "3. NUNCA diga que agendou algo sem antes executar a ferramenta `quick_add_event` ou `create_event` do Google Calendar.",
            "4. Aguarde a confirmação de sucesso da ferramenta antes de responder ao utilizador."
            ],     
        read_tool_call_history = True 
    )
    return agente