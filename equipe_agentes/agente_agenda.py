import os
from datetime import datetime, timezone, timedelta
from agno.agent import Agent
from agno.tools.google.calendar import GoogleCalendarTools


DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
DIRETORIO_RAIZ = os.path.dirname(DIRETORIO_ATUAL)
CAMINHO_CREDENCIAIS = os.path.join(DIRETORIO_RAIZ, 'credentials.json')
CAMINHO_TOKEN = os.path.join(DIRETORIO_RAIZ, 'token_agenda.json')

ferramenta_agenda = GoogleCalendarTools(credentials_path=CAMINHO_CREDENCIAIS, token_path=CAMINHO_TOKEN)

def funcao_agente_agenda():
    fusohorario = timezone(timedelta(hours=-3))
    agora = datetime.now(fusohorario)
    
    data_completa = agora.strftime("%d/%m/%Y às %H:%M:%S")
    data_exemplo_iso = agora.strftime("%Y-%m-%dT%H:%M:%S-03:00")
    
    ano_atual = agora.year
    
    agente = Agent(
        name='Agente Agenda',
        role='Você é um assistente pessoal produtivo especializado em gestão de tempo e agendas.',
        tools=[ferramenta_agenda],
        instructions=[
            f"CONTEXTO TEMPORAL CRÍTICO: Hoje é exatamente {data_completa}. O ano atual é {ano_atual}.",
            "FUSO HORÁRIO OBRIGATÓRIO: O utilizador está no fuso horário 'America/Bahia' (UTC-3).",
            "REGRAS DE AGENDAMENTO E FERRAMENTAS (INEGOCIÁVEIS):",
            "1. PARÂMETRO TIMEZONE: Em TODAS as chamadas de ferramentas (create_event, update_event, etc), você DEVE preencher o argumento 'timezone' EXPLICITAMENTE com o valor 'America/Bahia'.",
            "2. FORMATO DA DATA: Use o formato ISO exato com o offset local: 'YYYY-MM-DDTHH:MM:SS-03:00'.",
            "3. REGRA DE ALTERAÇÃO (MUITO IMPORTANTE): Quando o usuário pedir para ALTERAR ou REMARCAR, é ESTRITAMENTE PROIBIDO usar a ferramenta `create_event`. Você DEVE executar DUAS ETAPAS:",
            "   - ETAPA 1: Use `search_events` com uma palavra-chave para encontrar o evento desejado e copie o seu 'id'.",
            "   - ETAPA 2: Use `update_event` passando o 'id' encontrado, as novas datas e OBRIGATORIAMENTE o timezone='America/Bahia'.",
            "4. Nunca responda que fez algo sem ter recebido a mensagem de 'success' da ferramenta.",
            "5.Caso tenha Evento ou Agenda de Parabéns do usuário, não adicione na consulta e nem retorne, apenas ignore!"
        ],
        read_tool_call_history = True 
    )
    return agente